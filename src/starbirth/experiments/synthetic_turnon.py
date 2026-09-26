from __future__ import annotations

import argparse
import numpy as np

from starbirth.features.change_point import best_persistent_step


def wise_like_epochs(n_epochs: int = 21, exposures_per_epoch: int = 12) -> np.ndarray:
    """Simplified NEOWISE cadence: ~12 exposures in ~1 day every ~6 months."""
    epoch_centers = np.arange(n_epochs, dtype=float) * 182.625
    intra = np.linspace(-0.45, 0.45, exposures_per_epoch)
    return (epoch_centers[:, None] + intra[None, :]).reshape(-1)


def simulate_one(
    rng: np.random.Generator,
    amplitude_sigma: float,
    birth_epoch: int,
    noise_sigma: float = 1.0,
    n_epochs: int = 21,
    exposures_per_epoch: int = 12,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    t = wise_like_epochs(n_epochs, exposures_per_epoch)
    flux = rng.normal(0.0, noise_sigma, size=t.size)
    start = birth_epoch * exposures_per_epoch
    flux[start:] += amplitude_sigma * noise_sigma
    sigma = np.full_like(flux, noise_sigma)
    return t, flux, sigma


def run_grid(
    trials: int = 2000,
    seed: int = 42,
    threshold_delta_bic: float = 20.0,
) -> list[dict[str, float]]:
    rng = np.random.default_rng(seed)
    amplitudes = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
    results: list[dict[str, float]] = []
    for amp in amplitudes:
        detected = 0
        localized = 0
        for _ in range(trials):
            birth_epoch = int(rng.integers(4, 17))
            _, f, s = simulate_one(rng, amp, birth_epoch)
            cp = best_persistent_step(f, s, min_points_each_side=24)
            if cp.delta_bic >= threshold_delta_bic and cp.amplitude > 0:
                detected += 1
                expected_index = birth_epoch * 12
                if cp.index is not None and abs(cp.index - expected_index) <= 12:
                    localized += 1
        results.append(
            {
                "amplitude_sigma": amp,
                "detection_rate": detected / trials,
                "localization_rate": localized / trials,
            }
        )
    return results


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--trials", type=int, default=2000)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--threshold-delta-bic", type=float, default=20.0)
    args = p.parse_args()
    rows = run_grid(args.trials, args.seed, args.threshold_delta_bic)
    print("amplitude_sigma,detection_rate,localization_rate")
    for r in rows:
        print(f"{r['amplitude_sigma']:.2f},{r['detection_rate']:.4f},{r['localization_rate']:.4f}")


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
import platform
import time
import numpy as np

from starbirth.experiments.synthetic_turnon import simulate_one
from starbirth.features.change_point import best_persistent_step


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--curves", type=int, default=50_000)
    args = p.parse_args()
    rng = np.random.default_rng(123)

    t0 = time.perf_counter()
    detections = 0
    for _ in range(args.curves):
        birth_epoch = int(rng.integers(4, 17))
        _, f, s = simulate_one(rng, 1.0, birth_epoch)
        r = best_persistent_step(f, s, min_points_each_side=24)
        detections += r.delta_bic > 20 and r.amplitude > 0
    dt = time.perf_counter() - t0

    print(f"host={platform.platform()}")
    print(f"python={platform.python_version()}")
    print(f"curves={args.curves}")
    print(f"seconds={dt:.3f}")
    print(f"curves_per_second={args.curves/dt:.1f}")
    print(f"detected={detections}")

    try:
        import torch
        print(f"torch={torch.__version__}")
        print(f"mps_available={bool(getattr(torch.backends, 'mps', None) and torch.backends.mps.is_available())}")
        print(f"cuda_available={torch.cuda.is_available()}")
    except Exception as e:
        print(f"torch=unavailable ({e})")


if __name__ == "__main__":
    main()

#!/usr/bin/env bash
set -euo pipefail
python -m starbirth.experiments.synthetic_turnon --trials "${1:-5000}" --seed 42

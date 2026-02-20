# OpenPI Setup Quickstart

This guide gives a minimal, copy-paste setup flow for running `openpi` locally.

## 1) Clone and initialize submodules

```bash
git clone --recurse-submodules git@github.com:Physical-Intelligence/openpi.git
cd openpi
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

## 2) Install dependencies with uv

Install `uv` first (see the official Astral docs), then run:

```bash
GIT_LFS_SKIP_SMUDGE=1 uv sync
GIT_LFS_SKIP_SMUDGE=1 uv pip install -e .
```

`GIT_LFS_SKIP_SMUDGE=1` is required for pulling LeRobot as a dependency.

## 3) Verify environment

```bash
uv run python -c "import openpi; print('openpi import OK')"
uv run python -c "import jax, torch; print('jax', jax.__version__, 'torch', torch.__version__)"
```

## 4) (Optional) PyTorch-specific setup

If you plan to run PyTorch models:

```bash
uv pip show transformers
cp -r ./src/openpi/models_pytorch/transformers_replace/* .venv/lib/python3.11/site-packages/transformers/
```

## 5) Run a first command

Start a policy server using a checkpoint:

```bash
uv run scripts/serve_policy.py policy:checkpoint --policy.config=pi05_libero --policy.dir=/path/to/checkpoint
```

## I have GitHub Copilot CLI set up — now what?

Great — use Copilot CLI as a helper while you run the real `openpi` workflow:

1. **Ask Copilot to explain commands before you run them**
   ```bash
   gh copilot explain "uv run scripts/compute_norm_stats.py --config-name pi05_libero"
   ```
2. **Ask Copilot to suggest the next command**
   ```bash
   gh copilot suggest "start pi05_libero training in openpi"
   ```
3. **Run the actual openpi commands yourself** (copy from this guide or README).

A practical first sequence after setup is:

```bash
# compute normalization stats for your config
uv run scripts/compute_norm_stats.py --config-name pi05_libero

# launch training
XLA_PYTHON_CLIENT_MEM_FRACTION=0.9 uv run scripts/train.py pi05_libero --exp-name=my_experiment --overwrite

# serve a trained checkpoint
uv run scripts/serve_policy.py policy:checkpoint --policy.config=pi05_libero --policy.dir=checkpoints/pi05_libero/my_experiment/20000
```

Copilot CLI is optional convenience; it does not replace these project commands.

## Troubleshooting

- If submodule-related imports fail, rerun: `git submodule update --init --recursive`.
- If dependency resolution is inconsistent, rerun: `uv sync`.
- If PyTorch transformer patches cause issues, clean cache: `uv cache clean transformers` and reinstall.

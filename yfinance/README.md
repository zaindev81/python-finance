# yfinance

## Setup

```sh
uv init
uv venv
source .venv/bin/activate
uv pip install yfinance argsparse
```

## Activate

```sh
uv venv
source .venv/bin/activate
uv sync
```

## Development

```sh
# examples
uv run python examples/01_basic_history.py --ticker AAPL --period 3mo
```
# Passcode Brute-Force Simulation

This project simulates brute-forcing random numeric passcodes and records how many guesses it takes to find them. It's intended as a simple experiment for collecting data and comparing outcomes across different passcode lengths (4–8 digits).

## Files

- `main.py` generates random passcodes, simulates guessing them, and appends results to `results.csv`.
- `analyze.py` reads `results.csv` and prints a short summary for each passcode length.

## Running

Generate data (by default 100 samples per passcode length; either adjust this value or run the script multiple times to collect more data):

```sh
uv run main.py
```

Analyze collected results:

```sh
uv run analyze.py
```

## Output

The simulation writes (append-only) to a `results.csv` file containing, in each line:

- `length`: number of digits in the passcode
- `passcode`: the actual generated passcode
- `guesses`: how many guesses were needed to brute-force it

The analysis script only prints its results to the console.

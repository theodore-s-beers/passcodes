import numpy as np


def main():
    data = np.genfromtxt("results.csv", delimiter=",", names=True, dtype=int)

    for length in np.unique(data["length"]):
        avg_guesses = int(np.rint(np.mean(data["guesses"][data["length"] == length])))
        print(f"Length {length}: {avg_guesses}")


if __name__ == "__main__":
    main()

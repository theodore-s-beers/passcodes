import numpy as np


def main():
    data = np.genfromtxt("results.csv", delimiter=",", names=True, dtype=int)

    for length in np.unique(data["length"]):
        samples = data[data["length"] == length]
        guesses = samples["guesses"]

        avg_guesses = int(np.rint(np.mean(guesses)))
        lucky_idx = int(np.argmin(guesses))
        unlucky_idx = int(np.argmax(guesses))

        print(f"Length {length}:")
        print(f"  Samples: {samples.size}")
        print(f"  Average guesses: {avg_guesses}")
        print(f"  Luckiest run: {int(guesses[lucky_idx])} guesses")
        print(f"  Unluckiest run: {int(guesses[unlucky_idx])} guesses")


if __name__ == "__main__":
    main()

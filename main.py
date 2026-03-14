# We'll be saving experiment results in a CSV (Comma-Separated Values) file
import csv

# Import NumPy, a package that will make the math we do here much, much faster
import numpy as np

# Set up a random number generator for NumPy
rng = np.random.default_rng()

# The file name we'll use to save results
RESULTS_FILE = "results.csv"


# Since we're using only digits for our "passwords," it's more efficient to think of
# them as numbers rather than strings. We'll generate a number >= 0 and < a limit,
# determined by the length of the passcode. e.g., for a 4-digit passcode, the limit is
# 10^4 = 10000, meaning we can generate any number from 0 (i.e. "0000") to 9999.
def generate_passcode(length: int) -> tuple[int, int]:
    # Calculate the limit
    limit: int = 10**length

    # Generate a random passcode as a number between 0 and the limit
    passcode = int(rng.integers(limit))

    # Return both the passcode and the limit for convenience
    return passcode, limit


def guess_passcode(passcode: int, limit: int) -> int:
    # Start by creating a list of every possible number/passcode up to the limit
    choices = np.arange(limit, dtype=np.uint32)

    # Shuffle the possible choices into a random order
    # This is how we'll simulate brute-forcing, making random guesses without repeats
    # Once we have the list of choices in random order, we can just iterate through it
    # However far we go before landing on the passcode is how many "guesses" it took
    rng.shuffle(choices)

    # We'll keep track of "guesses"
    guesses = 0

    # Start going through the randomized list of choices
    for guess in choices:
        # Count each guess
        guesses += 1

        # If this is the lucky number, return how many guesses it took to find it
        if guess == passcode:
            return guesses

    # It should be impossible to reach this spot; it would indicate a bug in the code
    raise ValueError("Passcode not found")


# This function combines `generate_passcode` and `guess_passcode`. We just tell it what
# passcode length to use, and it generates a random passcode of that length, then
# brute-force guesses it, and reports how many guesses it took. We'll run this function
# many times for each passcode length, to generate many experimental samples.
def generate_sample(length: int) -> dict[str, str | int]:
    # Generate a random passcode of the given length
    # This also calculates the largest number value that can fit in that many digits
    passcode, limit = generate_passcode(length)
    # print(f"Generated {length}-digit passcode: {passcode:0{length}d}")

    # Brute-force guess the passcode, counting how many guesses it takes
    guesses = guess_passcode(passcode, limit)
    # print(f"Guesses to brute-force:     {guesses}")

    # Return the results of this sample run
    return {
        "length": length,
        "passcode": f"{passcode:0{length}d}",
        "guesses": guesses,
    }


# This function takes a sample result and saves it to our CSV file
def save_result(result: dict[str, str | int]) -> None:
    # Open the CSV file to add the newest result to it
    with open(RESULTS_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=result.keys())

        # If this is the first time we write to the file, we need to add a "header row"
        if file.tell() == 0:
            writer.writeheader()

        # Add the result row to the CSV file
        writer.writerow(result)


# The actual "main" function that runs when we execute the script
def main():
    # Set the minimum and maximum passcode lengths we want to test
    min_length = 4
    max_length = 8

    # Make sure the lengths we're using are valid and feasible
    assert min_length > 0, "Passcode lengths must be positive numbers"
    assert min_length <= max_length, "Minimum length must be <= maximum length"
    assert max_length <= 8, "Maximum practical passcode length is 8 digits"

    # How many samples to collect for each passcode length?
    samples_per_length = 100

    # Generate and save the desired number of samples for each passcode length
    for length in range(min_length, max_length + 1):
        for _ in range(samples_per_length):
            result = generate_sample(length)
            save_result(result)


# This tells Python to run the main function only when we execute the script directly
if __name__ == "__main__":
    main()

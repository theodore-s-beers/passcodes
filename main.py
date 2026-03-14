# Import NumPy, a package that will make the math we do here much, much faster
import numpy as np

# Set up a random number generator for NumPy
rng = np.random.default_rng()


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


# The actual "main" function that runs when we execute the script
def main():
    # Set the length and make sure it's valid
    length = 8
    assert length > 0, "Length must be a positive integer"
    assert length <= 8, "Maximum length is 8 digits"

    # Generate a random passcode
    passcode, limit = generate_passcode(length)
    print(f"Generated {length}-digit passcode: {passcode:0{length}d}")

    # Brute-force the passcode and report how many guesses it took
    guesses = guess_passcode(passcode, limit)
    print(f"Guesses to brute-force:     {guesses}")


# This tells Python to run the main function only when we execute the script directly
if __name__ == "__main__":
    main()

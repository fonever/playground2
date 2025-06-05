import random


def print_grid(rows=10, cols=10):
    """Prints a grid of random characters."""
    chars = "*#@$"
    for _ in range(rows):
        line = ''.join(random.choice(chars) for _ in range(cols))
        print(line)


if __name__ == "__main__":
    print_grid()

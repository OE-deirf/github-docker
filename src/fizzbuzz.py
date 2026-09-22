"""FizzBuzz simple implementation"""

LIMIT = 100  # limit


def fizzbuzz(n: int) -> str:
    "FizzBuzz decision"
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def fizzbuzz_range(limit: int = LIMIT) -> list[str]:
    """FizzBuzz with range"""
    return [fizzbuzz(i) for i in range(1, limit + 1)]


if __name__ == "__main__":
    print(" ".join(fizzbuzz_range()))

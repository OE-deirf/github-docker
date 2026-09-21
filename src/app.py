import time
from fizzbuzz import fizzbuzz_range, LIMIT

VERZIO = "v1"


def main():
    print(f"[{VERZIO}] FizzBuzz starting, upper bound = {LIMIT}", flush=True)
    while True:
        result = fizzbuzz_range(LIMIT)
        print(
            f"[{VERZIO}] {LIMIT}-ig: ... {' '.join(result[-5:])}",
            flush=True)
        print(f"[{VERZIO}] count: {len(result)}", flush=True)
        time.sleep(10)


if __name__ == "__main__":
    main()

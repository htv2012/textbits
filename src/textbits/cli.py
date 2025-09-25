import argparse

from .serve import serve


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["serve"])
    options, args = parser.parse_known_args()

    print(f"{options=}")
    print(f"{args=}")

    if options.action == "serve":
        serve(args)

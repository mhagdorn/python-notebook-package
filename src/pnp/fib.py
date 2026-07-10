import argparse
from .fibonacci import fibonacci
from ._version import __version__


def arg_parser():
    parser = argparse.ArgumentParser(
        description="Program computing numbers of the Fibonacci sequence")
    parser.add_argument(
        "-n", "--num-fib", type=int, default=10,
        help="the number of Fibonacci numbers to produce, default: 10")
    parser.add_argument(
        "--version", action="version",
        version=f'%(prog)s {__version__}')
    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()

    for f in fibonacci(args.num_fib):
        print(f)

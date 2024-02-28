import argparse


def parser() -> None:
    my_parser: any = argparse.ArgumentParser()
    my_parser.add_argument("num_string", type=int, help="add number of strings")
    args: any = my_parser.parse_args()
    if args.num_string > 0:
        for _ in range(args.num_string):
            check_zero(input())


def check_zero(string: str) -> None:
    if(len(string) == 33 and string.startswith("00000") and not string.startswith("000000")):
        print(string)


def main():
    parser()


if __name__ == "__main__":
    main()
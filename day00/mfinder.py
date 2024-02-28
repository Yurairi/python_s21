import re


def reader() -> None:
    fl: bool = True
    for i in range(3):
        init_string: str = input()
        fl = parcer(init_string, i, fl)
    print(fl)


def parcer(line: str, i: int, fl: bool) -> bool:
    example: tuple[str] = (r"\*[^*]{3}\*", r"\*\*[^*]{1}\*\*", r"\*[^*]\*[^*]\*")
    if len(line) != 6:
        fl = False
    if not re.search(example[i], line):
        fl = False
    return fl


def main():
    reader()


if __name__ == "__main__":
    main()
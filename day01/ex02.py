from typing import Dict

golds = "golden_ingots"


def signaler(my_func: any) -> any:
    def wrapper(purse: Dict[str, int]) -> Dict[str, int]:
        print("SQUEAK")
        return my_func(purse)

    return wrapper


@signaler
def empty(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse: Dict[str, int] = {}
    return new_purse


@signaler
def add_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse: Dict[str, int] = {golds: 1}
    if golds in purse:
        new_purse[golds] += purse[golds]
    return new_purse


@signaler
def get_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse: Dict[str, int] = {golds: 0}
    if golds in purse:
        new_purse[golds] = purse[golds] - 1
    return new_purse


def main():
    empty_purse: Dict[str, int] = {}
    purse: Dict[str, int] = {golds: 1, "money": 67}
    print(empty(purse))
    print(add_ingot(purse))
    print(get_ingot(purse))
    print(get_ingot(add_ingot(add_ingot(add_ingot(purse)))))
    print(add_ingot(get_ingot(add_ingot(empty(empty_purse)))))


if __name__ == "__main__":
    main()
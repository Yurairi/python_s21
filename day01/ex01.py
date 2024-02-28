from typing import List, Dict

golds: str = "golden_ingolt"


def split_booty(*purses: Dict[str, int]) -> List[Dict[str, int]]:
    result_purses: List[Dict[str, int]] = []
    count_of_ingolts: int = 0
    for purse in purses:
        if golds in purse:
            count_of_ingolts += purse[golds]

    real_amount: int = count_of_ingolts // 3
    extra_amount: int = count_of_ingolts % 3

    for _ in range(3):
        new_purse: Dict[str, int] = {golds: real_amount}
        if extra_amount > 0:
            new_purse[golds] += 1
        extra_amount -= 1
        result_purses.append(new_purse)

    return result_purses


def main():
    empty_purse: Dict[str, int] = {}
    purses: List[Dict[str, int]] = [
        {golds: 2},
        {golds: 3},
        {golds: 1},
        {golds: 4},
        {golds: 7},
        {golds: 3},
        {golds: 2},
        {"apples": 10},
    ]  # 17
    v1, v2, v3 = split_booty(purses[5], purses[6], purses[7])
    print(v1, v2, v3)


if __name__ == "__main__":
    main()


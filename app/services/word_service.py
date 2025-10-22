import random


def get_random_word(level: int) -> str:
    words_by_level = {
        1: ["eat", "fat"],
        2: ["eat", "fat"],
        3: ["eat", "fat"],
        4: ["eat", "fat"],
        5: ["eat", "fat"],
        6: ["eat", "fat"],
        7: ["eat", "fat"],
        8: ["eat", "fat"],
        9: ["eat", "fat"],
        10: ["eat", "fat"],
    }
    word: str = random.choice(seq=words_by_level[level])
    return word

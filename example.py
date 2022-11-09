import numpy as np
import json
from zipf import inverse_cdf_fast


def main():
    with open("data/english_10k_sorted.json", "r") as f:
        mt_10k = json.load(f)
    mt_10k_words = mt_10k["words"]
    example_str = ""
    for i in range(0, 20):
        index = inverse_cdf_fast(np.random.uniform(0, 1), 1.1, 10_000)
        word = mt_10k_words[index]
        example_str += word + " "
    print(example_str)
    return


if __name__ == "__main__":
    main()

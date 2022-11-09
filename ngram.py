import json


def main():
    with open("data/english_10k.json", "r") as f:
        mt_10k = json.load(f)
    mt_10k_words = mt_10k["words"]
    with open("data/google-10000-english-no-swears.txt", "r") as f:
        google_10k = f.readlines()
    for idx, word in enumerate(google_10k):
        google_10k[idx] = word.strip("\n")
    list_index = []
    for word in mt_10k_words:
        try:
            list_index.append(google_10k.index(word))
        except ValueError:
            list_index.append(10000)
    mt_10k_words_sorted = [
        x for (y, x) in sorted(zip(list_index, mt_10k_words), key=lambda pair: pair[0])
    ]
    mt_10k["words"] = mt_10k_words_sorted
    mt_10k["name"] = "english_10k_sorted"
    json_string = json.dumps(mt_10k, skipkeys=False, indent=2)
    with open("data/english_10k_sorted.json", "w") as f:
        f.write(json_string)
    return


if __name__ == "__main__":
    main()

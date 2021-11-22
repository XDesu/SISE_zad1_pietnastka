import glob
import os
import pickle

DICT = {}

if __name__ == "__main__":

    for file in glob.glob("./statistics/*.txt"):
        filename = os.path.basename(file)
        dimensions, difficulty, number, algorithm, param, stats = filename.split(
            "_")
        length, visited, processed, depth, time = 0, 0, 0, 0, 0
        with open(file, "r") as f:
            length = int(f.readline())
            visited = int(f.readline())
            processed = int(f.readline())
            depth = int(f.readline())
            time = float(f.readline())
        if difficulty not in DICT:
            DICT[difficulty] = {}
        if number not in DICT[difficulty]:
            DICT[difficulty][number] = {}
        if algorithm not in DICT[difficulty][number]:
            DICT[difficulty][number][algorithm] = {}
        if param not in DICT[difficulty][number][algorithm]:
            DICT[difficulty][number][algorithm][param] = {}
        DICT[difficulty][number][algorithm][param]["length"] = length
        DICT[difficulty][number][algorithm][param]["visited"] = visited
        DICT[difficulty][number][algorithm][param]["processed"] = processed
        DICT[difficulty][number][algorithm][param]["depth"] = depth
        DICT[difficulty][number][algorithm][param]["time"] = time

    out_file = open("data.puzz", "wb")
    pickle.dump(DICT, out_file)
    out_file.close()


def load_data():
    in_file = open("data.puzz", "rb")
    DICT = pickle.load(in_file)
    in_file.close()
    return DICT

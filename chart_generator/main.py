from dumpy import load_data
from matplotlib import pyplot as plt
import os

DATA = load_data()
STATISTICS = ['length', 'visited', 'processed', 'depth', 'time']
if not os.path.exists("charts"):
    os.makedirs("charts")
if not os.path.exists("charts/general"):
    os.makedirs("charts/general")
if not os.path.exists("charts/exact"):
    os.makedirs("charts/exact")
if not os.path.exists("charts/exist"):
    os.makedirs("charts/exist")

# ogólne statystyki per algorytm
general_averages = {}
# dokładne statystyki per algorytm (podział na metody (param))
exact_averages = {}

exist_averages = {}
for difficulty in DATA:
    for number in DATA[difficulty]:
        for algorithm in DATA[difficulty][number]:
            if algorithm not in general_averages:
                general_averages[algorithm] = {}
            if algorithm not in exact_averages:
                exact_averages[algorithm] = {}
            if algorithm not in exist_averages:
                exist_averages[algorithm] = {}
                exist_averages[algorithm]['exist'] = 0
                exist_averages[algorithm]['not_exist'] = 0
            for param in DATA[difficulty][number][algorithm]:
                ### statystyki istnienia rozwiązań ###
                if DATA[difficulty][number][algorithm][param]["length"] == -1:
                    exist_averages[algorithm]["not_exist"] += 1
                    continue
                exist_averages[algorithm]["exist"] += 1
                ### ogólne statystyki ###
                if "counter" not in general_averages[algorithm]:
                    general_averages[algorithm]["counter"] = 0
                if "length" not in general_averages[algorithm]:
                    general_averages[algorithm]["length"] = 0
                if "visited" not in general_averages[algorithm]:
                    general_averages[algorithm]["visited"] = 0
                if "processed" not in general_averages[algorithm]:
                    general_averages[algorithm]["processed"] = 0
                if "depth" not in general_averages[algorithm]:
                    general_averages[algorithm]["depth"] = 0
                if "time" not in general_averages[algorithm]:
                    general_averages[algorithm]["time"] = 0
                general_averages[algorithm]["length"] += DATA[difficulty][number][algorithm][param]["length"]
                general_averages[algorithm]["visited"] += DATA[difficulty][number][algorithm][param]["visited"]
                general_averages[algorithm]["processed"] += DATA[difficulty][number][algorithm][param]["processed"]
                general_averages[algorithm]["depth"] += DATA[difficulty][number][algorithm][param]["depth"]
                general_averages[algorithm]["time"] += DATA[difficulty][number][algorithm][param]["time"]
                general_averages[algorithm]["counter"] += 1

                ### dokładne statystyki ###
                if param not in exact_averages[algorithm]:
                    exact_averages[algorithm][param] = {}
                if "counter" not in exact_averages[algorithm][param]:
                    exact_averages[algorithm][param]["counter"] = 0
                if "length" not in exact_averages[algorithm][param]:
                    exact_averages[algorithm][param]["length"] = 0
                if "visited" not in exact_averages[algorithm][param]:
                    exact_averages[algorithm][param]["visited"] = 0
                if "processed" not in exact_averages[algorithm][param]:
                    exact_averages[algorithm][param]["processed"] = 0
                if "depth" not in exact_averages[algorithm][param]:
                    exact_averages[algorithm][param]["depth"] = 0
                if "time" not in exact_averages[algorithm][param]:
                    exact_averages[algorithm][param]["time"] = 0
                exact_averages[algorithm][param]["length"] += DATA[difficulty][number][algorithm][param]["length"]
                exact_averages[algorithm][param]["visited"] += DATA[difficulty][number][algorithm][param]["visited"]
                exact_averages[algorithm][param]["processed"] += DATA[difficulty][number][algorithm][param]["processed"]
                exact_averages[algorithm][param]["depth"] += DATA[difficulty][number][algorithm][param]["depth"]
                exact_averages[algorithm][param]["time"] += DATA[difficulty][number][algorithm][param]["time"]
                exact_averages[algorithm][param]["counter"] += 1

for algorithm in general_averages:
    counter = general_averages[algorithm]["counter"]
    general_averages[algorithm]["length"] = round(
        general_averages[algorithm]["length"] / counter, 3)
    general_averages[algorithm]["visited"] = round(
        general_averages[algorithm]["visited"] / counter, 3)
    general_averages[algorithm]["processed"] = round(
        general_averages[algorithm]["processed"] / counter, 3)
    general_averages[algorithm]["depth"] = round(
        general_averages[algorithm]["depth"] / counter, 3)
    general_averages[algorithm]["time"] = round(
        general_averages[algorithm]["time"] / counter, 3)

for algorithm in exact_averages:
    for param in exact_averages[algorithm]:
        counter = exact_averages[algorithm][param]["counter"]
        exact_averages[algorithm][param]["length"] = round(
            exact_averages[algorithm][param]["length"] / counter, 3)
        exact_averages[algorithm][param]["visited"] = round(
            exact_averages[algorithm][param]["visited"] / counter, 3)
        exact_averages[algorithm][param]["processed"] = round(
            exact_averages[algorithm][param]["processed"] / counter, 3)
        exact_averages[algorithm][param]["depth"] = round(
            exact_averages[algorithm][param]["depth"] / counter, 3)
        exact_averages[algorithm][param]["time"] = round(
            exact_averages[algorithm][param]["time"] / counter, 3)

for stat in STATISTICS:
    plt.clf()
    plt.title(f"ogólne statystyki - {stat}")
    if stat == 'time':
        plt.ylabel(f"{stat} [ms]")
    else:
        plt.ylabel(f"{stat}")
    plt.xlabel("algorytm")
    plt.bar(list(general_averages.keys()), [
        general_averages[algorithm][stat] for algorithm in general_averages])
    plt.savefig(f"./charts/general/{stat}_general.png")


keys = ["astr", "bfs"]
for stat in STATISTICS:
    plt.clf()
    plt.title(f"ogólne statystyki - {stat}")
    if stat == 'time':
        plt.ylabel(f"{stat} [ms]")
    else:
        plt.ylabel(f"{stat}")
    plt.xlabel("algorytm")
    plt.bar(list(keys), [
        general_averages[algorithm][stat] for algorithm in keys])
    plt.savefig(f"./charts/general/{stat}_general_small.png")

for algorithm in exact_averages:
    for stat in STATISTICS:
        plt.clf()
        plt.title(f"dokładne statystyki - {algorithm} - {stat}")
        if stat == 'time':
            plt.ylabel(f"{stat} [ms]")
        else:
            plt.ylabel(f"{stat}")
        plt.xlabel("parametr")
        plt.bar(list(exact_averages[algorithm].keys()), [
            exact_averages[algorithm][param][stat] for param in exact_averages[algorithm]])
        plt.savefig(f"./charts/exact/{stat}_{algorithm}.png")

# to jest trochę złe, można by poprawić, żeby lepiej zobrazować
# to ile procentowo jest znalezionych rozwiązań, a ile nie.
# (tak na prawdę ma to znaczenie, tylko dla DFS ślądzącego
# odwiedzone stany, wszystko inne powinno mieć 100% znalezionych rozwiązań)
for ex in ["exist", "not_exist"]:
    plt.clf()
    plt.title(f"statystyki istnienia rozwiązań - {ex}")
    plt.ylabel(f"liczba rozwiązań {ex}")
    plt.xlabel("algorytm")
    plt.bar(list(general_averages.keys()), [
        exist_averages[algorithm][ex] for algorithm in exist_averages])
    plt.savefig(f"./charts/exist/{ex}_existance.png")

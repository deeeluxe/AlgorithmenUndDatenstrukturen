# (2) Machen Sie sich mit dem Bubblesort Algorithmus bekannt. Erzeugen Sie unsortierte (also zufällige) Arrays mit beliebigen natürlichen Zahlen der Längen (n=500, 1000, 1500, 2000, 2500, 3000, 3500, 4000).
# (Tipp: wählen Sie den Bereich der natürlichen Schlüsselwerte groß, damit es beim zufälligen Erzeugen zu möglichst wenigen Mehrfach auswahlen kommt)
# Sortieren Sie diese jeweils mit Bubblesort und speichern Sie die dazu benötigen Rechenzeiten. Geben Sie diese als Grafik aus. Welche Vermutung der Zeitabhängigkeit T(n) könnte man anstellen?
# Prüfen Sie dies mit einem Fit der Daten an die vermutete Abhängigkeit (mit einer Python Fit routine). Geben Sie Fit und Daten in einer Grafik wider.
from typing import Callable, Any, Tuple

import time
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


def measure_runtime(func: Callable, *args, **kwargs) -> Tuple[Any, float]:
    """
    Führt eine Funktion aus und misst ihre Laufzeit.

    :param func: Die auszuführende Funktion
    :param args: Positionsargumente für die Funktion
    :param kwargs: Keyword-Argumente für die Funktion
    :return: Tuple aus (Rückgabewert der Funktion, Laufzeit in Sekunden)
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()

    runtime = end_time - start_time
    return result, runtime


def bubble_sort(sort_array: npt.NDArray) -> npt.NDArray:
    """
    Sortiert ein NumPy-Array mithilfe des Bubble-Sort-Algorithmus in aufsteigender Reihenfolge.

    Bubble Sort vergleicht wiederholt benachbarte Elemente und vertauscht sie,
    falls sie in der falschen Reihenfolge stehen. Der Algorithmus hat eine
    Laufzeit von O(n²) im Worst- und Average-Case.

    :param sort_array: NumPy-Array mit vergleichbaren Elementen
    :return: das sortierte NumPy-Array (in-place sortiert)
    """
    sort_len = len(sort_array)
    for i in range(sort_len):
        swapped = False
        for j in range(sort_len - i - 1):
            if sort_array[j] > sort_array[j + 1]:
                sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
                swapped = True
        if not swapped:
            break
    return sort_array


def plot_runtime_comparison(times_list: list, length: list) -> None:
    """
    Vergleicht die Laufzeiten zweier Algorithmen in einem Diagramm.

    :param times_list: Array mit Laufzeiten
    :param length: Liste mit Länge des zu sortierendem Arrays
    """
    plt.figure(figsize=(8, 5))

    plt.plot(length, times_list, marker="o")

    plt.title("Laufzeitvergleich Bubblesort")
    plt.xlabel("Messung / n")
    plt.ylabel("Zeit in Sekunden")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    n = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000]
    ts = []
    for size in n:
        arr = np.random.randint(1, size * 10, size=size)
        sorted_arr, t = measure_runtime(bubble_sort, arr)
        ts.append(t)

    plot_runtime_comparison(ts, n)
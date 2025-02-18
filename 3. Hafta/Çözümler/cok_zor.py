import csv
import time
import random
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.is_running:
            wrapper.is_running = True
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} çalıştı. Süre: {end - start} saniye")
            wrapper.is_running = False
            return result
        else:
            return func(*args, **kwargs)
    wrapper.is_running = False
    return wrapper

"""
# Bu zor kısım için yeterliydi. Üstteki kodun farkı recursive fonksiyonlarda tek tek çağırılmamasıydı.
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper
"""


@timer
def bubble_sort(data):
    for i in range(len(data)):
        swapped = False
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data

@timer
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

@timer
def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

@timer
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
    return data

@timer
def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

@timer
def bogosort(data):
    while not all(data[i] <= data[i + 1] for i in range(len(data) - 1)):
        random.shuffle(data)
    return data

def main():
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip the header row
        data = [float(row[0]) for row in reader]
    
    sorted_data_bubble = bubble_sort(data.copy())
    with open("sorted_bubble.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["value"])
        for row in sorted_data_bubble:
            writer.writerow([row])
    
    sorted_data_insertion = insertion_sort(data.copy())
    with open("sorted_insertion.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["value"])
        for row in sorted_data_insertion:
            writer.writerow([row])
    
    sorted_data_selection = selection_sort(data.copy())
    with open("sorted_selection.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["value"])
        for row in sorted_data_selection:
            writer.writerow([row])
    
    sorted_data_merge = merge_sort(data.copy())
    with open("sorted_merge.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["value"])
        for row in sorted_data_merge:
            writer.writerow([row])
    
    sorted_data_quick = quick_sort(data.copy())
    with open("sorted_quick.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["value"])
        for row in sorted_data_quick:
            writer.writerow([row])

    
    print("Tüm sıralama işlemleri tamamlandı.")

if __name__ == "__main__":
    main()
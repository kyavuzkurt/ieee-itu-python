import csv
import random

def datagen(size):
    with open("data.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["value"])
        for _ in range(size):
            writer.writerow([random.random()*random.randint(1, 10000)])

datagen(15000)


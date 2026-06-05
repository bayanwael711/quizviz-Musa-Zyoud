import csv

def create_sample_data(filepath="scores.csv"):
    rows = [
        ["name", "q1", "q2", "q3", "q4", "q5"],
        ["Bayan", 8, 7, 9, 6, 10],
        ["Ayah", 5, 4, 6, 5, 7],
        ["Alaa", 10, 9, 10, 8, 9],
        ["Amjaad", 3, 4, 2, 5, 4],
        ["Hussein", 7, 6, 8, 7, 9],
        ["Mona", 4, 5, 3, 4, 4],
        ["Wael", 9, 8, 10, 9, 8],
        ["Noor", 6, 5, 7, 6, 5],
    ]

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"Sample data created: {filepath}")


if __name__ == "__main__":
    create_sample_data()
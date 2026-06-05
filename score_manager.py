import csv
import json
import numpy as np


class ScoreManager:


    def load_scores(self, filepath: str):
        students = []
        keys = ["q1", "q2", "q3", "q4", "q5"]

        with open(filepath, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # convert to integers
                for key in keys:
                    row[key] = int(row[key])

                # compute total + average
                total = sum(row[k] for k in keys)
                avg = round(total / 5, 2)

                row["total"] = total
                row["average"] = avg
                row["status"] = "Pass" if avg >= 5 else "Fail"

                students.append(row)

        return students

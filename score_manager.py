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
                
                for key in keys:
                    row[key] = int(row[key])

                total = sum(row[k] for k in keys)
                avg = round(total / 5, 2)

                row["total"] = total
                row["average"] = avg
                row["status"] = "Pass" if avg >= 5 else "Fail"

                students.append(row)

        return students
    
    def calculate_stats(self, students: list):
        averages = np.array([s["average"] for s in students])

        stats = {
        "total_students": len(students),
        "class_average": round(float(np.mean(averages)), 2),
        "highest_average": round(float(np.max(averages)), 2),
        "lowest_average": round(float(np.min(averages)), 2),
        "std_deviation": round(float(np.std(averages)), 2),
        "pass_count": int(np.sum(averages >= 5)),
        "fail_count": int(np.sum(averages < 5))
    }

        return stats

    def save_report(self, students: list, stats: dict, filepath: str):
        report = {
        "summary": stats,
        "students": students
    }

        with open(filepath, "w") as f:
            json.dump(report, f, indent=2)

        print(f"Report saved: {filepath}")


if __name__ == "__main__":
     sm = ScoreManager()
     students = sm.load_scores("scores.csv")
     stats = sm.calculate_stats(students)

     sm.save_report(students, stats, "report.json")    
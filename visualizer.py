import matplotlib.pyplot as plt
import numpy as np


class Visualizer:

    def bar_chart(self, students: list):
        names = [s["name"] for s in students]
        averages = [s["average"] for s in students]

        colors = ["green" if avg >= 5 else "red" for avg in averages]

        fig, ax = plt.subplots()
        ax.bar(names, averages, color=colors)

        ax.axhline(y=5, color="red", linestyle="--", label="Pass threshold (5.0)")

        ax.set_title("Student Average Scores")
        ax.set_xlabel("Student")
        ax.set_ylabel("Average (out of 10)")
        ax.set_ylim(0, 10)
        ax.legend()

        plt.tight_layout()
        plt.show()

    
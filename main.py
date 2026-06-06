
from score_manager import ScoreManager
from visualizer import Visualizer

def main():
    sm = ScoreManager()
    viz = Visualizer()

    # Step 1: Load data
    students = sm.load_scores("scores.csv")
    print(f"Loaded {len(students)} students\n")

    # Step 2: Calculate statistics
    stats = sm.calculate_stats(students)
    print("=== Class Statistics ===")
    for key, value in stats.items():
        print(f"  {key}: {value}")

    # Step 3: Save report
    sm.save_report(students, stats, "report.json")

    # Step 4: Visualize
    print("\nDisplaying charts...")
    viz.bar_chart(students)
    viz.histogram(students)
    viz.pie_chart(stats)

if __name__ == "__main__":
    main()


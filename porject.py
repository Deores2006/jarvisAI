import matplotlib

# Force Matplotlib to use a non-interactive backend before importing pyplot
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def analyze_student_data():
    data = {
        "Student": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"],
        "Math": [85, 72, 90, 60, 78, 92],
        "Physics": [78, 65, 88, 55, 70, 85],
        "Chemistry": [82, 70, 85, 58, 75, 90],
        "Computer": [90, 80, 95, 65, 82, 98],
    }
    df = pd.DataFrame(data)

    subjects = ["Math", "Physics", "Chemistry", "Computer"]
    df["Average"] = df[subjects].mean(axis=1)

    math_scores = df["Math"].to_numpy()
    math_mean = np.mean(math_scores)
    math_std = np.std(math_scores)

    print("=== STUDENT SUMMARY ===")
    print(df[["Student", "Average"]])
    print(f"\nMath Mean: {math_mean:.2f} | Math Std Dev: {math_std:.2f}\n")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.bar(
        df["Student"], df["Average"], color="#2563eb", edgecolor="#1e40af"
    )
    ax1.set_title("Overall Average per Student")
    ax1.set_ylabel("Average Score (%)")
    ax1.set_ylim(0, 100)
    ax1.grid(axis="y", linestyle="--", alpha=0.7)

    subj_means = df[subjects].mean()
    ax2.plot(subjects, subj_means, marker="o", color="#ef4444", linewidth=2)
    ax2.set_title("Class Average by Subject")
    ax2.set_ylabel("Score (%)")
    ax2.set_ylim(0, 100)
    ax2.grid(True, linestyle="--", alpha=0.7)

    plt.tight_layout()

    # Note: plt.show() won't open a window using 'Agg', instead you save it:
    fig.savefig("student_analysis.png")
    print("Visualisation saved successfully as 'student_analysis.png'!")


if __name__ == "__main__":
    analyze_student_data()

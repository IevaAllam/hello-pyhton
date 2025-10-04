import matplotlib.pyplot as plt

# Data
stages = ["Stage 1", "Stage 2", "Stage 3"]
values = [158, 64, 177]
total = sum(values)
percentages = [v / total * 100 for v in values]

# Create plot
plt.figure(figsize=(6, 4))
bars = plt.bar(stages, values, color="gray", edgecolor="black")

# Add text labels (percentages)
for bar, pct in zip(bars, percentages):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
             f"{pct:.1f}%", ha="center", va="bottom",
             fontname="Times New Roman", fontsize=11)

# Labels and title
plt.xlabel("AKI KDIGO Stage", fontname="Times New Roman", fontsize=12)
plt.ylabel("Number of Patients", fontname="Times New Roman", fontsize=12)
plt.title("Distribution of AKI KDIGO Stages Among Patients", fontname="Times New Roman", fontsize=14)

# Style adjustments
plt.xticks(fontname="Times New Roman", fontsize=11)
plt.yticks(fontname="Times New Roman", fontsize=11)
plt.tight_layout()

# Show plot
plt.show()

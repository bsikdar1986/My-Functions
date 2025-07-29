# Pareto chart


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample data: Asset classes and their corresponding contributions to portfolio performance
data = {
    'Asset Class': ['Real Estate', 'Private Equity', 'Cryptocurrency', 'Commodities', 'Hedge Funds', 'Venture Capital'],
    'Contribution (%)': [25, 35, 10, 15, 8, 7]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort data by contribution in descending order
df = df.sort_values('Contribution (%)', ascending=False)

# Calculate cumulative contribution
df['Cumulative Contribution (%)'] = df['Contribution (%)'].cumsum()

# List of colors for the bars (one for each asset class)
colors = ['blue', 'green', 'orange', 'red', 'purple', 'brown']  #or hexadecimal color codes like '#FF5733'

# Plot the Pareto chart
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for contributions
bars = ax1.bar(df['Asset Class'], df['Contribution (%)'], color=colors, alpha=0.6, label='Contribution (%)')

# Add text annotations to the bars (percentages)
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}%', 
             ha='center', va='bottom', fontsize=10, color='black')

# Twin axis to plot the cumulative percentage line
ax2 = ax1.twinx()
ax2.plot(df['Asset Class'], df['Cumulative Contribution (%)'], color='red', marker='o', label='Cumulative Contribution (%)', linestyle='--')

# Add a horizontal line at the 80% level
ax2.axhline(y=80, color='green', linestyle='-', linewidth=2, label='80% Threshold')

# Set axis labels
ax1.set_xlabel('Asset Class')
ax1.set_ylabel('Contribution (%)', color='blue')
ax2.set_ylabel('Cumulative Contribution (%)', color='red')

# Title and grid
plt.title('Pareto Chart: Contribution of Alternative Investments to Portfolio Performance')
ax1.grid(True, linestyle='--', alpha=0.7)

# Show the plot with a legend
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()



"""

Key Observations:
1. Top-Contributing Asset Classes (Vital Few)
The Pareto Principle suggests that a small number of asset classes will likely contribute to the majority of the portfolio performance. In the provided example, the first few asset classes (those at the top in terms of contribution percentage) will likely contribute most of the overall performance or risk.
For example, if Private Equity and Real Estate are the first two asset classes and their contributions are 35% and 25% respectively, then these two asset classes together account for 60% of the total portfolio contribution (sum of first two bars).
As you progress down the chart, the contributions become smaller, indicating that a few asset classes are driving the majority of the portfolio's performance.
2. Cumulative Contribution Line
The cumulative contribution line (shown as a red dashed line) will help you understand how quickly the total contribution builds up as you move from left to right across the bars.
If the cumulative line reaches 80% after the first few bars (which will likely be the case based on the Pareto Principle), this means that just a small subset of the asset classes (the "vital few") are responsible for the majority of the portfolio's overall contribution.
For example, if the cumulative line reaches the 80% threshold after the first 2 or 3 asset classes, this indicates that 80% of the portfolio’s performance comes from just 2 or 3 asset classes.
3. 80% Threshold Line
The 80% horizontal threshold line (green solid line) marks the point where cumulative contributions reach 80%. This line helps you easily identify which asset classes contribute to this threshold.
If the line intersects after Private Equity and Real Estate, for example, it indicates that these two asset classes alone contribute to 80% of the total portfolio performance.
Asset classes to the left of the 80% line are crucial to the portfolio’s performance, while asset classes to the right (with lower contributions) can be considered the "trivial many" that have a less significant impact.
4. Distribution of Contributions Across Asset Classes
Individual bar heights represent the contribution percentage of each asset class to the portfolio.
By observing the bar heights, you can quickly identify which asset classes are contributing significantly (e.g., bars for Private Equity and Real Estate will be taller) and which contribute less (e.g., Venture Capital and Hedge Funds might have shorter bars).
This allows you to assess whether the portfolio is well-diversified or overly reliant on a few asset classes.
5. Color-Coded Bars
The color differentiation (blue, green, orange, etc.) helps visually distinguish the individual asset classes from one another. For example, you might notice:
The first few bars could be green or blue, indicating high-contributing asset classes like Private Equity and Real Estate.
The remaining bars, which contribute less, might be assigned colors like red or brown.
This helps you quickly associate the size of each asset class’s contribution with its visual color, making the chart more intuitive.
6. Identifying the "Vital Few" and the "Trivial Many"
The Pareto chart helps identify the vital few asset classes (those contributing most to the portfolio) and the trivial many (those contributing less).
By looking at the cumulative line and the height of the bars, you can tell whether you should focus on optimizing the top-performing asset classes or whether adjustments in the lower-contributing asset classes are necessary.
For example:

If Private Equity and Real Estate contribute most of the performance (say 60% combined), you might decide to increase your allocation in those asset classes to maximize performance.
On the other hand, asset classes that contribute very little (such as Venture Capital or Hedge Funds with low contributions) might be reconsidered for their value or risk within the portfolio.
Conclusion:
From the Pareto chart, you will likely observe that a small number of asset classes contribute the majority of the portfolio’s performance (the 80/20 rule in action). The chart makes it visually clear which asset classes are crucial to your portfolio’s overall success and which ones have less impact. This insight can help in making informed decisions on portfolio rebalancing, risk management, and strategic focus. You may choose to optimize around the "vital few" that offer the highest return or performance, while reconsidering or reducing exposure to the "trivial many."

"""



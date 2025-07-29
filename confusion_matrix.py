# Confusion matrix

from sklearn.metrics import confusion_matrix
mat = confusion_matrix(ytest, test_predicted)


# Calculate the percentages
mat_percentage = mat.astype('float') / mat.sum(axis=1)[:, np.newaxis] * 100

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))
sns.set(font_scale=1.4)  # for label size
sns.set_style("whitegrid")  # for background style

# Create a heatmap with both counts and percentages
labels = ['Predicted 0-Non Default', 'Predicted 1-Default']
percent_labels = [[f'{count}\n({percent:.1f}%)' for count, percent in zip(row, perc_row)]
                  for row, perc_row in zip(mat, mat_percentage)]

# Create the heatmap
ax = sns.heatmap(mat, annot=percent_labels, fmt='', cmap='Blues', cbar=False,
                 xticklabels=labels,
                 yticklabels=['Actual 0-Non Default', 'Actual 1-Default'],
                 annot_kws={'size': 16, 'weight': 'bold'},
                 linewidths=1.5, linecolor='gray', square=True)

# Add labels and title
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.title('Confusion Matrix of Loan Default Prediction', size=18)

# Show the plot
plt.tight_layout()
plt.show()
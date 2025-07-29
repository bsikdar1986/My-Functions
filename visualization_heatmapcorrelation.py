# Heat Map for correlation


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset (using the Iris dataset as an example)
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)


def plot_correlation_heatmap(data, figsize=(10, 8), cmap='coolwarm', annot=True, fmt='.2f', cbar_shrink=0.8):
    """
    Plot a heatmap of the correlation matrix of a DataFrame.

    Parameters:
    - data: pd.DataFrame - The input DataFrame to analyze.
    - figsize: tuple - Size of the figure (width, height).
    - cmap: str - Colormap to use for the heatmap.
    - annot: bool - Whether to annotate the heatmap with correlation values.
    - fmt: str - String format for the annotations.
    - cbar_shrink: float - Shrink factor for the color bar.

    Returns:
    - None
    """
    
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
    
    # Create a mask for the upper triangle
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    
    # Set the size of the heatmap
    plt.figure(figsize=figsize)

    # Create the heatmap with improved aesthetics
    sns.heatmap(correlation_matrix, 
            mask=mask,  # Only show the lower triangle of the correlation matrix
            annot=annot,  # Whether to display the correlation coefficients in the heatmap
            cmap=cmap,  # Color map to use for the heatmap
            fmt=fmt,  # String format for the annotations (e.g., '.2f' for two decimal places)
            square=True,  # Make each cell square-shaped
            cbar_kws={"shrink": cbar_shrink},  # Color bar settings
            linewidths=.5,  # Width of the lines that will divide each cell
            linecolor='black',  # Color of the lines dividing the cells
            vmin=-1,  # Minimum value for the color scale (for better control over color mapping)
            vmax=1,  # Maximum value for the color scale
            center=0,  # Center value for the colormap
            cbar=True)  # Whether to display the color bar

    # Add title and labels
    plt.title('Correlation Heatmap of Iris Dataset', fontsize=16)
    plt.xticks(rotation=90, ha='right', fontsize=12)
    plt.yticks(rotation=0, fontsize=12)
    
     # Show the plot
    plt.tight_layout()
    plt.show()
    
# Call the function
plot_correlation_heatmap(df)




'''
Choosing an aesthetically pleasing color map for a heatmap can greatly enhance its visual appeal and clarity. Here are a few examples of good color maps that are well-suited for heatmaps, along with brief descriptions and when to use them:

1. Coolwarm
Description: A diverging color map that transitions from blue to red, making it easy to see both positive and negative correlations.
Use Case: Ideal for visualizing data where both extremes are important, such as correlation coefficients.
Example:
python
Copy code
cmap = 'coolwarm'
2. Viridis
Description: A perceptually uniform sequential color map that transitions from dark blue to bright yellow.
Use Case: Good for representing quantitative data where you want to emphasize increasing values.
Example:
python
Copy code
cmap = 'viridis'
3. Magma
Description: Another perceptually uniform sequential color map, transitioning from dark purple to bright yellow.
Use Case: Useful for heatmaps and when you want a dark-to-light gradient. It’s particularly good for representing intensity.
Example:
python
Copy code
cmap = 'magma'
4. Plasma
Description: Similar to Viridis, but with a different range of colors, transitioning from dark purple to bright yellow.
Use Case: Great for visualizing data in a way that is colorblind-friendly and perceptually uniform.
Example:
python
Copy code
cmap = 'plasma'
5. Cividis
Description: Specifically designed for color vision deficiency, transitioning from blue to yellow.
Use Case: A good choice when you want to ensure accessibility for all viewers.
Example:
python
Copy code
cmap = 'cividis'
6. RdBu
Description: A diverging color map that transitions from red to blue, which can be effective for visualizing correlations.
Use Case: Particularly useful when highlighting negative and positive correlations distinctly.
Example:
python
Copy code
cmap = 'RdBu'
Example Usage in a Heatmap
Here’s how you might implement one of these color maps in the heatmap function:

python
Copy code
# Example using 'viridis'
plot_correlation_heatmap(df, cmap='viridis')
Summary
When selecting a color map, consider the type of data you are visualizing and the message you want to convey. Sequential color maps (like Viridis and Plasma) work well for showing gradients of intensity, while diverging color maps (like Coolwarm and RdBu) are effective for highlighting differences in positive and negative values. Always keep accessibility in mind, choosing color maps that are distinguishable by individuals with color vision deficiencies when possible. '''





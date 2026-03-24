import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df_ghi = pd.read_csv('GHI_Report.csv')

# Set aesthetic style
sns.set_theme(style="whitegrid")

# a. Bar chart for correlations
cols = ['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Happiness Score']
corr = df_ghi[cols].corr()['Happiness Score'].drop('Happiness Score')

plt.figure(figsize=(8, 5))
sns.barplot(x=corr.index, y=corr.values, palette='viridis')
plt.title('Correlation with Happiness Score', fontsize=14)
plt.ylabel('Correlation Coefficient', fontsize=12)
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('correlation_barchart.png', dpi=300)
plt.close()

# b. Histogram for Happiness Score distribution
plt.figure(figsize=(8, 5))
sns.histplot(df_ghi['Happiness Score'], bins=15, kde=True, color='skyblue')
plt.title('Distribution of Happiness Scores', fontsize=14)
plt.xlabel('Happiness Score', fontsize=12)
plt.ylabel('Frequency (Number of Countries)', fontsize=12)
plt.tight_layout()
plt.savefig('happiness_distribution_histogram.png', dpi=300)
plt.close()

# c. Scatter plot: Economy vs Happiness Score
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_ghi, x='Economy (GDP per Capita)', y='Happiness Score', color='coral', s=100, alpha=0.7)
sns.regplot(data=df_ghi, x='Economy (GDP per Capita)', y='Happiness Score', scatter=False, color='darkred')
plt.title('Economy (GDP per capita) vs Happiness Score', fontsize=14)
plt.xlabel('Economy (GDP per Capita)', fontsize=12)
plt.ylabel('Happiness Score', fontsize=12)
plt.tight_layout()
plt.savefig('economy_vs_happiness_scatter.png', dpi=300)
plt.close()

print("Plots generated successfully: correlation_barchart.png, happiness_distribution_histogram.png, economy_vs_happiness_scatter.png")

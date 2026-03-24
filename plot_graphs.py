import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df_ghi = pd.read_csv('GHI_Report.csv')

# Set aesthetic style
sns.set_theme(style="whitegrid")

# a. Bar chart for correlations
cols = ['Economy', 'Fam', 'Health', 'Freedom', 'H_Score']
corr = df_ghi[cols].corr()['H_Score'].drop('H_Score')

plt.figure(figsize=(8, 5))
sns.barplot(x=corr.index, y=corr.values, palette='viridis')
plt.title('Correlation with H_Score', fontsize=14)
plt.ylabel('Correlation Coefficient', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('correlation_barchart.png', dpi=300)
plt.close()

# b. Histogram for H_Score distribution
plt.figure(figsize=(8, 5))
sns.histplot(df_ghi['H_Score'], bins=15, kde=True, color='skyblue')
plt.title('Distribution of Happiness Scores (H_Score)', fontsize=14)
plt.xlabel('H_Score', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.savefig('happiness_distribution_histogram.png', dpi=300)
plt.close()

# c. Scatter plot: Economy vs H_Score
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_ghi, x='Economy', y='H_Score', color='coral', s=100, alpha=0.7)
sns.regplot(data=df_ghi, x='Economy', y='H_Score', scatter=False, color='darkred')
plt.title('Economy vs H_Score', fontsize=14)
plt.xlabel('Economy', fontsize=12)
plt.ylabel('H_Score', fontsize=12)
plt.tight_layout()
plt.savefig('economy_vs_happiness_scatter.png', dpi=300)
plt.close()

print("Plots generated successfully with the new dataset: correlation_barchart.png, happiness_distribution_histogram.png, economy_vs_happiness_scatter.png")

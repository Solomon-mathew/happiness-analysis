import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df_ghi = pd.read_csv('GHI_Report.csv')

# Check data
print(df_ghi.head())

# Select columns
cols = ['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Happiness Score']

# Correlation
corr = df_ghi[cols].corr()['Happiness Score'].drop('Happiness Score')

# Plot
plt.figure(figsize=(8,5))
corr.plot(kind='bar', color='green')
plt.title('Factors Affecting Happiness Score')
plt.ylabel('Correlation')

# Save image (important for your assignment)
plt.savefig('correlation_chart.png')

plt.show()
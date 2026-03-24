import pandas as pd
import numpy as np

# Generate 150 countries
np.random.seed(42)
n = 150
countries = [f"Country_{i}" for i in range(1, n+1)]
economy = np.random.uniform(0.1, 1.7, n)
family = np.random.uniform(0.2, 1.4, n)
health = np.random.uniform(0.1, 1.0, n)
freedom = np.random.uniform(0.1, 0.7, n)

# Happiness is positively correlated with the above factors
happiness = 2.0 + 1.2*economy + 1.0*family + 0.8*health + 0.5*freedom + np.random.normal(0, 0.5, n)
happiness = np.clip(happiness, 2.5, 8.0)

df = pd.DataFrame({
    'Country': countries,
    'Economy (GDP per Capita)': economy,
    'Family': family,
    'Health (Life Expectancy)': health,
    'Freedom': freedom,
    'Happiness Score': happiness
})

df.to_csv('GHI_Report.csv', index=False)
print("Synthetic GHI_Report.csv created successfully.")

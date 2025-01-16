import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

uploaded = files.upload()
file_name = list(uploaded.keys())[0]


df = pd.read_excel(file_name, sheet_name='Sheet1')


df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Plot 1: TFLOPs/Watt over time for AMD and NVIDIA
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Year', y='TFLOPs/Watt', hue='Manufacturer', marker='o')
plt.title('GPU Performance (TFLOPs/Watt) Over Time by Manufacturer')
plt.xlabel('Year')
plt.ylabel('TFLOPs/Watt')
plt.legend(title='Manufacturer')
plt.grid(True)
plt.show()

# Plot 2: TFLOPs/Watt over time by class
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Year', y='TFLOPs/Watt', hue='Class', marker='o')
plt.title('GPU Performance (TFLOPs/Watt) Over Time by Class')
plt.xlabel('Year')
plt.ylabel('TFLOPs/Watt')
plt.legend(title='Class', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# GFLOPs over time by manufacturer
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Year', y='GFLOPS', hue='Manufacturer', marker='o')
plt.title('GPU Raw Computational Power (GFLOPS) Over Time by Manufacturer')
plt.xlabel('Year')
plt.ylabel('GFLOPS')
plt.legend(title='Manufacturer')
plt.grid(True)
plt.show()

# Transistor density (Transistors/Die Size) over time
df['Transistor Density'] = df['Transistors (million)'] / df['Die size']
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Year', y='Transistor Density', hue='Manufacturer', marker='o')
plt.title('Transistor Density Over Time by Manufacturer')
plt.xlabel('Year')
plt.ylabel('Transistors per mm²')
plt.legend(title='Manufacturer')
plt.grid(True)
plt.show()

# TDP over time by class
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Year', y='TDP', hue='Class', marker='o')
plt.title('Thermal Design Power (TDP) Over Time by Class')
plt.xlabel('Year')
plt.ylabel('TDP (Watts)')
plt.legend(title='Class', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

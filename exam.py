import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')

plt.figure(figsize=(10, 6), dpi=100)

plt.subplot(2, 1, 1)

species_counts = df['Species'].value_counts()
plt.pie(species_counts.values, labels=species_counts.index, autopct='%1.1f%%', startangle=120)
plt.title('Доля разных видов ирисов')

plt.subplot(2, 1, 2)

petal_length = df['PetalLengthCm']
cat1 = (petal_length < 1.2).sum()
cat2 = ((petal_length > 1.2) & (petal_length <= 1.5)).sum()
cat3 = (petal_length > 1.5).sum()

cat = ['меньше 1.2 см', '1.2-1.5 см', 'больше 1.5 см']
counts = [cat1, cat2, cat3]

plt.pie(counts, labels=cat, autopct='%1.1f%%', startangle=90)
plt.title('Доли ирисов по их длине')

plt.tight_layout()
plt.show()


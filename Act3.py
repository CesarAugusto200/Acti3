import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


archivo_csv = r'C:\Users\aguil\OneDrive\Escritorio\Actividad 3\IQ Child vs Mother_exported.csv'
df = pd.read_csv(archivo_csv)


print(df.columns)


columna_cuantitativa = df['kid_score']
columna_cualitativa = df['mom_hs']


media = np.mean(columna_cuantitativa)
varianza = np.var(columna_cuantitativa)
desviacion_estandar = np.std(columna_cuantitativa)

frecuencias_cuantitativas = columna_cuantitativa.value_counts().sort_index()


frecuencias_cualitativas = columna_cualitativa.value_counts()


plt.figure(figsize=(15, 5))

# Histograma
plt.subplot(1, 2, 1)
plt.hist(columna_cuantitativa, bins=10, color='skyblue', edgecolor='black')
plt.title('Histograma de Datos Cuantitativos')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')


plt.subplot(1, 2, 2)
freq, bins, _ = plt.hist(columna_cuantitativa, bins=10, color='lightgreen', edgecolor='black', alpha=0)
bin_centers = np.mean(np.vstack([bins[1:], bins[:-1]]), axis=0)
plt.plot(bin_centers, freq, marker='o', linestyle='-')
plt.title('Polígono de Frecuencia')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.axhline(freq.max(), color='red', linestyle='dashed', linewidth=1)
plt.text(bin_centers[len(bin_centers)//2], freq.max() + 0.5, f'Media: {media:.2f}', color='red')

plt.tight_layout()
plt.show()


plt.figure(figsize=(7, 5))


frecuencias_cualitativas.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Diagrama de Barras de Datos Cualitativos')
plt.xlabel('Categoría')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()


print(f'Media: {media:.2f}')
print(f'Varianza: {varianza:.2f}')
print(f'Desviación Estándar: {desviacion_estandar:.2f}')
print(f'Tabla de frecuencias cuantitativas:\n{frecuencias_cuantitativas}')
print(f'Tabla de frecuencias cualitativas:\n{frecuencias_cualitativas}')

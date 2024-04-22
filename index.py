import pandas as pd
from controllers import calculation_hour 
from data import files
import matplotlib.pyplot as plt
import numpy as np

description = "" 
solutions = []
energy = []
hour = []
price = []

for file_name in files:
    solution = calculation_hour(file_name, True)
    solutions.append(solution)

for idx, sol in enumerate(solutions):
    energy.append(sol[0])
    hour.append(idx + 1)
    price.append(sol[1])

daily = {'hour': hour, 'price': price}
df = pd.DataFrame(data=daily)

pb_mean = df['price'].mean()
pb_std = df['price'].std()
pb_var = df['price'].var()
pb_max = df['price'].max()
pb_min = df['price'].min()

line_mean = np.arange(len(hour))
line_mean.fill(pb_mean)

line_max = np.arange(len(hour))
line_max.fill(pb_max)

line_min = np.arange(len(hour))
line_min.fill(pb_min)

line_std_upper = np.arange(len(hour))
line_std_upper.fill(pb_mean + pb_std)

line_std_lower = np.arange(len(hour))
line_std_lower.fill(pb_mean - pb_std)

plt.plot(hour, price, color='red', label=f'Precio de bolsa por hora')
plt.plot(hour, line_mean, '--', color='dimgray', alpha=0.3, label=f'Promedio del precio de bolsa:  {pb_mean}')
plt.plot(hour, line_std_upper, 'o', color='gray', alpha=0.3, label=f'Desviación estandar superior del precio bolsa promedio: {pb_mean + pb_std}')
plt.plot(hour, line_std_lower, 'o', color='silver', alpha=0.3, label=f'Desviación estandar inferior del precio bolsa promedio: {pb_mean - pb_std}')
plt.plot(hour, line_max, '-', color='lightgray', alpha=0.3, label=f'Máximo del precio de bolsa: {pb_max}')
plt.plot(hour, line_min, '-', color='darkgray', alpha=0.3, label=f'Mínimo del precio de bolsa: {pb_min}')


plt.legend(title="Descripción")
plt.title(f'Precio de bolsa diario')
plt.show()


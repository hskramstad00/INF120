import pandas as pd

# Oppgaven skal lese inn data fra en tekstfil med Pandas og bruke Matplotlib til å plotte
# disse dataene. Dataen inneholder daglig tempratur fra 2012 i Ås

# Del 1
# Bruke Pandas read_csv til å lese inn dataen til en Pandas DataFrame

df = pd.read_csv('data/meteodata_aas_2012.csv', sep=';', header=1)

print('PART 1:')
print(f'{df} \n')

# Del 2
# Plotte tempraturdata med bare kolonen T_avg og konvertere til numpy array

import matplotlib.pyplot as plt

# selecting average temprature
temp_avg = df['T_avg']

print('PART 2:')

temp_avg_numpy = temp_avg.to_numpy()
plt.plot(temp_avg_numpy, label='Daily average meassurement')
plt.legend(loc='upper right')
plt.ylabel('Temp [deg C]')
plt.xlabel('day of year')
plt.title('Temprature readings for 2012')
plt.show()
print('see own plot \n')

# Part 3
# Lag en funksjon som beregner tempratur gjennom året med gitt formel
# Plot funksjonen sammen med målte tempraturer
print('PART 3:')
import numpy as np

def year_temp(days,T_avg=10, A=20, offset=0):
    omega = 2 * np.pi / 365

    return T_avg + A * np.sin(omega * (days + offset))

one_year = np.arange(1,366)

fig, ax = plt.subplots()
ax.plot(year_temp(one_year), label='T0 + A * sin(omega * (day + offset))', color='orange')
ax.plot(temp_avg_numpy, label='Daily average meassurement', color='blue')
ax.legend(loc='upper right')
ax.set_xlabel('day of year')
ax.set_ylabel('Temp [deg C]')
ax.set_title('Temperature reading for 2012')

plt.show()
print('see own plot \n')

# Part 4
# Ved å endre på  Tavg og offset og plotte igjen kan du få kurvene til å sammenfalle ganske bra med faktis T_avg
# Hva er estimert årsgjennomsnitt T_avg for 2012?
# Hva er estimert amplitude for temretursvingningen?

print('Part 4:')
print('see own plot')

print(f'{temp_avg.mean():.2f}')
# I see from this print stament that approximatley 5.91 celcius is mean for 2012
# Also see form plot that A is approcaimatley 20
fig, ax = plt.subplots()
ax.plot(year_temp(one_year, T_avg=5.91,A=10,offset=-109), label='T0 + A * sin(omega * (day + offset))', color='orange')
ax.plot(temp_avg_numpy, label='Daily average meassurement', color='blue')
ax.legend(loc='lower center')
ax.set_xlabel('day of year')
ax.set_ylabel('Temp [deg C]')
ax.set_title('Temperature reading for 2012')

plt.show()

print('Estimated average for 2012 is 5.91 degrees celcius \n' \
'and estimated amplitude is 10')
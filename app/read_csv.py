# Leer un CSV

# https://www.w3schools.com/python/python_file_open.asp
# https://www.kaggle.com/
# https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset

import csv
'''
def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    # Convertir lista de registro a diccionario
    header = next(reader)
    print(header)
    for row in reader:
      print("***" * 5)
      print(row)
'''
# Convertir lista de registro a diccionario

def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    # Convertir lista de registro a diccionario
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      #print(list(iterable))
      # Generar diccionario
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/world_population.csv')
  print(data[0])


# Playground: Lee un CSV para calcular el total de gastos
'''
Para resolver este desafío, debes utilizar el archivo data.csv que contiene los datos de los gastos de una empresa. El archivo tiene dos columnas: el nombre del área y el total de gastos del año.

Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa. Para leer el archivo CSV, puedes utilizar la función open y el módulo csv de Python. Una vez que hayas leído los datos, puedes calcular el total de gastos implementando la lógica que consideres necesaria.

Ejemplo

Input: data.csv
Administration,10
Marketing,20
Purchasing,10
Human Resources,20

Output:
60

#import csv

def read_csv(path):
   # Tu código aquí 👇
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    total = 0
    for row in reader:
      total += int(row[1])
    return total

response = read_csv('./app/data.csv')
print(response)
'''
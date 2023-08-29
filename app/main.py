# Importamos el modulo
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('world_population.csv')

  # Reto: graficando la población mundial
  data = list(filter(lambda item: item["Continent"] == "South America", data))
  countries = list(map(lambda x: x["Country/Territory"], data))  
  percentages = list(map(lambda x: x["World Population Percentage"], data))

  # Reto: graficando la población de un país
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country["Country/Territory"], labels, values)
    charts.generate_pie_chart(country["Country/Territory"], countries, percentages)
  
# Módulos como scripts: __name__ y __main__
# Entry point
'''
Este if le dice al main.py, que si el archivo es ejecutado desde la terminal, ejecute el metodo run, pero si es ejecutado desde otro archivo, el metodo run no se ejecutaria.
'''

if __name__ == '__main__':
  run()
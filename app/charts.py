# Creando una gráfica

# https://platzi.com/blog/matplotlib/
# https://platzi.com/cursos/matplotlib-seaborn/
# https://matplotlib.org/
# https://www.w3schools.com/python/matplotlib_pyplot.asp

#pip install matplotlib
import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  #plt.show()
  plt.savefig(f'./imgs/{name}_bar.png')
  plt.close()

def generate_pie_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis("equal")
  #plt.show()
  plt.savefig(f'./imgs/{name}_pie.png')
  plt.close()

if __name__ == "__main__":
  labels = ["a", "b", "c"]
  values = [70, 150, 120]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)

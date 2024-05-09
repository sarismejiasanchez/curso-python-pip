import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # Obtener el estado
    print(r.status_code)
    # Obtener la respuesta
    print(r.text)
    # Obtener el tipo de la respuesta
    print(type(r.text))
    # Obtener respuesta en formato json
    categories = r.json()
    # Obtenemos el atributo name de cada categoria
    for category in categories:
        print(category['name'])
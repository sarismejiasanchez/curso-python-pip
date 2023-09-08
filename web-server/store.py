import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # Obtener el Estado
    print(r.status_code)
    # Obtener la respuesta
    print(r.text)
    print(type(r.text))
    
    # Obtener respuesta en json (iterable)
    categories = r.json() # Lista
    
    for category in categories:
        print(category['name'])
    
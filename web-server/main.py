import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Creamos una instancia de la aplicacion
app = FastAPI()

# Creamos un decorador, con la ruta desde la cual se accederá desde la web
@app.get('/')
# Creamos un recurso
def get_list():
    return [1, 2, 3]

@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

def run():
    store.get_categories()

# Correr como script
if __name__ == '__main__':
    run()
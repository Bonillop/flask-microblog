from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    """
        El decorador @app.shell_context_processor toma una funcion y permite retornar un diccionario que maneja los
        imports cuando se ejecuta el comando flask shell, para no tener que importarlos a mano en una sesion del
        interprete de python
    """
    return {"db":db, "User":User, "Post":Post}

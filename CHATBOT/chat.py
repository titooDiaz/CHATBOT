import os
from bardapi import Bard

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')

# Comprueba si el archivo .env existe
if os.path.isfile(dotenv_path):
    # Carga las variables de entorno desde el archivo .env
    with open(dotenv_path) as f:
        for line in f:
            key, value = line.strip().split('=')
            os.environ[key] = value

# Accede a la variable de entorno "KEY"
KEY = os.getenv("KEY")#recuerda tener un archivo lalmada .env en la carpeta raiz, con la variable y tu KEY de la API

os.environ["_BARD_API_KEY"] = KEY
message = input("¿Qué deseas preguntar? ")
print(Bard().get_answer(str(message))['content'])

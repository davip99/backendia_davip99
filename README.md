# backendia_davip99

# Requisitos

Python 3.13

Se recomienda el uso de aplicaciones como Postman para realizar pruebas sobre la API.

# Implementación
Una vez tengamos los requisitos marcados en la parte superior, podemos implementar la api con los siguientes pasos:

1. Descargar el código fuente desde este repositorio.

2. Acceder desde una terminal al directorio donde se encuentra el código.

3. Ejecutar el siguiente comando: `python -m venv venv`

4. Ejecutar el siguiente comando: `.\venv\Scripts\activate`

5. Ejecutar el siguiente comando: `pip install -r requirements.txt`

6. Crear en el directorio raíz del proyecto el archivo '.env', existe un archivo de ejemplo denominado '.env.example'.

7. Crear dentro del archivo '.env' las siguientes variables:
```env

API_TOKEN=mi_token_secreto

```
8. Ejecutar el comando: `uvicorn main:app --reload `

9. Escribir un prompt usando el siguiente comando: `curl -X 'POST' \'http://localhost:8000/generate' \-H 'accept: application/json' \ -H 'token: mi_token_secreto' \ -H 'Content-Type: application/x-www-form-urlencoded' \ -d 'prompt=once%20upon%20a%20time&max_length=128&temperature=0.6&top_p=1'`

[Documentacion de la API](https://documenter.getpostman.com/view/41258294/2sAYQiAnFS)

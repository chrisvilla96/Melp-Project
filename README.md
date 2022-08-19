# MELP - Project

MELP es un API para acceder a información de restaurantes cerca de tu zona.

Está hecho con Python y Django Restframework

## Instalación

Para poder correr el repositorio es necesario contar con Python 3 y PIP instalado dentro de tu ordenador.


Al descargar este repositorio se recomienda crear un entorno de desarrollo con virtualenv. 
Si no se tiene instalado virtualenv se puede instalar con el siguiente comando.

```bash
pip3 install virtualenv
```

Ya con esto se procede a crear el entorno con el siguiente comando.

```bash
python3 -m venv .
```
Se activa el entorno con el siguiente comando


```bash
source venv/bin/activate
```

Con el entorno activado se procede a instalar las dependencias dentro del requirements.txt

```bash
(venv) $ pip3 install -r requirements.txt
```

Para poder correr el sistema, se usa el siguiente comando


```bash
(venv) $ pyhton3 ./manage.py runserver
```


## Uso

Para poder hacer uso del API, se tienen 3 endpoints

GET y POST - [http://127.0.0.1:8000/api/restaurants/](http://127.0.0.1:8000/api/restaurants/)

PUT y DELETE - [http://127.0.0.1:8000/api/restaurants/<uuid: pk>](http://127.0.0.1:8000/api/restaurants/)

Statistics - http://127.0.0.1:8000/api/restaurants/statistics?latitude=<latitude>&longitude=<longitud>&radious=<radio>

Ejemplo - [http://127.0.0.1:8000/api/restaurants/statistics?latitude=19.440226&longitude=-99.128489&radious=500](http://127.0.0.1:8000/api/restaurants/statistics?latitude=19.440226&longitude=-99.128489&radious=500)

# pokeapi

## Descripción

La Poke-Berries API es una aplicación web desarrollada en Django que proporciona estadísticas sobre las bayas (berries) en el universo Pokémon. Esta API consume datos de la API oficial de Pokémon para obtener información sobre las bayas y sus tiempos de crecimiento. Los usuarios pueden acceder a las estadísticas generales de las bayas, incluyendo el tiempo mínimo, mediano y máximo de crecimiento, la varianza y la media de los tiempos de crecimiento, así como la frecuencia de cada tiempo de crecimiento. Además, la API genera un histograma que muestra la distribución de los tiempos de crecimiento de las bayas.

## Características

- Proporciona estadísticas sobre las bayas en el universo Pokémon
- Consumo de la API oficial de Pokémon para obtener datos sobre las bayas
- Estadísticas generales como tiempo mínimo, mediano y máximo de crecimiento
- Varianza y media de los tiempos de crecimiento
- Frecuencia de cada tiempo de crecimiento
- Generación de un histograma que muestra la distribución de los tiempos de crecimiento

## Tecnologías Utilizadas

- Python
- Django
- Requests
- Plotly

## Requisitos

- Python 3.x
- Django 3.x
- Requests
- Plotly

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/MigueAmaterasu/pokeapi.git
```

2. Accede al directorio del proyecto:

```bash
cd pokeapi
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno:
    Crea un archivo .env en el directorio raíz del proyecto y define las siguientes variables:

```plaintext
POKEMON_API_URL=https://pokeapi.co/api/v2/
```

5. Ejecuta las migraciones:

```bash
python manage.py migrate
```

6. Inicia el servidor:

```bash
python manage.py runserver
```

7. Accede a la API en tu navegador:

http://127.0.0.1:8000/berry-stats/



## Uso

Para acceder a las estadísticas de las bayas, simplemente haz una solicitud GET a la siguiente URL:

http://127.0.0.1:8000/allBerryStats

## Contribución

Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
Realiza tus cambios y haz commit (git commit -am 'Agrega una nueva característica').
Haz push a la rama (git push origin feature/nueva-caracteristica).
Crea un nuevo pull request.

## Créditos

Este proyecto fue desarrollado por Miguel de Jesus Sanchez 

## Licencia

Este proyecto está bajo la Licencia MIT.
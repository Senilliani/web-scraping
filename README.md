# Scraping de Nombres de Máquinas

Este script de Python extrae nombres de máquinas desde una página web.
Además, verifica si una determinada máquina, en este caso noob-1, está en la vista principal, si no está, considera que ha pasado a la siguiente página y que se ha agregado una o más nuevas máquinas. Según sea el caso, muestra un mensaje u otro.

## Requisitos

- Python 3.x
- Paquetes:
  - `requests`
  - `colorama`

## Instalación

1. Clona el repositorio:

```bash
   git clone https://github.com/Senilliani/web-scraping.git
```

2. Navega al directorio del proyecto

```bash
  cd web-scraping
```

3. Crea y activa un entorno virtual (opcional pero recomendado):

```bash
  python -m venv .venv
  source .venv/bin/activate  # En macOS y Linux
  # .venv\Scripts\activate     # En Windows
```

4. Instala las dependencias:

```bash
  pip install -r requirements.txt
```

## Uso

Ejecuta el script:

```bash
  python script_getTitles.py
```

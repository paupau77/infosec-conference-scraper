# Infosec Conference Scraper

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Automation-green)](https://playwright.dev/python/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

Scraper en **Python** basado en [Playwright](https://playwright.dev/python/) que extrae conferencias de ciberseguridad desde [infosec-conferences.com](https://infosec-conferences.com/) y las guarda en un archivo CSV.

---

## 🚀 Características
- Extrae automáticamente todas las conferencias listadas en la web.
- Guarda los resultados en `infosec_conferences.csv`.
- Incluye los encabezados de la tabla.
- Navega por todas las páginas disponibles.
- Reporta cuántos eventos fueron extraídos en total.

---

## 🛠️ Requisitos
- Python 3.9+
- Playwright
- asyncio

Instalación de dependencias:
pip install playwright
playwright install


---

▶️ Uso

Ejecutar el script:

python AppInfosecConferences.py

El archivo resultante infosec_conferences.csv contendrá los eventos extraídos.


---

📊 Ejemplo de salida

Event Name	Date	Location	...

DEFCON	Aug 2025	Las Vegas, USA	...



---

📜 Licencia

Mi proyecto está bajo la licencia MIT.

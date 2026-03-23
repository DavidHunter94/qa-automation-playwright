# Proyecto de Automatización QA – Urban Routes

## 📌 Descripción

Proyecto de automatización de pruebas UI para una aplicación web de solicitud de taxis.

Este proyecto valida los flujos críticos de usuario, incluyendo selección de ruta, elección de tarifa, verificación de teléfono, método de pago, servicios adicionales y flujo completo de pedido.

La implementación sigue el patrón **Page Object Model (POM)** y utiliza **Playwright con pytest** para la ejecución de pruebas.

---

## 🧠 Objetivo

Demostrar habilidades en:

* Automatización de pruebas UI
* Diseño de pruebas estructuradas (POM)
* Validación de flujos end-to-end
* Comparación entre Selenium y Playwright

---

## ⚙️ Tecnologías utilizadas

* **Lenguaje:** Python
* **Framework de pruebas:** pytest
* **Herramienta de automatización:** Playwright
* **Patrón de diseño:** Page Object Model (POM)

---

## 🧪 Cobertura de pruebas

### Pruebas funcionales

* Validación de origen y destino
* Selección de tarifa (Comfort)
* Verificación de número telefónico (integración con API)
* Registro de tarjeta de crédito
* Ingreso de mensaje al conductor

### Servicios adicionales

* Activación de “Manta y pañuelos”
* Selección de cantidad de helados

### Prueba end-to-end (E2E)

* Flujo completo de solicitud de taxi
* Validación de aparición del modal de búsqueda de conductor

---

## 🏗️ Estructura del proyecto

```text id="l0x7yt"
project/
│
├── pages/
│   └── urban_routes_page.py
│
├── tests/
│   └── test_urban_routes.py
│
├── data.py
├── requirements.txt
└── README.md
```

---

## ▶️ Ejecución de pruebas

Instalar dependencias:

```text id="9uxv0c"
pip install -r requirements.txt
```

Ejecutar pruebas:

```text id="l6p2eq"
py -m pytest -v --headed
```

---

## 🔍 Detalles de implementación

* Uso de **auto-waiting de Playwright** para mejorar la estabilidad
* Captura del código de verificación mediante respuesta del backend
* Reutilización de flujo base con el método `complete_basic_flow()`
* Separación de responsabilidades mediante Page Object Model

---

## ⚖️ Comparación: Selenium vs Playwright

Este proyecto también fue implementado con Selenium para comparar enfoques.

**Diferencias observadas:**

| Selenium                               | Playwright                     |
| -------------------------------------- | ------------------------------ |
| Requiere esperas explícitas            | Manejo automático de esperas   |
| Mayor cantidad de código               | Código más limpio y legible    |
| Mayor probabilidad de tests inestables | Mayor estabilidad en ejecución |

👉 Playwright ofrece mejor mantenibilidad y confiabilidad en aplicaciones web modernas.

---

## 🚀 Autor David Martinez Matias

QA Engineer en transición con experiencia en:

* Pruebas manuales
* Automatización UI
* Pruebas de API

Enfocado en desarrollar soluciones de testing confiables y escalables.
# Urban Routes – Automatización QA con Playwright

Proyecto de automatización de pruebas UI para la aplicación web **Urban Routes**, desarrollado como parte del Sprint 8 del Bootcamp de QA de TripleTen.

Valida que en un flujo completo el usuario pueda solicitar un taxi, registrar su teléfono, agregar método de pago y solicitar extras — todo sin errores.

![CI](https://github.com/DavidHunter94/qa-automation-playwright/actions/workflows/tests.yml/badge.svg)

---

## 🧪 Cobertura de pruebas

### Pruebas funcionales
- Validación de origen y destino
- Selección de tarifa (Comfort)
- Verificación de número telefónico (integración con API)
- Registro de tarjeta de crédito
- Ingreso de mensaje al conductor

### Servicios adicionales
- Activación de "Manta y pañuelos"
- Selección de cantidad de helados

### Prueba end-to-end (E2E)
- Flujo completo de solicitud de taxi
- Validación de aparición del modal de búsqueda de conductor

---

## ⚙️ Tecnologías utilizadas

- **Lenguaje:** Python 3.11
- **Framework de pruebas:** pytest
- **Automatización:** Playwright
- **Patrón de diseño:** Page Object Model (POM)
- **CI/CD:** GitHub Actions

---

## 🏗️ Estructura del proyecto

```
project/
│
├── .github/
│   └── workflows/
│       └── tests.yml       ← Pipeline de CI/CD
│
├── pages/
│   └── urban_routes_page.py
│
├── tests/
│   └── test_urban_routes.py
│
├── conftest.py
├── data.py
├── requirements.txt
└── README.md
```

---

## ▶️ Instalación y ejecución local

```bash
# 1. Clonar el repositorio
git clone https://github.com/DavidHunter94/qa-automation-playwright.git
cd qa-automation-playwright

# 2. Crear entorno virtual e instalar dependencias
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt

# 3. Instalar navegadores de Playwright
playwright install chromium

# 4. Ejecutar los tests
pytest -v tests/
```

> ⚠️ Los tests requieren que el servidor de Urban Routes esté activo.
> La URL se configura en `data.py`. Esta URL es temporal del entorno de TripleTen.

---

## 🤖 CI/CD con GitHub Actions

El proyecto incluye un pipeline automático que se activa en cada `push` a `main`.

**Pasos del pipeline:**
1. Instala Python 3.11
2. Instala dependencias del proyecto
3. Instala Playwright y Chromium
4. Ejecuta los 9 tests en modo headless
5. Genera y sube un reporte HTML como artefacto descargable

Para ver los resultados: pestaña **Actions** en el repositorio de GitHub.

---

## ⚖️ Comparación: Selenium vs Playwright

Este proyecto también fue implementado con Selenium para comparar enfoques.

| | Selenium | Playwright |
|---|---|---|
| Esperas | Manuales (explicit waits) | Automáticas (auto-waiting) |
| Cantidad de código | Mayor | Más limpio y conciso |
| Estabilidad | Más flaky | Mayor estabilidad |
| Soporte CI/CD | Requiere más config | Nativo con headless |

Playwright ofrece mejor mantenibilidad y confiabilidad en aplicaciones web modernas.

---

## 🚀 Autor

**Victor David Martínez Matías**
QA Engineer con experiencia en pruebas manuales, automatización UI y pruebas de API.
Enfocado en desarrollar soluciones de testing confiables y escalables.
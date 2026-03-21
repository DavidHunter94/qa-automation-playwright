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

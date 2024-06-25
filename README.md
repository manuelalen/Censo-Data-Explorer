# Censo Data Explorer

Bienvenido al repositorio de la aplicación Censo Data Explorer, una herramienta interactiva para explorar y analizar datos de empresarios (ficticios) almacenados en Excel. Esta aplicación está diseñada para proporcionar insights detallados y permitir una exploración dinámica de los datos.

## 🌐 Aplicación en Vivo

Puedes acceder a la aplicación, se puede hacer uso del siguiente enlace: [Censo Data Explorer](https://censo-data-explorer-n5n8q7cyssrfsivugmpdij.streamlit.app/)

## 📊 Origen de los Datos

El origen de los datos es un archivo Excel que contiene información detallada sobre empresarios. Aquí se detallan los campos disponibles en el archivo:

- `cod_empresario`: Código identificador del empresario.
- `nif_empresa`: Número de identificación fiscal de la empresa.
- `nombre_empresa`: Nombre de la empresa.
- `puntos`: Puntos acumulados por incumplimientos.
- `motivo`: Razón por la cual se retiran los puntos.
- `fecha`: Fecha en la que se registraron los puntos.

Estos datos han sido obtenidos de manera random con `ChatGPT`, a la que se le ha especificado un prompt y una codificación determinada para el `cod_empresario` y el `nif_empresa`. También se le ha pasado un listado de motivos por los que retirar puntos con su correspondiente valor de puntos a retirar. 

## 🛠️ Funcionalidad de la Aplicación

La aplicación permite a los usuarios:

- **Filtrar Datos**: Utiliza los filtros disponibles en la barra lateral para buscar y filtrar datos por fecha, NIF de empresa, nombre de empresa, motivo y código de empresario.
- **Visualizar Datos**: Observa los datos filtrados en una tabla interactiva que se actualiza basada en tus filtros.
- **Analizar Tendencias**: Examina un gráfico de barras que muestra los puntos restantes por empresario, calculados como `12 - puntos acumulados`.

## 🚀 Cómo Utilizar

1. **Accede a la Aplicación**: Usa la [URL](https://censo-data-explorer-n5n8q7cyssrfsivugmpdij.streamlit.app/) para visitar la aplicación.
2. **Aplica Filtros**: Selecciona las opciones deseadas en los campos de filtrado para refinar los resultados mostrados.
3. **Explora los Resultados**: Visualiza los resultados en la tabla y el gráfico proporcionado para entender mejor la distribución de puntos y el cumplimiento de los empresarios.

## 💻 Desarrollo Local

Si deseas ejecutar la aplicación localmente, sigue estos pasos:

1. Clona este repositorio.
2. Asegúrate de tener Python y pip instalados.
3. Instala las dependencias necesarias con `pip install -r requirements.txt`.
4. Ejecuta la aplicación con `streamlit run app.py`.

## ⚒️ Uso personal

Para mi caso, este dataset creado mediante GPT, se utiliza para mostrar los datos en este streamlit. No obstante, también se ha desarrollado una aplicación en `PowerApps` mediante la cual podremos insertar una determinada sanción de puntos a un empresario asociado a una empresa. Además, desarrollamos un informe en `PowerBI` con el que elaboramos una serie de métricas que deseamos para nuestro caso de uso. El esquema quedaría de la siguiente manera:

!(/images/streamlit.png)

## 📝 Licencia

Este proyecto está bajo la Licencia GNU. Consulta el archivo `LICENSE` en este repositorio para más detalles.

---

Gracias por visitar y utilizar Censo Data Explorer!

# Censo Data Explorer

Bienvenido al repositorio de la aplicación Censo Data Explorer, una herramienta interactiva para explorar y analizar datos de empresarios almacenados en un archivo Excel. Esta aplicación está diseñada para proporcionar insights detallados y permitir una exploración dinámica de los datos.

## 🌐 Aplicación en Vivo

Puedes acceder a la aplicación en vivo a través de la siguiente URL: [Censo Data Explorer](https://censo-data-explorer-n5n8q7cyssrfsivugmpdij.streamlit.app/)

## 📊 Origen de los Datos

El origen de los datos es un archivo Excel que contiene información detallada sobre empresarios. Este archivo es esencial para la operación de la aplicación, ya que contiene todos los datos que se visualizan y analizan. Aquí se detallan los campos disponibles en el archivo:

- `cod_empresario`: Código identificador del empresario.
- `nif_empresa`: Número de identificación fiscal de la empresa.
- `nombre_empresa`: Nombre de la empresa.
- `puntos`: Puntos acumulados por incumplimientos o méritos.
- `motivo`: Razón por la cual se asignaron los puntos.
- `fecha`: Fecha en la que se registraron los puntos.

## 🛠️ Funcionalidad de la Aplicación

La aplicación permite a los usuarios:

- **Filtrar Datos**: Utiliza los filtros disponibles en la barra lateral para buscar y filtrar datos por fecha, NIF de empresa, nombre de empresa, motivo y código de empresario.
- **Visualizar Datos**: Observa los datos filtrados en una tabla interactiva que se actualiza basada en tus filtros.
- **Analizar Tendencias**: Examina un gráfico de barras que muestra los puntos restantes por empresario, calculados como `12 - puntos acumulados`.

## 🚀 Cómo Utilizar

1. **Accede a la Aplicación**: Usa la [URL proporcionada](https://censo-data-explorer-n5n8q7cyssrfsivugmpdij.streamlit.app/) para visitar la aplicación.
2. **Aplica Filtros**: Selecciona las opciones deseadas en los campos de filtrado para refinar los resultados mostrados.
3. **Explora los Resultados**: Visualiza los resultados en la tabla y el gráfico proporcionado para entender mejor la distribución de puntos y el cumplimiento de los empresarios.

## 💻 Desarrollo Local

Si deseas ejecutar la aplicación localmente, sigue estos pasos:

1. Clona este repositorio.
2. Asegúrate de tener Python y pip instalados.
3. Instala las dependencias necesarias con `pip install -r requirements.txt`.
4. Ejecuta la aplicación con `streamlit run app.py`.

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` en este repositorio para más detalles.

---

Gracias por visitar y utilizar Censo Data Explorer!

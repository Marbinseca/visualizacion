# Visualizador de Datos Interactivo con Streamlit

Una aplicación web simple construida con Streamlit que permite a los usuarios cargar archivos de Excel, seleccionar datos y visualizarlos a través de varios tipos de gráficos interactivos como barras, pastel, líneas y dispersión.

## 🎮 Demo

🌐 [Ver Demo en Vivo](https://visualizacion-wosh6quvzdes4ilcip88ka.streamlit.app/)

![Demo de la Aplicación](demo.gif)

---

## 🚀 Características Principales

- **Carga de Archivos**: Soporta la carga de archivos de Excel (`.xlsx`, `.xls`).
- **Selección de Hoja**: Permite elegir qué hoja de cálculo visualizar del archivo cargado.
- **Vista de Tabla**: Muestra los datos crudos en una tabla interactiva.
- **Generación de Gráficos**: Crea 4 tipos de gráficos diferentes:
  - Gráfico de Barras
  - Gráfico de Pastel
  - Gráfico de Líneas
  - Gráfico de Dispersión
- **Personalización Interactiva**: Ofrece una amplia gama de opciones en la barra lateral para personalizar los gráficos:
  - Selección de columnas para los ejes X e Y.
  - Agrupación de datos por color.
  - Títulos personalizables para el gráfico y los ejes.
  - Opciones de ordenamiento para gráficos de barras (ascendente, descendente, cronológico).
  - Ajuste dinámico del tamaño del gráfico (ancho y alto).
  - Paletas de colores y estilos de fuente.
- **Manejo de Errores**: Proporciona retroalimentación útil si ocurre un error al cargar un archivo o generar un gráfico.
- **Datos por Defecto**: Carga un conjunto de datos de ejemplo si no se proporciona ningún archivo, permitiendo probar la funcionalidad inmediatamente.

---

## 🛠️ Instalación y Puesta en Marcha

Para ejecutar esta aplicación en tu máquina local, sigue estos pasos:

### Prerrequisitos

- Python 3.8 o superior.

### Pasos

1.  **Clona o descarga el repositorio**
    Si tienes Git, puedes clonar el repositorio. De lo contrario, simplemente descarga los archivos `app.py` y `requirements.txt`.

2.  **Crea un entorno virtual (Recomendado)**
    Es una buena práctica aislar las dependencias del proyecto.
    ```bash
    python -m venv venv
    ```

3.  **Activa el entorno virtual**
    - **En Windows:**
      ```bash
      .\venv\Scripts\activate
      ```
    - **En macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```

4.  **Instala las dependencias**
    Crea un archivo `requirements.txt` con el siguiente contenido y luego ejecuta el comando `pip install`.

    **`requirements.txt`**:
    ```
    streamlit
    pandas
    plotly
    numpy
    openpyxl
    ```

    **Comando de instalación**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Ejecuta la aplicación Streamlit**
    Una vez instaladas las dependencias, ejecuta el siguiente comando en tu terminal:
    ```bash
    streamlit run app.py
    ```
    Tu navegador se abrirá automáticamente en `http://localhost:8501` con la aplicación en funcionamiento.

---

## 📖 Cómo Usar la Aplicación

1.  **Cargar Datos**: Usa la barra lateral para subir tu propio archivo de Excel. Si no subes ninguno, la aplicación usará un conjunto de datos de ejemplo.
2.  **Seleccionar Hoja**: Si tu Excel tiene múltiples hojas, podrás seleccionar cuál usar.
3.  **Elegir un Gráfico**: En la sección "Navegación", selecciona "Gráficos".
4.  **Personalizar**: Usa las "Opciones de Gráfico" en la barra lateral para seleccionar el tipo de gráfico, las columnas para los ejes, los colores, los títulos y más.
5.  **Explorar**: Interactúa con el gráfico generado. ¡Los gráficos de Plotly te permiten hacer zoom, moverte y ver detalles al pasar el cursor!



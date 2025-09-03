import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Visualizador de Datos", page_icon="📈", layout="wide")

# ---
# Sección de carga de archivo
# ---
st.sidebar.header("Cargar Datos")
uploaded_file = st.sidebar.file_uploader("Elige un archivo de Excel (.xlsx)", type=["xlsx", "xls"])

original_df = pd.DataFrame() # DataFrame original

# Manejo del archivo cargado
if uploaded_file:
    try:
        xls = pd.ExcelFile(uploaded_file)
        sheet_names = xls.sheet_names
        
        st.sidebar.subheader("Opciones de Hoja")
        selected_sheet = st.sidebar.selectbox("Selecciona una hoja:", sheet_names)
        
        original_df = pd.read_excel(xls, sheet_name=selected_sheet)
        st.subheader("Tabla de Datos")
        st.dataframe(original_df, use_container_width=True) # Muestra la tabla sin editar
        
    except Exception as e:
        st.error(f"Ocurrió un error al leer el archivo de Excel: {e}")
        st.info("Asegúrate de que el archivo tenga un formato válido.")

else:
    # Si no hay archivo cargado, muestra la tabla por defecto
    st.subheader("Tabla de Datos (Por defecto)")
    data = {
        'Categoría': ['A', 'B', 'C', 'D'],
        'Valor_1': [15, 20, 35, 10],
        'Valor_2': [25, 15, 10, 30],
        'latitud': [-33.456, -34.567, -35.678, -36.789],
        'longitud': [-70.678, -71.789, -72.890, -73.901]
    }
    original_df = pd.DataFrame(data)
    st.dataframe(original_df, use_container_width=True) # Muestra la tabla por defecto

# ---
# Navegación entre páginas
# ---
st.sidebar.markdown("---")
page = st.sidebar.radio("Navegación", ("Gráficos", ))

# ---
# Página de Gráficos
# ---
if page == "Gráficos":
    st.title("Visualizador de Datos Interactivo")
    st.markdown("Explora tus datos con diferentes tipos de gráficos.")

    # Sección de gráficos en la barra lateral
    st.sidebar.subheader("Opciones de Gráfico")

    if not original_df.empty:
        
        # Selección del tipo de gráfico
        chart_type = st.sidebar.selectbox(
            "Selecciona el tipo de gráfico:",
            ("Barras", "Pastel", "Líneas", "Dispersión")
        )
        
        st.subheader(f"Gráfico de {chart_type}")
        
        # Título principal del gráfico
        chart_title = st.sidebar.text_input("Título del Gráfico:", value=f"Gráfico de {chart_type}")
        
        try:
            # Gráfico de Barras
            if chart_type == "Barras":
                st.sidebar.markdown("---")
                x_column = st.sidebar.selectbox("Eje X:", original_df.columns)
                y_column = st.sidebar.selectbox("Eje Y:", original_df.columns)
                color_column = st.sidebar.selectbox("Color por:", [None] + list(original_df.columns))
                color_palette = st.sidebar.selectbox(
                    "Paleta de colores:",
                    ['Plotly', 'Prism', 'Dark24', 'Pastel']
                )

                # Opción para ordenar
                sort_option = st.sidebar.radio(
                    "Ordenar por:",
                    ("Sin ordenar", "Mayor a menor (Eje Y)", "Cronológico (Eje X)")
                )

                if sort_option == "Mayor a menor (Eje Y)":
                    sorted_df = original_df.sort_values(by=y_column, ascending=False)
                elif sort_option == "Cronológico (Eje X)":
                    try:
                        sorted_df = original_df.sort_values(by=x_column)
                        # Convertimos la columna a tipo datetime para mejor visualización
                        sorted_df[x_column] = pd.to_datetime(sorted_df[x_column])
                    except Exception as e:
                        st.warning("La columna del Eje X no puede ser convertida a formato de fecha. Se mostrará sin ordenar.")
                        sorted_df = original_df.copy()
                else:
                    sorted_df = original_df.copy()

                fig = px.bar(
                    sorted_df, 
                    x=x_column, 
                    y=y_column, 
                    color=color_column,
                    color_discrete_sequence=getattr(px.colors.qualitative, color_palette),
                    text_auto=True # Mostrar valor en las barras
                )
                
                # Ajuste del eje Y para evitar que los datos se salgan
                max_y_value = sorted_df[y_column].max()
                fig.update_yaxes(range=[0, max_y_value * 1.1])

                # Opciones para títulos de ejes
                x_title = st.sidebar.text_input("Título del Eje X:", value=x_column)
                y_title = st.sidebar.text_input("Título del Eje Y:", value=y_column)
                fig.update_layout(title_text=chart_title, xaxis_title=x_title, yaxis_title=y_title)
                
                # Opción para mostrar los nombres del eje X en cursiva
                if st.sidebar.checkbox("Mostrar nombres del Eje X en cursiva"):
                    fig.update_xaxes(tickfont=dict(family="Arial", style="italic"))

                # Opciones para personalizar tamaño del gráfico
                st.sidebar.subheader("Personalizar tamaño del gráfico")
                chart_width = st.sidebar.slider("Ancho del gráfico (px)", 400, 1200, 800)
                chart_height = st.sidebar.slider("Alto del gráfico (px)", 300, 900, 500)
                fig.update_layout(width=chart_width, height=chart_height)

                st.plotly_chart(fig)
                
            # Gráfico de Pastel
            elif chart_type == "Pastel":
                names_column = st.sidebar.selectbox("Nombres (etiquetas):", original_df.columns)
                values_column = st.sidebar.selectbox("Valores:", original_df.columns)
                
                fig = px.pie(original_df, names=names_column, values=values_column)
                fig.update_layout(title_text=chart_title)
                st.plotly_chart(fig, use_container_width=True)

            # Gráfico de Líneas
            elif chart_type == "Líneas":
                x_column = st.sidebar.selectbox("Eje X:", original_df.columns)
                y_column = st.sidebar.selectbox("Eje Y:", original_df.columns)
                
                fig = px.line(original_df, x=x_column, y=y_column)

                # Ajuste del eje Y para evitar que los datos se salgan
                max_y_value = original_df[y_column].max()
                fig.update_yaxes(range=[0, max_y_value * 1.1])
                
                # Opciones para títulos de ejes
                x_title = st.sidebar.text_input("Título del Eje X:", value=x_column)
                y_title = st.sidebar.text_input("Título del Eje Y:", value=y_column)
                fig.update_layout(title_text=chart_title, xaxis_title=x_title, yaxis_title=y_title)

                st.plotly_chart(fig, use_container_width=True)
            
            # Gráfico de Dispersión
            elif chart_type == "Dispersión":
                x_column = st.sidebar.selectbox("Eje X:", original_df.columns)
                y_column = st.sidebar.selectbox("Eje Y:", original_df.columns)
                color_column = st.sidebar.selectbox("Agrupar por color:", [None] + list(original_df.columns))
                
                fig = px.scatter(original_df, x=x_column, y=y_column, color=color_column)

                # Ajuste del eje Y para evitar que los datos se salgan
                max_y_value = original_df[y_column].max()
                fig.update_yaxes(range=[0, max_y_value * 1.1])

                # Opciones para títulos de ejes
                x_title = st.sidebar.text_input("Título del Eje X:", value=x_column)
                y_title = st.sidebar.text_input("Título del Eje Y:", value=y_column)
                fig.update_layout(title_text=chart_title, xaxis_title=x_title, yaxis_title=y_title)

                st.plotly_chart(fig, use_container_width=True)
                
        except Exception as e:
            st.error(f"Ocurrió un error al generar el gráfico: {e}")
            st.warning("Asegúrate de que las columnas seleccionadas contengan datos numéricos apropiados para el gráfico.")
    else:
        st.info("La tabla está vacía. Por favor, añade datos para visualizar un gráfico.")

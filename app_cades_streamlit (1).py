
import streamlit as st
import pandas as pd
import plotly.express as px

# Datos simulados
vocaciones_df = pd.DataFrame({
    'Vocación': ['Arte', 'Deporte', 'Tecnología', 'Cultura'],
    'Localidad': ['Gaitana', 'Manitas', 'Bosa', 'San Cristóbal'],
    'Responsable': ['Ana Pérez', 'Luis Gómez', 'Carlos Ruiz', 'Marta Díaz'],
    'Estado': ['Planeado', 'En curso', 'Finalizado', 'Planeado'],
    'Avance (%)': [60, 75, 90, 50]
})

planificacion_df = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo'],
    'Vocación': ['Arte', 'Deporte', 'Tecnología'],
    'Actividad': ['Exposición de arte', 'Torneo deportivo', 'Feria tecnológica'],
    'Responsable': ['Ana', 'Luis', 'Carlos'],
    'Estado': ['Planeado', 'En curso', 'Finalizado']
})

actores_df = pd.DataFrame({
    'Entidad': ['Integración Social', 'Club Deportivo Local', 'Fundación Cultural'],
    'Tipo': ['Gobierno', 'Comunitario', 'ONG'],
    'Contacto': ['contacto@integracion.gov.co', 'clublocal@gmail.com', 'info@fundacioncultural.org'],
    'Zona de Influencia': ['Gaitana', 'Bosa', 'San Cristóbal'],
    'Articulación Posible': ['Adultos mayores', 'Jóvenes deportistas', 'Eventos culturales']
})

st.set_page_config(page_title='Matriz Vocaciones CADES', layout='wide')
st.title('📊 Matriz Interactiva de Vocaciones CADES')

# Filtros
localidades = st.multiselect('Filtrar por Localidad', options=vocaciones_df['Localidad'].unique())
voc_filtradas = vocaciones_df[vocaciones_df['Localidad'].isin(localidades)] if localidades else vocaciones_df

# Gráfico de avance
st.subheader('Avance por Vocación')
fig = px.bar(voc_filtradas, x='Vocación', y='Avance (%)', color='Estado', barmode='group',
             color_discrete_map={'Planeado': 'yellow', 'En curso': 'orange', 'Finalizado': 'red'})
st.plotly_chart(fig, use_container_width=True)

# Planificación mensual
st.subheader('📅 Planificación Mensual')
st.dataframe(planificacion_df, use_container_width=True)

# Mapa de actores
st.subheader('🧩 Mapa de Actores')
st.dataframe(actores_df, use_container_width=True)

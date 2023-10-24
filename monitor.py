import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
import warnings
import datetime
import calendar
import json
import requests
from dash import Dash, dcc, html, Input, Output
import holoviews as hv
import geoviews as gv
import geoviews.feature as gf
from geoviews import tile_sources as gvts
from holoviews import opts

hv.extension('bokeh')

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Monitor endividamento", page_icon=":bar_chart:",layout="wide")

st.title(" :bar_chart: Monitor do endividamento dos brasileiros")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

#Caixa para selecionar as datas

st.sidebar.header("Qual período você deseja consultar?")
diferentes_dividas = pd.read_csv("analise_divida_tempo.csv", encoding="UTF-8", delimiter=',', decimal='.')
diferentes_dividas["data_base"] = pd.to_datetime(diferentes_dividas["data_base"], format='%Y-%m-%d')

min_year = int(diferentes_dividas['data_base'].dt.year.min())
max_year = int(diferentes_dividas['data_base'].dt.year.max())

min_month = int(diferentes_dividas['data_base'].dt.month.min())
max_month = int(diferentes_dividas['data_base'].dt.month.max())

month_abbr = list(calendar.month_abbr) 

def select_month_and_year(name, min_year, max_year, default_month, default_year):
    with st.sidebar.expander(name):
        year = st.selectbox(f'{name} - Ano', range(max_year, min_year - 1, -1), index=max_year - default_year)
        month = st.selectbox(f'{name} - Mês', month_abbr[1:], index=default_month - 1) 
    return month, year

start_month, start_year = select_month_and_year('Data de Início', min_year, max_year, min_month, min_year)
end_month, end_year = select_month_and_year('Data Final', min_year, max_year, max_month, max_year)

date1 = datetime.datetime(start_year, month_abbr.index(start_month), 1)
last_day = calendar.monthrange(end_year, month_abbr.index(end_month))[1]
date2 = datetime.datetime(end_year, month_abbr.index(end_month), last_day)

st.sidebar.markdown(f'<p style="text-align: center">Exibindo dados para o intervalo {date1.strftime("%Y-%m")} a {date2.strftime("%Y-%m")}.</p>', unsafe_allow_html=True)


#Gráfico diferentes dívidas ao longo do tempo

diferentes_dividas["data_base"] = diferentes_dividas["data_base"].dt.to_period('M').dt.to_timestamp()
diferentes_dividas = diferentes_dividas.sort_values(by="data_base")

diferentes_dividas = diferentes_dividas[(diferentes_dividas["data_base"] >= date1) & (diferentes_dividas["data_base"] <= date2)].copy()

st.subheader("Prazo da dívida")

fig = go.Figure()

for col in diferentes_dividas.columns[1:]:
    if col != 'carteira_ativa':
        fig.add_trace(go.Scatter(x=diferentes_dividas['data_base'], 
                                 y=diferentes_dividas[col], 
                                 mode='lines', 
                                 name=col,
                                yaxis='y2'))

# Adicionar barras para 'carteira_ativa'
fig.add_trace(go.Bar(x=diferentes_dividas['data_base'], 
                     y=diferentes_dividas['carteira_ativa'],
                    opacity=0.5,
                    showlegend=False))

# Atualizar o layout
fig.update_layout(
    title='Parcelas a vencer vs Carteira ativa',
    xaxis_title='Data',
    yaxis_title='Parcelas das operações de crédito',
    yaxis2=dict(
        title='Carteira ativa',
        overlaying='y',
        side='right'
    ),
    legend=dict(
        y=-0.2,
        traceorder='normal',
        orientation='h',
        font=dict(
            size=12,
            
        ),
    ),
    template='seaborn'
)

# Exibir o gráfico
st.plotly_chart(fig, use_container_width=True, height=200)

st.subheader("Ocupação (PF) e Setor Econômico vs Dívida vencida acima de 15 dias")
    
df = pd.read_csv("dicionarios_ate2018.csv", encoding="UTF-8", delimiter=',', decimal='.')

df["data_base"] = pd.to_datetime(df["data_base"], format='%Y-%m-%d')

df_filtrado = df[(df["data_base"] >= date1) & (df["data_base"] <= date2)].copy()

plot_ocupacao_divida = px.line(df_filtrado, 
              x="data_base", 
              y="vencido_acima_de_15_dias", 
              color="ocupacao", 
              line_group="ocupacao", 
              labels={"vencido_acima_de_15_dias": "Dívida vencida acima de 15 dias", "data_base": "Date"},
              template="seaborn")

plot_ocupacao_divida.update_layout(
    legend=dict(
        y = -0.2,
        traceorder='normal',
        orientation='h',
        font=dict(
            size=12,
        ),
    )
)

plot_setor_divida = px.line(df_filtrado, 
              x="data_base", 
              y="vencido_acima_de_15_dias", 
              color="ocupacao", 
              line_group="ocupacao", 
              labels={"vencido_acima_de_15_dias": "Dívida vencida acima de 15 dias", "data_base": "Date"},
              template="seaborn")
plot_setor_divida.update_layout(
    legend=dict(
        y = -0.2,
        traceorder='normal',
        orientation='h',
        font=dict(
            size=12,
        ),
    )
)

col1, col2 = st.columns((2))

with col1:
    st.plotly_chart(plot_ocupacao_divida,use_container_width=True, height = 200)

with col2:
    st.plotly_chart(plot_setor_divida,use_container_width=True, height = 200)

st.subheader('Dados macroeconômicos vs endividamento')

inflacao_df = pd.read_csv("estudo_inflacao.csv", encoding="UTF-8", delimiter=',', decimal='.')

inflacao_df["data_base"] = pd.to_datetime(inflacao_df["data_base"], format='%Y-%m')

inflacao_df_filtrado = inflacao_df[(inflacao_df["data_base"] >= date1) & (inflacao_df["data_base"] <= date2)].copy()

plot_inflacao = px.scatter(inflacao_df_filtrado, x="carteira_ativa", y="inflacao",
                          template="seaborn")

st.plotly_chart(plot_inflacao, use_container_width=True)

divida_uf = pd.read_csv("analise_divida_uf.csv", encoding="UTF-8", delimiter=',', decimal='.')
divida_uf["ano"] = pd.to_datetime(divida_uf["ano"], format='%Y')
divida_uf_filtrado = divida_uf[(divida_uf["ano"] >= date1) & (divida_uf["ano"] <= date2)].copy()

divida_uf_filtrado['ano'] = divida_uf_filtrado['ano'].dt.year

divida_uf_filtrado['ano'] = divida_uf_filtrado['ano'].astype('object')

plot_divida_uf = px.bar(divida_uf_filtrado, 
                        x='uf', 
                        y='carteira_ativa',
                        title='Carteira Ativa por UF e Ano',
                        labels={'carteira_ativa':'Carteira Ativa', 'uf_ano':'UF e Ano'},
                        color='ano',
                        barmode = 'group',
                        template="seaborn")
plot_divida_uf.update_layout(
    legend=dict(
        y = -0.2,
        traceorder='normal',
        orientation='h',
        font=dict(
            size=12,
        ),
    )
)

st.plotly_chart(plot_divida_uf, use_container_width=True)

#Mapa

empregado_empresaprivada = pd.read_csv("empregado_empresaprivada_uf_ativoproblematico.csv", encoding="UTF-8", delimiter=',', decimal='.')
servidor_publico = pd.read_csv("servidor_publico_uf_ativoproblematico.csv", encoding="UTF-8", delimiter=',', decimal='.')


url = "https://raw.githubusercontent.com/jonates/opendata/master/arquivos_geoespaciais/unidades_da_federacao.json" #Temos que dar os créditos
response = requests.get(url)
geojson_data = response.json()

st.title('Análise dos ativos problemáticos')

plot_empresaprivada_uf = px.choropleth_mapbox(empregado_empresaprivada, 
                           geojson=geojson_data, 
                           locations='coluna_estado', 
                           color='ativo_problematico',
                           color_continuous_scale="sunsetdark",
                           range_color=(0, max(empregado_empresaprivada['ativo_problematico'])),
                           mapbox_style="open-street-map",
                           zoom=2,
                           animation_frame='ano', 
                           center={"lat": -17.14, "lon": -57.33},
                           opacity=1,
                           labels={'ativo_problematico':'Ativo problemático',
                                   'uf': 'Unidade da Federação do Brasil'},
                           featureidkey="properties.NM_ESTADO",
                           title='Empregados de empresas privadas')

plot_empresaprivada_uf.update_layout(margin={'r':0,'t':0,'l':0, 'b':0})

plot_empregado_servidorpublico = px.choropleth_mapbox(servidor_publico, 
                           geojson=geojson_data, 
                           locations='coluna_estado', 
                           color='ativo_problematico',
                           color_continuous_scale="sunsetdark",
                           range_color=(0, max(servidor_publico['ativo_problematico'])),
                           mapbox_style="open-street-map",
                           zoom=2,
                           animation_frame='ano', 
                           center={"lat": -17.14, "lon": -57.33},
                           opacity=1,
                           labels={'ativo_problematico':'Ativo problemático',
                                   'uf': 'Unidade da Federação do Brasil'},
                           featureidkey="properties.NM_ESTADO",
                           title='Servidores ou empregados públicos')

plot_empregado_servidorpublico.update_layout(margin={'r':0,'t':0,'l':0, 'b':0})

col3, col4 = st.columns((2))

with col3:
    st.plotly_chart(plot_empresaprivada_uf,use_container_width=True, height = 200, config={'scrollZoom': True})

with col4:
    st.plotly_chart(plot_empregado_servidorpublico,use_container_width=True, height = 200, config={'scrollZoom': True})
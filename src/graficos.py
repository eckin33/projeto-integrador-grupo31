import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def grafico_distribuicao_saude(df):
    #grafico 1: Barras Simples
    counts = df['Status de Saúde Mental'].value_counts().reset_index()
    counts.columns = ['Status', 'Quantidade']
    fig = px.bar(counts, x='Status', y='Quantidade', 
                 title='Distribuição do Status de Saúde Mental',
                 color='Status', color_discrete_sequence=px.colors.qualitative.Safe)
    return fig

def grafico_estresse_idade(df):
    # grafico 2: Barras agrupadas
    fig = px.histogram(df, x='Faixa_Etaria', color='Nivel_Estresse', 
                       barmode='group', title='Nível de Estresse por Faixa Etária',
                       category_orders={"Faixa_Etaria": ["18-25", "26-40", "41-60", "60+"]})
    return fig

def grafico_redes_sociais_estresse(df):
    fig = px.scatter(df, x='Horas de Uso de Redes Sociais', y='Estresse_Score',
                     color='Estresse_Score', color_continuous_scale='RdYlGn_r',
                     title='Relação: Uso de Redes Sociais vs Nível de Estresse',
                     render_mode='webgl') 
    return fig

def grafico_sono_saude(df):
    sono_media = df.groupby('Status de Saúde Mental')['Horas de Sono'].mean().reset_index()
    fig = px.bar(sono_media, x='Horas de Sono', y='Status de Saúde Mental', 
                 orientation='h', title='Média de Horas de Sono por Status de Saúde Mental',
                 text_auto='.2f', color='Horas de Sono')
    return fig

def grafico_tempo_tela_genero(df):
    tela_genero = df.groupby('Gênero')['Horas de Tempo na Tela'].mean().reset_index()
    fig = px.bar(tela_genero, x='Gênero', y='Horas de Tempo na Tela',
                 title='Média de Horas de Tempo na Tela por Gênero',
                 text_auto='.2f', color='Gênero')
    return fig

def grafico_suporte_saude(df):
    fig = px.histogram(df, x='Acesso a Sistemas de Suporte', color='Status de Saúde Mental',
                       barnorm='percent', title='Status de Saúde Mental por Acesso a Suporte (%)',
                       barmode='group')
    return fig

def grafico_atividade_estresse(df):
    ativ_estresse = df.groupby('Nivel_Estresse')['Horas de Atividade Física'].mean().reset_index()
    fig = px.bar(ativ_estresse, x='Nivel_Estresse', y='Horas de Atividade Física',
                 title='Atividade Física Média por Nível de Estresse',
                 color='Nivel_Estresse')
    return fig

def grafico_distribuicao_tecnologia(df):
    fig = px.histogram(df, x='Horas de Uso de Tecnologia', nbins=50,
                       title='Distribuição de Horas de Uso de Tecnologia',
                       marginal='box') 
    return fig

def grafico_heatmap_correlacao(df):
    df_numeric = df.select_dtypes(include=[np.number])
    corr = df_numeric.corr()
    fig = px.imshow(corr, text_auto='.2f', aspect="auto",
                    color_continuous_scale='RdBu_r',
                    title='Matriz de Correlação entre Variáveis')
    return fig

def grafico_boxplot_estresse_faixa(df):
    fig = px.box(df, x='Faixa_Etaria', y='Estresse_Score', color='Faixa_Etaria',
                 title='Distribuição do Score de Estresse por Faixa Etária',
                 category_orders={"Faixa_Etaria": ["18-25", "26-40", "41-60", "60+"]})
    return fig

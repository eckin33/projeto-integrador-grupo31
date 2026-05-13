import pandas as pd
import numpy as np

# Parte de Extract
df = pd.read_csv('./data/base.csv')

#Parte de Transform
# Traduzir os nomes das colunas para português
df.rename(columns={
    'User_ID': 'ID do Usuário',
    'Age': 'Idade',
    'Gender': 'Gênero',
    'Technology_Usage_Hours': 'Horas de Uso de Tecnologia',
    'Social_Media_Usage_Hours': 'Horas de Uso de Redes Sociais',
    'Gaming_Hours': 'Horas de Jogos',
    'Screen_Time_Hours': 'Horas de Tempo na Tela',
    'Mental_Health_Status': 'Status de Saúde Mental',
    'Stress_Level': 'Nivel_Estresse',
    'Sleep_Hours': 'Horas de Sono',
    'Physical_Activity_Hours': 'Horas de Atividade Física',
    'Support_Systems_Access': 'Acesso a Sistemas de Suporte',
    'Work_Environment_Impact': 'Impacto do Ambiente de Trabalho',
    'Online_Support_Usage': 'Uso de Suporte Online'
}, inplace=True)

# Traduzir os conteúdos das colunas categóricas
df['Gênero'] = df['Gênero'].map({'Male': 'Masculino', 'Female': 'Feminino', 'Other': 'Outro'})
df['Status de Saúde Mental'] = df['Status de Saúde Mental'].map({'Good': 'Bom', 'Poor': 'Ruim', 'Fair': 'Regular', 'Excellent': 'Excelente'})
df['Nivel_Estresse'] = df['Nivel_Estresse'].map({'Low': 'Baixo', 'Medium': 'Médio', 'High': 'Alto'})
df['Acesso a Sistemas de Suporte'] = df['Acesso a Sistemas de Suporte'].map({'Yes': 'Sim', 'No': 'Não'})
df['Impacto do Ambiente de Trabalho'] = df['Impacto do Ambiente de Trabalho'].map({'Negative': 'Negativo', 'Positive': 'Positivo', 'Neutral': 'Neutro'})
df['Uso de Suporte Online'] = df['Uso de Suporte Online'].map({'Yes': 'Sim', 'No': 'Não'})

# Remover a coluna ID do usuario
df.drop('ID do Usuário', axis=1, inplace=True)

#criacao da faixa etaria
df['Faixa_Etaria'] = pd.cut(df['Idade'], bins=[18, 25, 40, 60, 100], labels=['18-25', '26-40', '41-60', '60+'])

#coluna que o nível de estresse em um valor numérico para facilitar as analises futuras
mapa_estresse = {'Baixo': 1, 'Médio': 2, 'Alto': 3}
df['Estresse_Score'] = df['Nivel_Estresse'].map(mapa_estresse)

#coluna que pode indicar um alerta se o usuario tiver poucas horas de sono e nivel alto de horas de tela
#funciona assim: se o usuario tiver menos de 6 horas de sono e mais de 8 horas de tempo na tela, o alerta sera "sim"
df['Alerta_Saude'] = np.where((df['Horas de Sono'] < 6) & (df['Horas de Tempo na Tela'] > 8), 'Sim', 'Não')

print(df.head())
print(df['Alerta_Saude'].value_counts())

# Parte de Load
# Após a transformação, salvamos a base tratada em um novo arquivo CSV
df.to_csv('./data/base_tratada.csv', index=False)

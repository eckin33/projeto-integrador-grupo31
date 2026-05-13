import pandas as pd

# Parte de Extract
df = pd.read_csv('./data/base.csv')

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
    'Stress_Level': 'Nível de Estresse',
    'Sleep_Hours': 'Horas de Sono',
    'Physical_Activity_Hours': 'Horas de Atividade Física',
    'Support_Systems_Access': 'Acesso a Sistemas de Suporte',
    'Work_Environment_Impact': 'Impacto do Ambiente de Trabalho',
    'Online_Support_Usage': 'Uso de Suporte Online'
}, inplace=True)

print(df.head())
#print(df.info())
#print(df.shape())

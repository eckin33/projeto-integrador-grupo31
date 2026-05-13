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

# Traduzir os conteúdos das colunas categóricas
df['Gênero'] = df['Gênero'].map({'Male': 'Masculino', 'Female': 'Feminino', 'Other': 'Outro'})
df['Status de Saúde Mental'] = df['Status de Saúde Mental'].map({'Good': 'Bom', 'Poor': 'Ruim', 'Fair': 'Regular', 'Excellent': 'Excelente'})
df['Nível de Estresse'] = df['Nível de Estresse'].map({'Low': 'Baixo', 'Medium': 'Médio', 'High': 'Alto'})
df['Acesso a Sistemas de Suporte'] = df['Acesso a Sistemas de Suporte'].map({'Yes': 'Sim', 'No': 'Não'})
df['Impacto do Ambiente de Trabalho'] = df['Impacto do Ambiente de Trabalho'].map({'Negative': 'Negativo', 'Positive': 'Positivo', 'Neutral': 'Neutro'})
df['Uso de Suporte Online'] = df['Uso de Suporte Online'].map({'Yes': 'Sim', 'No': 'Não'})

# Remover a coluna ID do Usuário
df.drop('ID do Usuário', axis=1, inplace=True)

print(df.head())
#print(df.info())
#print(df.shape())

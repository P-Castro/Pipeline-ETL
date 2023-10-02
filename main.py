# fazendo extração de dados de alunos de um cs

import pandas as pd

users = pd.read_csv('SDW2023.csv')
users.head

openai_api_key = 'chave'

# Fazendo a Transformação dos dados
import openai

openai.api_key = openai_api_key

def generate_ai_news(users, index):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em pos-graduação."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {users['UserName'][index]} sobre a importância de fazer uma pos-graduação para o curso de {users['UserCurso'][index]}  (máximo de 100 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')
  

# Carregando os dados em um novo csv  
for index, j in users.iterrows():
 news = generate_ai_news(users, index)
 users['UserMessage'][index] = news


users.to_csv("SDW202301.csv")


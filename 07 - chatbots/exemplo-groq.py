from groq import Groq
import json
import requests
from dotenv import load_dotenv

import os

load_dotenv()

def ligar_ar(mensagem,resposta_dados):
    print(f'Ligando ar condicionado, {mensagem}')
    print(f'JSON: {resposta_dados}')

def desligar_ar(mensagem,resposta_dado):
    print(f'Desligando ae condicionado, {mensagem}')
    print(f'JSON: {resposta_dados}')


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

prompt_do_usuario = input('O que deseja? ')

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": '''
                Analise a mensagem do usuário para identificar qual é a sua 
                intenção, e responda com um json no seguinte formato: 
                {\"intencao\": <numero>, \"resposta\": <texto>}. 
                No atributo \"intencao\" do JSON, deve haver o número da 
                intenção, e no atributo \"resposta\", deve haver uma resposta educada para enviar ao usuário. 
                Caso a intenção seja ligar o ar-condicionado, o número da intenção é 1. 
                Caso a intenção seja desligar o ar-condicionado, o número da intenção é 2. 
                Caso o usuário tenha outra intenção, o número é 0. Não dê respostas fora desse formato.
            '''
        },
        {
            "role": "user",
            "content": prompt_do_usuario
        },
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
    response_format={'type': 'json_object'}
)



resposta_json = completion.choices[0].message.content
resposta_dados = json.loads(resposta_json)

intencao = resposta_dados['intencao']
resposta_ao_usuario = resposta_dados['resposta']

if intencao == 1:
    ligar_ar(resposta_ao_usuario,resposta_dados)
elif intencao == 2:
    desligar_ar(resposta_ao_usuario,resposta_dados)
else:
    print('COMANDO NÃO RECONHECIDO')

  

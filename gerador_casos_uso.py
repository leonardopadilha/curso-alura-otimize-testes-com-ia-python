from openai import OpenAI
from tools import *
from dotenv import load_dotenv

load_dotenv()

cliente = OpenAI()

def gerar_casos_uso(modelo=MODELO_REFINADO):

    # Prompt de sistema
    prompt_sistema = f"""
        Você é um especialista em desenvolver casos de uso. Você deve adotar o padrão abaixo
        para gerar seu caso de uso:

        *Nome da Persona*, em *contexto do app*, precisa realizar *tarefas no app* no aplicativo. Logo, 
        *Benefício Esperado*, para isso ela *descrição detalhada da tarefa realizada*.

        Considere os dados de entrada sugeridos pelo usuário e gere o caso de uso no formato adequado.
    """

    # Prompt de orientação
    prompt_usuario = f"""
        Ana deseja realizar login na plataforma AcordeLab.
    """

    resposta = cliente.chat.completions.create(
        model=modelo,
        messages = [
            { "role": "system", "content": prompt_sistema },
            { "role": "user", "content": prompt_usuario }
        ],
        temperature=0.5
    )

    return resposta.choices[0].message.content
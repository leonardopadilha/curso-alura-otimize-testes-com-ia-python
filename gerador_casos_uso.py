from openai import OpenAI
from tools import *
from dotenv import load_dotenv

load_dotenv()

cliente = OpenAI()

def gerar_casos_uso(prompt, assistente, thread, modelo=MODELO_GPT_4):

    # Prompt de sistema
    pergunta = f"""
        Gere um caso de uso para: {prompt}. 
        Para isso, busque nos arquivos associados a você o conteúdo # Exemplos de Caso de Uso
        (no arquivo exemplos_casos_uso.txt)

        Adote o formato de saída abaixo.

        # Formato de Saída

        *Nome da Persona*, em *contexto do app*, precisa realizar *tarefa no app* no 
        aplicativo. Logo, *Beneficio Esperado*, para isso ela *descrição detalhada da 
        tarefa realizada*.
    """

    cliente.beta.threads.messages.create(
        thread_id = thread.id,
        role = "user",
        content = pergunta
    )

    run = cliente.beta.threads.runds.create(
        thread_id = thread.id,
        assistant_id = assistente.id,
        tools = [{ "type": "retrieval" }],
        model = modelo
    )

    ran = cliente.beta.threads.runds.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    while ran.status != STATUS_COMPLETED:
        print("Gerando Caso: ", ran.status)
        ran = cliente.beta.threads.run.retrieve(
            thread_id = thread.id,
            run_id = run.id
        )

        if ran.status == STATUS_FAILED:
            raise Exception("OpenAI Falhou!")

    mensagens = cliente.beta.threads.messages.list(
        thread_id = thread.id
    )

    return mensagens.data[0].content[0].text.value

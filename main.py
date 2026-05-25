import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

from gerador_casos_uso import *
from gerador_cenarios_teste import *
from gerador_script_teste import *
from tools import *

from assistente_projeto import *
import openai

def main():
    pedido_usuario = input("Digite um caso de uso: ")
    pagina_considerada = "index"

    lista_ids_arquivos = []
    mapa_arquivos = {}
    assistente = None
    vector_store_id = None
    thread = None

    try:
        lista_ids_arquivos, mapa_arquivos = criar_lista_ids_app_web("AcordeLab")
        assistente, vector_store_id = criar_assistente(lista_ids_arquivos=lista_ids_arquivos)
        thread = criar_thread()

        casos_uso = gerar_casos_uso(prompt=pedido_usuario, assistente=assistente, thread=thread)
        print("\nCasos de Uso:\n", casos_uso)

        cenario_teste = gerar_cenario_teste(caso_uso=casos_uso, documento=pagina_considerada, dicionario_arquivos = mapa_arquivos, assistente = assistente, thread = thread)
        print("\nCenário de Teste:\n", cenario_teste)

        script_teste = gerar_script_teste(cenario_teste=cenario_teste, documento=pagina_considerada, dicionario_arquivos=mapa_arquivos, assistente=assistente, thread=thread)
        print("\nScript de Teste\n", script_teste)

        salva(f"scripts_gerados/script_{pagina_considerada}.py", script_teste)

    except openai.APIError as e:
        print("Deu erro: ", e)
    
    finally:
        print("Apagando arquivos gerados...")
        if lista_ids_arquivos:
            apagar_arquivos(lista_ids_arquivos=lista_ids_arquivos)
        if vector_store_id:
            apagar_vector_store(vector_store_id=vector_store_id)
        if assistente is not None:
            apagar_assistente(assistente_id=assistente.id)
        if thread is not None:
            apagar_thread(thread_id=thread.id)
        

    
if __name__ == "__main__":
    main()
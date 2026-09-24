from google.adk.agents.llm_agent import Agent
from trello import TrelloClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

#Suas Credenciais
API_KEY = os.getenv("TRELLO_API_KEY")
API_SECRET = os.getenv("TRELLO_API_SECRET")
TOKEN = os.getenv("TRELLO_TOKEN")

def get_temporal_context():
    now = datetime.now()
    return now.strftime('%d/%m/%Y %H:%M:%S')

def adicionar_tarefa(nome_da_task: str, descricao_da_task: str, due_date: str):
    client = TrelloClient{
        api_key=API_KEY,
        api_secret=API_SECRET,
        token=TOKEN,
    }

    client.list_boards()
    #Obter o board
    boards = client.list_boards()
    meu_board = [b for b in boards if b.name == 'DID'][0]

    #Obter Lista
    listas = meu_board.list_lists()

    minha_lista = [l for l in listas if l.name.upper() == 'TO DO' or l.name.upper() == 'A FAZER'][0]

    #Adicionar o Card (TASK)
    minha_lista.add_card(
        name=nome_da_task,
        desc=descricao_da_task,
        due=due_date,
    )


root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='Você será um Agente Organizador de Tarefas.',
    instruction='''
    
    Você é um agente de organização de tarefas.
    Sua função é criar um card do trello com nome e descrição da tarefa.
    Voce deve perguntar quais tarefas eu tenho do dia e criar um card para cada uma delas.
    Você inicia a conversa assim que for ativado.
    Sempre inicie a conversa perguntando quais são as tarefas do dia informando a data com a tool get_temporal_context.
    Suas Funções:
        1- Adicionar novas tarefas com descrição;
        2- Listar todas as tarefas e filtrar por status
        3- Marcar Tarefas como Concluidas
        4. Remover Tarefas da Lista
        5. Mudar status da tarefa ( De "A Fazer" para "Em andamento" para "Concluido" )
        6- Gerar contexto temporal ( data e hora atual ) para organizar as tarefas do dia

''',
)

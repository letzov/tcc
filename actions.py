try:
    from googlesearch import search
except ImportError:
    print ("no module named 'google' found")
from typing import Any, Text, Dict, List ## Datatypes
from rasa_sdk import Action, Tracker  ##
from rasa_sdk.executor import CollectingDispatcher

class all_of_them(Action): # pode ser qualquer coisa, mas por padrão utilizaremos o nome da ação

    def name(self) -> Text:
        return "utter_name_all" # precisa ser o mesmo nome da ação utilizada nas stories e domain file

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        vacinas = {
        'Astrazeneca': {'numero de doses': 2, 'eficiencia': {'1 dose':'76%', '2 dose': '81%'}, 'eficiencia contra variantes': '92%', 'intervalo entre as doses': '3 meses', 'efeitos colaterais': 'Dor no local da injeção, dor de cabeça, fadiga, dor no corpo e mal esta'},
        'Pfizer': {'numero de doses': 2, 'eficiencia': {'1 dose':'61%', '2 dose': '88%'}, 'eficiencia contra variantes': '88%', 'intervalo entre as doses': '3 meses', 'efeitos colaterais':'Dor no local da injeção, dor de cabeça, fadiga, dor no corpo e mal estar'},
        'Coronavac': {'numero de doses': 2, 'eficiencia': {'1 dose':'sem dados%', '2 dose': '63%'}, 'eficiencia contra variantes': 'entre 69 e 78%', 'intervalo entre as doses': '21 dias', 'efeitos colaterais':'Dor no local da injeção, febre, cansaço e calafrios'},
        'Janssen': {'numero de doses': 1, 'eficiencia': {'1 dose':'85%', '2 dose': 'dose única'}, 'eficiencia contra variantes': '85%', 'intervalo entre as doses': 'dose única', 'efeitos colaterais':'Dor no local da injeção, vermelhidão, dores musculares, febre, náusea, dor no peito e falta de ar'},
        'Moderna': {'numero de doses': 2, 'eficiencia': {'1 dose':'94%', '2 dose': '94%'}, 'eficiencia contra variantes': '94%', 'intervalo entre as doses': '28 dias', 'efeitos colaterais':'Dor no local injeção, febre, vermelhidão, náusea e cansaço'},
        'Sputnik': {'numero de doses': 2, 'eficiencia': {'1 dose':'sem dados', '2 dose': '92%'}, 'eficiencia contra variantes': '81%', 'intervalo entre as doses': '21 dias', 'efeitos colaterais':'Dor no local injeção, febre, vermelhidão, náusea e cansaço'}
        }
        nome1 = 'Astrazeneca'
        nome2 = 'Pfizer'
        nome3 = 'Coronavac'
        nome4 = 'Janssen'
        nome5 = 'Moderna'
        nome6 = 'Sputnik'
        if all == "todas":
            caracteristica = 'eficiencia contra variantes'
            dispatcher.utter_message(text = 'a vacina' + str(nome1)+'possui'+ str(caracteristica)+ str(vacinas[nome1][caracterisca])) 
        #dispatcher.utter_message(text = 'a vacina' + str(nome2)+'possui'+ str(caracteristica)+ str(vacinas[nome2][caracterisca]))
        #dispatcher.utter_message(text = 'a vacina' + str(nome3)+'possui'+ str(caracteristica)+ str(vacinas[nome3][caracterisca]))
        #dispatcher.utter_message(text = 'a vacina' + str(nome4)+'possui'+ str(caracteristica)+ str(vacinas[nome4][caracterisca]))
        #dispatcher.utter_message(text = 'a vacina' + str(nome5)+'possui'+ str(caracteristica)+ str(vacinas[nome5][caracterisca]))
        #dispatcher.utter_message(text = 'a vacina' + str(nome6)+'possui'+ str(caracteristica)+ str(vacinas[nome6][caracterisca]))
        else: 
            all == ""
            
        return []







class ActionSearch(Action): # pode ser qualquer coisa, mas por padrão utilizaremos o nome da ação

    def name(self) -> Text:
        return "action_search" # precisa ser o mesmo nome da ação utilizada nas stories e domain file

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # podemos chamar banco de dados 
        # chamar alguma API
        # fazer qualquer coisa
        # adepois podemos dar um retorno ao usuário
        idade = tracker.get_slot('idade')
        cidade = tracker.get_slot('cidade')
        dispatcher.utter_message(text= 'pessoas com '+ str(idade)+' anos serão vacinadas semana que vem na cidade ' +str(cidade)) 
        return []

class Google(Action): # pode ser qualquer coisa, mas por padrão utilizaremos o nome da ação

    def name(self) -> Text:
        return "search_google" # precisa ser o mesmo nome da ação utilizada nas stories e domain file

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idade = tracker.get_slot('idade')
        cidade = tracker.get_slot('cidade')
        query =  "vacinacao" +str(cidade) +str(idade) 
        resultado = search(query)
        dispatcher.utter_message(text= 'voce pode encontrar essa informação em: '+str(resultado[0]))
        for j in search(query):
            print(j)
        return []

########################

class ActionShowLatestNews(Action):

    def name(self) -> Text:
        return "action_show_latest_news"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='Aqui estão as ultimas noticias..')

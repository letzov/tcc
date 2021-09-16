try:
    from googlesearch import search
except ImportError:
    print ("no module named 'google' found")
from typing import Any, Text, Dict, List ## Datatypes
from rasa_sdk import Action, Tracker  ##
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class kek(Action): # pode ser qualquer coisa, mas por padrão utilizaremos o nome da ação

    def name(self) -> Text:
        return "action_gg" # precisa ser o mesmo nome da ação utilizada nas stories e domain file

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       

        vacinas = {
        'Astrazeneca': {'numero de doses': 2, 'eficiencia': {'1 dose':'76%', '2 dose': '81%'}, 'eficiencia contra variantes': '92%', 'intervalo entre as doses': '3 meses', 'efeitos colaterais': 'Dor no local da injeção, dor de cabeça, fadiga, dor no corpo e mal esta'},
        'Pfizer': {'numero de doses': 2, 'eficiencia': {'1 dose':'61%', '2 dose': '88%'}, 'eficiencia contra variantes': '88%', 'intervalo entre as doses': '3 meses', 'efeitos colaterais':'Dor no local da injeção, dor de cabeça, fadiga, dor no corpo e mal estar'},
        'Coronavac': {'numero de doses': 2, 'eficiencia': {'1 dose':'sem dados%', '2 dose': '63%'}, 'eficiencia contra variantes': 'entre 69% e 78%', 'intervalo entre as doses': '21 dias', 'efeitos colaterais':'Dor no local da injeção, febre, cansaço e calafrios'},
        'Janssen': {'numero de doses': 1, 'eficiencia': {'1 dose':'85%', '2 dose': 'dose única'}, 'eficiencia contra variantes': '85%', 'intervalo entre as doses': 'dose única', 'efeitos colaterais':'Dor no local da injeção, vermelhidão, dores musculares, febre, náusea, dor no peito e falta de ar'},
        'Moderna': {'numero de doses': 2, 'eficiencia': {'1 dose':'94%', '2 dose': '94%'}, 'eficiencia contra variantes': '94%', 'intervalo entre as doses': '28 dias', 'efeitos colaterais':'Dor no local injeção, febre, vermelhidão, náusea e cansaço'},
        'Sputnik': {'numero de doses': 2, 'eficiencia': {'1 dose':'sem dados', '2 dose': '92%'}, 'eficiencia contra variantes': '81%', 'intervalo entre as doses': '21 dias', 'efeitos colaterais':'Dor no local injeção, febre, vermelhidão, náusea e cansaço'}
        }
        nome = 'Astrazeneca'
        nome2 = 'Pfizer'
        nome3 = 'Coronavac'
        nome4 = 'Janssen'
        nome5 = 'Moderna'
        nome6 = 'Sputnik'
        caracteristica = 'eficiencia contra variantes'
        dispatcher.utter_message(text ='A vacina ' + nome + ' possui ' + caracteristica + ": " + str(vacinas[nome][caracteristica]))
        dispatcher.utter_message(text ='A vacina ' + nome2 + ' possui ' + caracteristica + ": " + str(vacinas[nome2][caracteristica]))
        dispatcher.utter_message(text ='A vacina ' + nome3 + ' possui ' + caracteristica + ": " + str(vacinas[nome3][caracteristica]))
        dispatcher.utter_message(text ='A vacina ' + nome4 + ' possui ' + caracteristica + ": " + str(vacinas[nome4][caracteristica]))
        dispatcher.utter_message(text ='A vacina ' + nome5 + ' possui ' + caracteristica + ": " + str(vacinas[nome5][caracteristica]))
        dispatcher.utter_message(text ='A vacina ' + nome6 + ' possui ' + caracteristica + ": " + str(vacinas[nome6][caracteristica]))
        return []

class alfa(Action): 

    def name(self) -> Text:
        return "action_uma" 
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        eficacia = tracker.get_slot('eficacia')
        if eficacia == "Pfizer":
            dispatcher.utter_message(text ='1 dose 61%, 2 dose 88%')

        if eficacia == "Coronavac":
            dispatcher.utter_message(text ='primeira dose sem dados, 2 dose 63%')
        
        if eficacia == "Astrazeneca":
            dispatcher.utter_message(text ='1 dose 76%, 2 dose 81%')

        if eficacia == "Janssen":
            dispatcher.utter_message(text ='85%')

        if eficacia == "Sputnik":
            dispatcher.utter_message(text ='primeira dose sem dados, 2 dose 92%')

        if eficacia == "Moderna":
            dispatcher.utter_message(text ='1 dose 94%, 2 dose 94%')

class NomeVacinasForm(FormAction):

    def name(self) -> Text:

        return "nome_vacinas_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return ["eficacia"]


    @staticmethod
    def eficacia_db() -> List[Text]:
        return [
            "Pfizer",
            "Coronavac",
            
        ]
        
    def validate_spec(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value in self.eficacia_db():
            return {"eficacia": value}
        else: 
            dispatcher.utter_message(template="utter_vacina_invalida")
            return {"eficacia": None}

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any],
    )   -> List[Dict]:
        return []  
        
    







class ActionSearch(Action): 

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

    



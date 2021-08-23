try:
    from googlesearch import search
except ImportError:
    print ("no module named 'google' found")
from typing import Any, Text, Dict, List ## Datatypes
from rasa_sdk import Action, Tracker  ##
from rasa_sdk.executor import CollectingDispatcher

pfeizer [
["número de doses",2],
["eficacia após primeira dose", 61%],
["eficacia após duas doses",85%],
["efeitos colaterais","dor no corpo, no local da injeção, dor de cabeça e fadiga"],
["país de origem","EUA e Alemanha"]
["aprovada pela anvisa","Sim"],
["eficácia contra variantes","88%"],
["como é feita", ],
["intervalo entre doses","21 dias"],
["eficácia por faixa etária","acima de 55 anos, 94%, entre 16 e 55 anos 95%"]
]
aztrazeneca [
["número de doses",2],
["eficacia após primeira dose",76%],
["eficacia após duas doses",81%],
["efeitos colaterais","dor no corpo, no local da injeção, dor de cabeça e fadiga"],
["país de origem","Inglaterra"]
["aprovada pela anvisa","Sim"],
["eficácia contra variantes", 67%],
["como é feita",],
["intervalo entre doses"","90 dias"],
["eficácia por faixa etária","acima de 80 anos, 90%, entre 60 e 79 anos, 93%, entre 18 e 59 anos, 60%"]
]
coronavac [
["número de doses",2],
["eficacia após primeira dose",76%],
["eficacia após duas doses",63%]
["efeitos colaterais","dor no corpo, no local da injeção, dor de cabeça e fadiga"],
["país de origem","Brasil e China"]
["aprovada pela anvisa","Sim"],
["eficácia contra variantes", ""],
["como é feita",],
["intervalo entre doses",""],
["eficácia por faixa etária",""]
]
janssen
["número de doses",1,
["eficacia após primeira dose",85%],
["eficacia após duas doses","dose única"],
["efeitos colaterais","dor no corpo, no local da injeção, dor de cabeça,fadiga e calafrios"],
["país de origem","EUA"]
["aprovada pela anvisa","Sim"],
["eficácia contra variantes", 67%],
["como é feita",""],
["intervalo entre doses","dose única"],
["eficácia por faixa etária","acima de 59 anos, 76%, entre 18 e 59 anos,64%"]
]
moderna
["número de doses",2],
["eficacia após primeira dose",94%],
["eficacia após duas doses"94%,],
["efeitos colaterais","dor no corpo, no local da injeção, vermelhidão, náusea e cansaço"],
["país de origem","EUA"]
["aprovada pela anvisa","Sim"],
["eficácia contra variantes", 94%],
["como é feita",""],
["intervalo entre doses","28 dias"],
["eficácia por faixa etária","acima de 65 anos, 86%, entre 18 e 64 anos,95%"]
]
sputnik
["número de doses",2],
["eficacia após primeira dose",""],
["eficacia após duas doses"92%,],
["efeitos colaterais","dor no corpo, no local da injeção, vermelhidão, náusea e cansaço"],
["país de origem","Rússia"]
["aprovada pela anvisa","Não"],
["eficácia contra variantes", ""],
["como é feita",""],
["intervalo entre doses","21 dias"],
["eficácia por faixa etária","De acordo com o laboratório responsável pela sputink, a eficácia da vacina é igual para todas as faixas etárias"]
]







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
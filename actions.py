try:
    from googlesearch import search
except ImportError:
    print ("no module named 'google' found")
from typing import Any, Text, Dict, List ## Datatypes
from rasa_sdk import Action, Tracker, FormValidationAction  ##
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


vacinas = {
'astrazeneca': {'numero de doses': 2, 'eficiencia por faixa etaria': 'Acima de 80 anos = 91% entre 60 e 79 anos = 93% entr 18 e 59 anos = 60% ', 'eficiencia': {'1 dose':'76%', '2 dose': '81%'}, 'eficiencia contra variantes': '92%', 'intervalo entre as doses': '3 meses', 'efeitos colaterais': 'Dor no local da injeção, dor de cabeça, fadiga, dor no corpo e mal esta', 'tecnologia': 'Usa uma técnica conhecida como vetor viral não replicante.  Funciona da seguinte maneira: Utiliza um "vírus vivo", tal qual um adenovírus (causador do resfriado), que não consegue se replicar no organismo humano ou causar malefícios a saúde.  Este adenovírus também é modificado através de engenharia genética para passar a carregar dentro de si as instruções para a produção de uma proteína característica do  coronavírus. Ao entrar nas células, o adenovírus faz com que elas comecem a produzir essa proteína e a exiba em sua superfície, o que é detectado pelo  sistema imunológico, que age de maneira para combater o coronavírus e cria uma resposta protetora contra uma infecção.'},
'pfizer': {'numero de doses': 2, 'eficiencia por faixa etaria': 'Acima de 55 anos = 94% Entre 16 e 55 anos = 95%', 'eficiencia': {'1 dose':'61%', '2 dose': '88%'}, 'eficiencia contra variantes': '88%', 'intervalo entre as doses': '3 meses', 'efeitos colaterais':'Dor no local da injeção, dor de cabeça, fadiga, dor no corpo e mal estar', 'tecnologia': 'A vacina utiliza a tecnologia chamada de mRNA ou RNA-mensageiro. Os imunizantes são produzidos por meio de replicação de sequências de RNA através de engenharia genética. O RNA mensageiro imita a proteína spike, específica do vírus Sars-CoV-2, que o ajuda a invadir as células humanas.  Essa "cópia", contudo, não causa prejuízos a saúde, como o vírus, mas é o suficiente para desencadear uma reação das células do sistema imunológico, que por sua vez, cria uma defesa no organismo '},
'coronavac': {'numero de doses': 2, 'eficiencia por faixa etaria': 'Faltam dados conclusivos sobre a eficácia da Coronavac por faixa etária', 'eficiencia': {'1 dose':'sem dados%', '2 dose': '63%'}, 'eficiencia contra variantes': 'entre 69% e 78%', 'intervalo entre as doses': '21 dias', 'efeitos colaterais':'Dor no local da injeção, febre, cansaço e calafrios', 'tecnologia': 'Feita com  uma técnica conhecida como  "vírus inativo": Nesta técnica, o vírus é cultivado e multiplicado e depois inativado através de uma reação química ou aquecimento. O organismo que entrar em contato com a vacina com o vírus  já inativo, começa a produzir os anticorpos necessários para combater o coronavírus.  As células defesa que começam à resposta imune, encontram os vírus inativados e os capturam, ativando os linfócitos.  Os linfócitos por sua vez, começam a produzir anticorpos, que entram em contato com os vírus para evitar a infecção das células.'},
'janssen': {'numero de doses': 1, 'eficiencia por faixa etaria': 'Acima de 59 anos = 76% Entre 18 e 59 anos = 64%', 'eficiencia': {'1 dose':'85%', '2 dose': 'dose única'}, 'eficiencia contra variantes': '85%', 'intervalo entre as doses': 'dose única', 'efeitos colaterais':'Dor no local da injeção, vermelhidão, dores musculares, febre, náusea, dor no peito e falta de ar', 'tecnologia': 'A tecnologia utilizada na vacina da Janssen é baseada em vetores de adenovírus —tipo de vírus que causam o resfriado comum, mas após serem modificados para desenvolver a vacina, eles não se  replicam e não causam resfriado, nem qualquer outro malefício para a saúde humana.  Para realizar a produção da vacina, um pedaço da proteína "S", presente nessas espículas responsáveis pela ligação do vírus às células do corpo humano, é colocado dentro do adenovírus  . Quando alguém recebe a vacina composta do adenovírus não replicante, que carrega a informação genética do novo coronavírus,  o organismo começa um processo de defesa e produz anticorpos contra tal invasor, o que acarreta na criação de uma memória do organismo contra o coronavírus' },
'moderna': {'numero de doses': 2, 'eficiencia por faixa etaria': 'Acima de 65 anos = 86% entre 18 e 65 anos = 95%', 'eficiencia': {'1 dose':'94%', '2 dose': '94%'}, 'eficiencia contra variantes': '94%', 'intervalo entre as doses': '28 dias', 'efeitos colaterais':'Dor no local injeção, febre, vermelhidão, náusea e cansaço', 'tecnologia': 'A vacina da Moderna utiliza a técnica do RNA mensageiro, ou mRNA, uma espécie de receita que imitam fragmentos do aspecto externo do coronavírus. Após a injeção da vacina, o sistema imunológico produz anticorpos contra estes fragmentos. A vacina da Moderna, contém um mRNA sintético que é capaz de codificar uma estrutura conhecida como glicoproteína de fragmento estabilizada em pré-fusão do vírus.'},
'sputnik': {'numero de doses': 2, 'eficiencia por faixa etaria': 'Os desenvolvedores da Sputnik afirmam que o imunizante possui a mesma eficacia para todas as faixas etárias', 'eficiencia': {'1 dose':'sem dados', '2 dose': '92%'}, 'eficiencia contra variantes': '81%', 'intervalo entre as doses': '21 dias', 'efeitos colaterais':'Dor no local injeção, febre, vermelhidão, náusea e cansaço', 'tecnologia': 'Utiliza a técnica do vetor viral não replicante. De maneira análoga a técnica utilizada pela Pfizer, a vacina da Sputnik é feita com adenovírus que responsáveis pelos resfriados. Os adenovírus são modificados em laboratório para não sejam capazes de se replicar após entrarem em contato com as células humanas.  Os adenovírus presentes na vacina possuem instruções genéticas para a produção de uma proteína característica do novo coronavírus, a espícula.  Uma vez no organismo, os adenovírus entram nas células e fazem com que elas comecem a produzir e exibir essa proteína nas suas superfícies.  Isso faz com que sistema imunológico que acione células de defesa que por sua vez, aprende a combater o coronavírus.'}
}


class actionEficienciaUma(Action):

    def name(self) -> Text:
        return "action_inform_eficiencia_uma"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot('nomevacina')
        if nome in vacinas:
            dispatcher.utter_message(text ='A eficácia da vacina ' + nome + ' é de ' + vacinas[nome]['eficiencia']['1 dose'] + ' após a primeira dose e ' + vacinas[nome]['eficiencia']['2 dose'] + ' após a segunda dose.' )
        else:
            dispatcher.utter_message(text ='Vacina não encontrada na base de dados')

class actionEficienciaUmaVariantes(Action):

    def name(self) -> Text:
        return "action_inform_eficacia_uma_variantes"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot('nomevacina')
        if nome in vacinas:
            dispatcher.utter_message(text ='A eficácia contra as variantes da ' + nome + ' é de ' + vacinas[nome]['eficiencia contra variantes'] )
        else:
            dispatcher.utter_message(text ='Vacina não encontrada na base de dados')

class actionEficienciaTodas(Action): # pode ser qualquer coisa, mas por padrão utilizaremos o nome da ação

    def name(self) -> Text:
        return "action_inform_eficienciatodas" # precisa ser o mesmo nome da ação utilizada nas stories e domain file

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        caracteristica = 'eficiencia'
        for nome in vacinas.keys():
            dispatcher.utter_message(text ='A vacina ' + nome + ' possui ' + caracteristica + ": " + str(vacinas[nome][caracteristica]))
        return []

class actionEficienciaTodasVariantes(Action): # pode ser qualquer coisa, mas por padrão utilizaremos o nome da ação

    def name(self) -> Text:
        return "action_inform_eficienciatodas_variantes" # precisa ser o mesmo nome da ação utilizada nas stories e domain file

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        caracteristica = 'eficiencia contra variantes'
        for nome in vacinas.keys():
            dispatcher.utter_message(text ='A vacina ' + nome + ' possui ' + caracteristica + ": " + str(vacinas[nome][caracteristica]))

class Google(Action): # pode ser qualquer coisa, mas por padrão utilizaremos o nome da ação

    def name(self) -> Text:
        return "action_search_google" # precisa ser o mesmo nome da ação utilizada nas stories e domain file

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


class actionEfeitoscolateraisespecifica(Action):

    def name(self) -> Text:
        return "action_colaterais_uma_vacina"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot('nomevacina')
        if nome in vacinas:
            dispatcher.utter_message(text ='Os efeitos colaterais da vacina ' + nome + ' são: ' + vacinas[nome]['efeitos colaterais'] )
        else:
            dispatcher.utter_message(text ='Vacina não encontrada na base de dados')

class actionEfeitoscolaterais(Action): # pode ser qualquer coisa, mas por padrão utilizaremos o nome da ação

    def name(self) -> Text:
        return "action_colaterais" # precisa ser o mesmo nome da ação utilizada nas stories e domain file

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        caracteristica = 'efeitos colaterais'
        for nome in vacinas.keys():
            dispatcher.utter_message(text ='A vacina ' + nome + ' possui os seguintes '  + caracteristica + ": "  + str(vacinas[nome][caracteristica]))
        return []

class actionintervaloentretodas(Action): # pode ser qualquer coisa, mas por padrão utilizaremos o nome da ação

    def name(self) -> Text:
        return "action_intervalo_todas_doses" # precisa ser o mesmo nome da ação utilizada nas stories e domain file

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        caracteristica = 'intervalo entre as doses'
        for nome in vacinas.keys():
            dispatcher.utter_message(text ='O ' + caracteristica + ' da vacina '  + nome + " é: "  + str(vacinas[nome][caracteristica]))
        return []


class actionIntervaloEpecifica(Action):

    def name(self) -> Text:
        return "action_intervalo_doses"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot('nomevacina')
        if nome in vacinas:
            dispatcher.utter_message(text ='O intervalo entre as doses da vacina ' + nome + ' é: ' + vacinas[nome]['intervalo entre as doses'] )
        else:
            dispatcher.utter_message(text ='Vacina não encontrada na base de dados')


class actioneficacia1(Action):

    def name(self) -> Text:
        return "action_eficacia_primeira_dose"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot('nomevacina')
        if nome in vacinas:
            dispatcher.utter_message(text ='A eficacia da primeira dose da ' + nome + ' é: ' + vacinas[nome]['eficiencia']['1 dose'] )
        else:
            dispatcher.utter_message(text ='Vacina não encontrada na base de dados')


class actioneficacia2(Action):

    def name(self) -> Text:
        return "action_eficacia_segunda_dose"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot('nomevacina')
        if nome in vacinas:
            dispatcher.utter_message(text ='A eficacia da segunda dose da ' + nome + ' é: ' + vacinas[nome]['eficiencia']['2 dose'] )
        else:
            dispatcher.utter_message(text ='Vacina não encontrada na base de dados')

class actionfaixaetariaall(Action): # pode ser qualquer coisa, mas por padrão utilizaremos o nome da ação

    def name(self) -> Text:
        return "action_faixa_etaria_todas" # precisa ser o mesmo nome da ação utilizada nas stories e domain file

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        caracteristica = 'eficiencia por faixa etaria'
        for nome in vacinas.keys():
            dispatcher.utter_message(text ='A vacina ' + nome + ' possui a seguinte '  + caracteristica + " : "  + str(vacinas[nome][caracteristica]))
        return []


class actionfaixaetariasingle(Action):

    def name(self) -> Text:
        return "action_faixa_etaria_individual"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot('nomevacina')
        if nome in vacinas:
            dispatcher.utter_message(text ='A eficacia por faixa etaria da ' + nome + ' é: ' + vacinas[nome]['eficiencia por faixa etaria'] )
        else:
            dispatcher.utter_message(text ='Vacina não encontrada na base de dados')

class actioncomofuncionaespecifica(Action):

    def name(self) -> Text:
        return "action_tecnologia_especifica"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot('nomevacina')
        if nome in vacinas:
            dispatcher.utter_message(text ='A vacina ' + nome + ' funciona da seguinte maneira ' + vacinas[nome]['como funciona'] )
        else:
            dispatcher.utter_message(text ='Vacina não encontrada na base de dados')

class actiontecnologiatodas(Action): # pode ser qualquer coisa, mas por padrão utilizaremos o nome da ação

    def name(self) -> Text:
        return "action_tecnologia_todas" # precisa ser o mesmo nome da ação utilizada nas stories e domain file

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        caracteristica = 'tecnologia'
        for nome in vacinas.keys():
            dispatcher.utter_message(text ='A vacina ' + nome + ' funciona assim '  + caracteristica + " : "  + str(vacinas[nome][caracteristica]))
        return []




class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_nomevacina_form"

    def validate_nomevacina(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `nomevacina` value."""
        print(f"Nome fornecido = {slot_value}")
        if str.lower(slot_value) in vacinas:
            print(f"Nome válido = {slot_value}")
            return {"nomevacina": str.lower(slot_value)}
        else:
            print(f"Nome Inválido = {slot_value}")
            dispatcher.utter_message(text=f"Nome inválido")
            return {"nomevacina": None}
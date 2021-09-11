## storie
* greet
  - utter_how_can_I_help
* when_vaccine{"calendar":"quando"}
  - utter_ask_age
* informar_idade{"idade":"20"}
  - utter_ask_city
* informar_cidade{"cidade":"ararangua"}
  - search_google
    



## storie2
* greet
  - utter_how_can_I_help
* eficacia_vacinas 
  - utter_uma_ou_todas
* todas_vacinas
  - action_gg

## storie2
* greet
  - utter_how_can_I_help
* eficacia_vacinas 
  - utter_uma_ou_todas
* spec_vacinas{"eficacia":"Pfizer"}
  - action_uma


## storie3
* greet
  - utter_how_can_I_help
* transmissao_vacina {"transmissao":"virus"}
  - utter_vacinados

## storie4
* greet
  - utter_how_can_I_help
* utter_vacina_jovens {"young":"jovens"}
  - utter_populacao_jovem

## storie5
* greet
  - utter_how_can_I_help
* utter_reacao_vacina {"reação":"vacinas"} 
  - utter_alergia

## storie6 
* greet
  - utter_how_can_I_help
* utter_variantes_vaccine {"variante":"cepas"}
  - utter_variante  

## storie67
* greet
  - utter_how_can_I_help
* utter_onde_vacinar {"where":"locais"}
  - utter_local

## storie666
* greet
  - utter_how_can_I_help
* utter_sem_segunda_dose {"second":"doses"}
  - utter_apenas_primeira_dose

import json
from collections import defaultdict

def load_json(data):
    with open(data, 'r') as file:
        return json.load(file)

#function that evaluates variables with fuzzification.py

def apply_rule(fuzzified_inputs, rules, countries):

    destination_scores = defaultdict(float)

    for rule in rules:
        condition = rule['if']
        destinations = rule['then']

        strength = #function that evaluates variables with fuzzification.py

        if strength == 0:
            continue
        
        for country in destinations:
            if country in countries:
                destination_scores[country] += strength

    return destination_scores

def evaluate_destinations(fuzzified_inputs, rules_data = "rules.json", countries_data = "countries.json"):
    
    rules = load_json(rules_data)
    countries = load_json(countries_data)

    scores = apply_rule(fuzzified_inputs, rules, countries)

    return scores

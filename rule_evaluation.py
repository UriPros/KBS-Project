import json
from collections import defaultdict

def load_json(data):
    with open(data, 'r') as file:
        return json.load(file)

#function that evaluates variables with fuzzification.py

#function that applies rules and returns scores for each destination

def evaluate_destinations(fuzzified_inputs, rules_data = "rules.json", countries_data = "countries.json"):
    
    rules = load_json(rules_data)
    countries = load_json(countries_data)

    scores = ""

    return scores

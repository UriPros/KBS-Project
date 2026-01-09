import json
from fuzzification import fuzzify_user_input
from rule_evaluation import evaluate_rules
from defuzzification import defuzzify


def recommend_destination(user_input):
    with open("destinations.json") as f:
        destinations = json.load(f)

    with open("countries.json") as f:
        rules = json.load(f)

    with open("fuzzy_sets.json") as f:
        fuzzy_sets = json.load(f)

    fuzzified_inputs = fuzzify_user_input(user_input, fuzzy_sets) #fuzzification

    scores = evaluate_rules(fuzzified_inputs, rules, destinations) # rule evaluation

    def_scores = defuzzify(scores) # defuzzification

    best = max(def_scores, key=def_scores.get) #choose best destination

    return best, def_scores

if __name__ == "__main__":
    user_input = {
        "temperature": 0.2,
        "budget": 0.6,
        "eco_friendly": 0.6
    }

    best, scores = recommend_destination(user_input)

    print("Recommended destination:", best)
    print("Scores:", dict(scores))

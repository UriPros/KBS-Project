import json
from fuzzification import fuzzify_user_input, extract_weather_label
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
    fuzzified_inputs = fuzzify_user_input(user_input, fuzzy_sets)

    # OPTIONAL, ho he posat just TO CHCK: print("FUZZIFIED INPUTS:", fuzzified_inputs)

    weather_label = extract_weather_label(fuzzified_inputs)
    if weather_label:
        fuzzified_inputs["weather"] = {weather_label: 1.0}


    scores = evaluate_rules(fuzzified_inputs, rules, destinations) # rule evaluation

    def_scores = defuzzify(scores) # defuzzification

    if not def_scores:
        return None, {}

    best = max(def_scores, key=def_scores.get) #choose best destination

    return best, def_scores

if __name__ == "__main__":
    user_input = {
        "avg_temperature": 20,
        "budget": 150,
        "eco_friendly": 0.8
    }


    best, scores = recommend_destination(user_input)

    print("Recommended destination:", best)
    print("Scores:", dict(scores))



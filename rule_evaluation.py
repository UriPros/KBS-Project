from collections import defaultdict

def evaluate_rules(fuzzified_inputs, rules, destinations):

    destination_scores = defaultdict(dict)

    for idx, rule in enumerate(rules):
        condition = rule["if"]
        recommended = rule["then"]

        strength = 1.0

        for variable, label in condition.items():

            if variable not in fuzzified_inputs:
                strength = 0
                break

            strength = min(strength, fuzzified_inputs[variable].get(label, 0))

        if strength == 0:
            continue

        for dest in recommended:
            if dest in destinations:
                destination_scores[dest][f"r{idx}"] = strength

    return destination_scores

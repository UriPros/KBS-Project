from collections import defaultdict

def evaluate_rules(fuzzified_inputs, rules, destinations):

    # CHANGED: store fuzzy contributions, not floats
    destination_scores = defaultdict(dict)

    for idx, rule in enumerate(rules):
        condition = rule["if"]
        recommended = rule["then"]

        # Rule strength (AND = min)
        strength = 1.0
        for variable, fuzzy_values in fuzzified_inputs.items():
            if variable in condition:
                label = condition[variable]
                strength = min(strength, fuzzy_values.get(label, 0))

        if strength == 0:
            continue

        # CHANGED: store each rule's contribution
        for dest in recommended:
            if dest in destinations:
                destination_scores[dest][f"r{idx}"] = strength

    return destination_scores

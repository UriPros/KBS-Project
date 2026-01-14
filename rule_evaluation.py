from collections import defaultdict

def evaluate_rules(fuzzified_inputs, rules, destinations):

    destination_scores = defaultdict(dict)

    for idx, rule in enumerate(rules):
        condition = rule["if"]
        recommended = rule["then"]

        strengths = []

        for variable, label in condition.items():
            if variable in fuzzified_inputs:
                strengths.append(fuzzified_inputs[variable].get(label, 0))

        if not strengths:
            continue

        rule_strength = sum(strengths) / len(strengths)

        for dest in recommended:
            if dest in destinations:
                destination_scores[dest][f"r{idx}"] = rule_strength

    return destination_scores

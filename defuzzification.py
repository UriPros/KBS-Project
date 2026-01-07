def defuzzify_destination(scores):

    if not scores:
        return 0.0
    
    numerator = sum(scores.values())
    denominator = len(scores)

    return round (numerator / denominator, 2)


def defuzzify(scores):

    final_scores = {}

    for destination, fuzzy_scores in scores.items():

        final_scores[destination] = defuzzify_destination(fuzzy_scores)

    return final_scores

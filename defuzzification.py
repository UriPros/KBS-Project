def defuzzify_destination(scores):
    if not scores:
        return 0.0
    return max(scores.values())


def defuzzify(scores):

    final_scores = {}

    for destination, fuzzy_scores in scores.items():

        final_scores[destination] = defuzzify_destination(fuzzy_scores)

    return final_scores

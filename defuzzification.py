def defuzzify_destination(scores):
    if not scores:
        return 0.0
    return sum(scores.values()) / len(scores) #ho podem canviar perque retorni el que vulguem


def defuzzify(scores):

    final_scores = {}

    for destination, fuzzy_scores in scores.items():
        final_scores[destination] = defuzzify_destination(fuzzy_scores)

    destinations_list = list(final_scores.items())

    # Sort the list by the score from highest to lowest
    destinations_list.sort(key=lambda x: x[1], reverse=True)

    top3_list = destinations_list[:3]

    top3_scores = {destination: score for destination, score in top3_list}


    return top3_scores

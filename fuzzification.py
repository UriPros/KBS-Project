import json

def load_sets (data = "fuzzy_sets.json"):
    with open(data, "r") as f:
        return json.load(f)


def trapezoidal(x, a, b, c, d):
    if x < a or x > d:
        return 0.0
    elif a <= x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1.0
    elif c < x <= d:
        return (d - x) / (d - c)


def fuzzify(value, sets):

    memberships = {}

    for set_name, params in sets.items():
        
        a, b, c , d = params
        memberships[set_name] = round(trapezoidal(value, a, b, c, d), 3)
    
    return memberships

def fuzzify_user_input(user_input, fuzzy_sets):
    
    fuzzified_inputs = {}

    for variable, value in user_input.items():
        if variable in fuzzy_sets:
            fuzzified_inputs[variable] = fuzzify(value, fuzzy_sets[variable])

    return fuzzified_inputs

def extract_weather_label(fuzzified_inputs):
    weather_fuzzy = fuzzified_inputs.get("weather")

    if not weather_fuzzy:
        return None

    return max(weather_fuzzy, key=weather_fuzzy.get)


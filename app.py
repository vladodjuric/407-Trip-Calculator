import json

with open('interchanges.json', 'r') as f:
    data = json.load(f)
    locations = data['locations']
interchanges = {locations[i]['name'] : [locations[i]['routes'], i] for i in locations}

def costOfTrip(l1, l2):
    if l1 == l2 or l1 not in interchanges or l2 not in interchanges:
        raise ValueError("Please provide two unique, valid interchanges.")
    cost = 0.25
    distance = 0
    points = [interchanges[l1], interchanges[l2]]
    if int(points[0][-1]) < int(points[1][-1]):
        start, end = 0, 1
    else:
        start, end = 1, 0

    x, y = int(points[start][-1]), int(points[end][-1])
    exclusions = {21, 27}
    while x != y:
        route = 0 if x < y else 1
        distance += locations[str(x)]['routes'][route]['distance']
        if x < y:
            x += 1 if x+1 not in exclusions else 2
        else:
            x -= 1 if x-1 not in exclusions else 2
    print(f'The distance from {l1} to {l2} is: {str(round(distance,2))}km, and the cost is: ${str(round(cost * distance))}CAD')
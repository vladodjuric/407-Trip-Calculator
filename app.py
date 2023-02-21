import json
with open('interchanges.json', 'r') as f:
    data = json.load(f)

x = data['locations']

def costOfTrip(l1, l2):
    if l1 == l2:
        raise ValueError("Please provide two unique,valid interchanges.")
    cost = 0.25
    distance = 0
    stops = []
    for i in x:
        if l1 in x[i].values() or l2 in x[i].values():
            stops.append([i, x[i]])
        if len(stops) == 2:
            break
    if len(stops) != 2:
        raise ValueError("Please provide two unique,valid interchanges.")
    if int(stops[0][0]) < int(stops[1][0]):
        d = int(stops[0][0])
        while d < int(stops[1][0]):
            distance += x[str(d)]['routes'][0]['distance']
            if d == 20 or d == 26:
                d += 2 
            else:
                d += 1
    else:
        y = int(stops[1][0])
        while y > int(stops[0][0]):
            distance += x[str(d)]['routes'][1]['distance']
            if y == 22 or y == 28:
                y -= 2
            else:
                y -= 1
    print(f'The distance from {l1} to {l2} is: {str(round(distance,2))}km, and the cost is: ${str(round(cost * distance))}CAD')
if __name__ == '__main__':
    costOfTrip('QEW', 'Highway 400')
    costOfTrip('Salem Road', 'QEW')
    costOfTrip('QEW', 'Salem Road')
f.close()

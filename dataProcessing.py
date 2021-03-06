from Read_data import read_json, read_pickle
from bokeh.colors import RGB
import time

def generate_severityDictionary(severityLevel, color):
    filename = 'processed_data/completeSeverity{}.pickle'.format(severityLevel)
    colorname = 'processed_data/severity{}_violation_percentage.pickle'.format(severityLevel)
    results = read_pickle(filename)
    rating = getRatings()
    data = dict(lat=[], lon=[], color=[], name=[], rating=[])
    limit = 0
    for name in results:
        data['lat'].append(results[name]['location'][0])
        data['lon'].append(results[name]['location'][1])
        data['color'].append(color)
        data['name'].append(name)
        data['rating'].append(rating[name])
        limit += 1
    return data

def generate_foodtypeDictionary(filename, foodtype, color):
    results = read_pickle(filename)
    coordinates = getCoordinates()
    rating = getRatings()
    data = dict(lat=[], lon=[], color=[], name=[], rating=[],foodtype=[])
    limit = 0
    for name in results:
        if results[name]['foodtype'] == foodtype:
            try:
                data['lat'].append(coordinates[name]['location'][0])
                data['lon'].append(coordinates[name]['location'][1])
            except:
                data['lat'].append(0)
                data['lon'].append(0)
            data['color'].append(color)
            data['name'].append(name)
            data['rating'].append(rating[name])
            data['foodtype'].append(foodtype)
            limit += 1
    return data


def generate_mainDictionary(filename):
    results = read_pickle(filename)
    coordinates = getCoordinates()
    rating = getRatings()
    data = dict(lat=[], lon=[], color=[], name=[], rating=[])
    limit = 0
    for name in results:
        red, green, blue = results[name]['color'][0], results[name]['color'][1], results[name]['color'][2]
        data['lat'].append(coordinates[name]['location'][0])
        data['lon'].append(coordinates[name]['location'][1])
        data['color'].append(RGB(red, green, blue))
        data['name'].append(name)
        data['rating'].append(rating[name])
        limit += 1
    return data

def getCoordinates():
    coordinates = read_pickle('processed_data/completeSeverity1.pickle')
    for i in range(2,4):
        print(i)
        filename='processed_data/completeSeverity{}.pickle'.format(i)
        tempDict = read_pickle(filename)
        print(type(coordinates), type(tempDict))
        coordinates = z = {**coordinates, **tempDict}
        print(type(coordinates))
    return coordinates

def getRatings():
    ratings = read_pickle('processed_data/rating.pickle')
    return ratings
# def generate_dictionary(filename='word', color='red', stop=49):
#     results = read_pickle(filename)
#     data = dict(lat=[], lon=[], color=[])
#     limit = 0
#     for name in results:
#         data['lat'].append(results[name]['lon'])
#         data['lon'].append(results[name]['lat'])
#         data['color'].append(RGB(255,0,0))
#         if limit > stop:
#             break
#         limit += 1
#     return data
#


if __name__ == "__main__":
    pass
    #generate_dictionary('completeSeverity1.pickle', color='red')

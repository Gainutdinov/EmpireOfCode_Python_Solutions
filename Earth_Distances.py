import re
from math import radians, sin, cos, sqrt, asin
R = 6371

def distance(first, second):

    h1, w1 = first.replace(", ", " ").replace(",", " ").split(" ") #latitude, longitude
    h2, w2 = second.replace(", ", " ").replace(",", " ").split(" ")
    #print(h1,w1,h2,w2)
    reg = r"(\d+)°(\d+)′(\d+)″(\D)"

    h1 = re.match(reg, h1).groups() #возвращает кортеж в котором содержащий значения всех групп.
    #  помомщью ...groups("MyMessage") можно выводить сообщ. если такие группы не нашлись
    h2 = re.match(reg, h2).groups()
    w1 = re.match(reg, w1).groups()
    w2 = re.match(reg, w2).groups()
    coordinates = [h1,w1,h2,w2]
    for i, s in enumerate(coordinates):
        if ('S' in coordinates[i]) or ('W' in coordinates[i]):
            coordinates[i] = -(float(s[0]) + float(s[1]) / 60 + float(s[2]) / 3600)
        else:
            coordinates[i] = float(s[0]) + float(s[1]) / 60 + float(s[2]) / 3600
    h1,w1,h2,w2 = coordinates
    dlon = radians(w2 - w1)  #w2 - w1
    dlat = radians(h2 - h1)  # h2 - h1
    a = pow(sin(dlat / 2), 2) + cos(radians(h1)) * cos(radians(h2)) * pow(sin(dlon / 2), 2)
    c = 2 * asin(sqrt(a))
    result = R * c
    #print(round(result,1))
    return round(result,1)



distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W")
#    assert almost_equal(
#        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
#    assert almost_equal(
#        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
#    assert almost_equal(
#        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"

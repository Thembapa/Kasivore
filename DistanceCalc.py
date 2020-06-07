from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km

def estimatedDistance (_lat1,_lon1,_lat2,_lon2 ):
    R = 6378.0

    lat1 = radians(_lat1)
    lon1 = radians(_lon1)
    lat2 = radians(_lat2)
    lon2 = radians(_lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance
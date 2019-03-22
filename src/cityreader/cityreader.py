import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"({self.name}, {self.lat},{self.lon})"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list

    with open('cities.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            if line == 0:
                line += 1
            else:
                cities.append(City(row[0], float(row[3]), float(row[4])))

        return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

cmd = input('Enter in 2 latitude and longitude values with a space in between each value in the following format - (lat1 lon1 lat2 lon2):')
cmd = cmd.split()

min_lat = None
min_lon = None
max_lat = None
max_lon = None

if len(cmd) != 4 and int(cmd[0]) != True and int(cmd[1]) != True and int(cmd[2]) != True and int(cmd[3]) != True:
    cmd = input(
        'Please enter in a lattitude and longitude in the correct format:')
else:
    if int(cmd[0]) < int(cmd[2]):
        min_lat = float(cmd[0])
        max_lat = float(cmd[2])
    else:
        min_lat = float(cmd[2])
        max_lat = float(cmd[0])

    if int(cmd[1]) < int(cmd[3]):
        min_lon = float(cmd[1])
        max_lon = float(cmd[3])
    else:
        min_lon = float(cmd[3])
        max_lon = float(cmd[1])


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    if float(lat1) < float(lat2):
        min_lat = float(lat1)
        max_lat = float(lat2)
    else:
        min_lat = float(lat2)
        max_lat = float(lat1)

    if float(lon1) < float(lon2):
        min_lon = float(lon1)
        max_lon = float(lon2)
    else:
        min_lon = float(lon2)
        max_lon = float(lon1)

    # TODO Ensure that the lat and lon values are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.

    for i in cities:
        if min_lat <= i.lat <= max_lat and min_lon <= i.lon <= max_lon:
            within.append(i)
        else:
            continue

    return within

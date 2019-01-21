"""
The Problem:
Write a function that has three parameters:

a restaurant file that is open for reading,
the price range (one of $, $$, $$$ and $$$$), and
a list of cuisines.
The function returns a list of restaurants (in that price range, serving at least one of those cuisines),
and their ratings sorted from highest to lowest.

read in the whole file using readlines => list
''.join(the list above) then split by '\n\n'
feed each bit into a Restaurant constructor
"""


class Restaurant:
    def __init__(self, *args):
        if len(args) != 4:
            raise Exception(f'expecting restaurant name, rating, price and cuisines but got {len(args)} args instead')
        self.name, self.rating, self.price, self.cuisines_str = args
        self.cuisines = set(self.cuisines_str.split(','))

    def __repr__(self):
        return ','.join([self.name, self.rating, self.price, self.cuisines_str]) + '\n'

    def __eq__(self, other):
        return self.name == other.name and \
                self.rating == other.rating and \
                self.price == other.price and \
                self.cuisines == other.cuisines

    @staticmethod
    def percentage2float(x: str):
        return float(x.strip('%')) / 100

    def __gt__(self, other):
        return self.percentage2float(self.rating) > self.percentage2float(other.rating)


def recommend(filepath: str, price_range: str, cuisines: [str]):
    with open(filepath) as fo:
        filecontent = ''.join(fo.readlines())
        each_restaurant = filecontent.split('\n\n')
        restaurants = []
        for restaurant in each_restaurant:
            restaurants.append(Restaurant(*restaurant.strip('\n').split('\n')))
        restaurants = filter(lambda r: r.price == price_range, restaurants)
        restaurants = filter(lambda r: set(r.cuisines).intersection(set(cuisines)), restaurants)
        return sorted(list(restaurants), reverse=True)

# print(recommend('./restaurants_small.txt', '$', ['Chinese']))
# print(recommend('./restaurants_small.txt', '$', ['Chinese', 'Thai']))

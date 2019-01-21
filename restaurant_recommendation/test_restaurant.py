from restaurant_recommendation.restaurant import recommend, Restaurant


def test_init():
    r = Restaurant('Henry\'s', '100%', '$$', 'Chinese')
    assert r.name == 'Henry\'s'
    assert r.rating == '100%'
    assert r.price == '$$'
    assert r.cuisines == {'Chinese'}


def test_recommend_a():
    assert recommend('./restaurant_recommendation/restaurants_small.txt', '$', ['Chinese']) == \
           [Restaurant('Dumplings R Us', '71%', '$', 'Chinese')]


def test_recommend_b():
    assert recommend('./restaurant_recommendation/restaurants_small.txt', '$', ['Chinese', 'Thai']) == \
           [Restaurant('Queen St. Cafe', '82%', '$', 'Malaysian,Thai'),
            Restaurant('Dumplings R Us', '71%', '$', 'Chinese')]

from scifinames.star_wars import star_wars_data, star_wars_name

def test_star_wars_name_returns_title_from_data():
    response = star_wars_name()
    title = response.split(response)[0]
    assert(title in star_wars_data["title"])


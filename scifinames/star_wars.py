from random import choice

star_wars_data = {
    "first_name": [
        "Aambler",
        "Aban",
        "Bafor",
        "Ballax",
    ],
    "second_name": [
        "Aloo",
        "Alozen",
        "Bada",
        "Bakarn",
        "Kelo",
        "Skywalker",
        "Tano"
    ],
    "title": [
        "Jedi Padawan ",
        "Jedi Knight ",
        "Jedi Master ",
        "Private ",
        "Captain ",
        "Admiral ",
        "Bounty Hunter ",
        "Senator ",
        ""
    ]
}


def _title():
    return choice(star_wars_data["title"])


def _first_name():
    return choice(star_wars_data["first_name"])


def _second_name_prefix():
    return choice([" ", "-"])


def _second_name():
    return choice(star_wars_data["second_name"])


def star_wars_name():
    return _title() + _first_name() + _second_name_prefix() + _second_name()


from models.marvel_character import MarvelCharater

marvel_characters_db = {}

marvel_characters = [
    {
        "name": "Kang",
        "alias": "Kang the Conqueror",
        "real_name": "Nathaniel Richards",
        "short_bio": "Kang the Conqueror is a time-traveling warlord who has battled many heroes, especially the Avengers. He is known for his mastery of advanced technology and his ability to manipulate time.",
        "first_appearance": 1964,
        "is_villian": True,
        "image_url": "http://localhost:8005/images/kang.png"
    },
    {
        "name": "Hulk",
        "alias": "The Hulk",
        "real_name": "Bruce Banner",
        "short_bio": "Hulk is a gamma-powered superhero with incredible strength and durability. He transforms into a green giant when angered or stressed.",
        "first_appearance": 1962,
        "image_url": "http://localhost:8005/images/hulk.png"
    },
    {
        "name": "Black Widow",
        "alias": "Natasha Romanoff",
        "real_name": "Natasha Romanoff",
        "short_bio": "Black Widow is a highly trained spy and former assassin with exceptional skills in hand-to-hand combat and espionage.",
        "first_appearance": 1964,
        "image_url": "http://localhost:8005/images/black_widow.png"
    },
    {
        "name": "Black Cat",
        "alias": "Felicia Hardy",
        "real_name": "Felicia Hardy",
        "short_bio": "Black Cat is a skilled burglar with a unique power that brings bad luck to her enemies. She often operates in the gray area between hero and villain.",
        "first_appearance": 1979,
        "is_villian": True,
        "image_url": "http://localhost:8005/images/black_cat.png"
    },
]


marvel_characters_db = {character['name'].lower(): MarvelCharater(**character) for character in marvel_characters}


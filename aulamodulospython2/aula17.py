# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
from pprint import pprint
from typing import TypedDict


string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

filme = json.loads(string_json)
pprint(filme)
print(filme['title'])


print('*'*20)


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


filme2: Movie = json.loads(string_json)
pprint(filme2, width=40)
print(filme2['title'])
print(filme2['characters'][0])
print(filme2['year'] + 10)
json_string = json.dumps(filme2, ensure_ascii=False, indent=2)
print(json_string)

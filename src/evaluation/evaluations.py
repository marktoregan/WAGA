from collections import namedtuple
from src.calc import distance as dis
from src.calc import  normalize as nl

ennis = nl.Normalize(latitude=52.847054, longitude=-8.988436)
print(f' ennis {ennis.x} {ennis.y}')

sligo = nl.Normalize(latitude=54.26969, longitude=-8.46943)
print(f' sligo {sligo.x} {sligo.y}')

dublin_city = nl.Normalize(latitude=53.338313, longitude=-6.238713)
print(f'dublin {dublin_city.x} {dublin_city.y}')
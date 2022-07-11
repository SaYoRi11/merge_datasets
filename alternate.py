import difflib
from datasets import dict_1, dict_2

final = []
districts_2 = [d['District'] for d in dict_2]

for x in dict_1:
    match = difflib.get_close_matches(x['District'], districts_2)[0]
    y_index = districts_2.index(match)
    y = dict_2[y_index]
    final.append({**x, **y})

print(final)
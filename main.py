from datasets import dict_1, dict_2

dict_1 = sorted(dict_1, key = lambda x:x["District"])
dict_2 = sorted(dict_2, key = lambda x:x["District"])

final = []
for x in list(zip(dict_1, dict_2)):
    final.append({**x[0], **x[1]})

print(final)
dict_1 = [{
    "District": "Kathmandu",
    "KPI_1": .8
},
{
    "District": "Dhanusha",
    "KPI_1": .85
},
{
    "District": "Kavrepalanchok",
    "KPI_1": .75
}
]

dict_2 = [{
    "District": "Kathmandu",
    "KPI_2": .35
},
{
    "District": "Kavrepalanchok",
    "KPI_2": .65
},
{
    "District": "Dhanusha",
    "KPI_2": .6
}
]

dict_1 = sorted(dict_1, key = lambda x:x["District"])
dict_2 = sorted(dict_2, key = lambda x:x["District"])

new = []
for x in list(zip(dict_1, dict_2)):
    new.append({**x[0], **x[1]})

print(new)
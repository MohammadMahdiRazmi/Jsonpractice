import json
place1={"province":"Hormozgan",
        "city":"bandar abbas",
        "yy":2023,"mm":10,
        "dd":24,
        "hh":11,
        "mm":17,
        "ss":51,
        "Richter":4.1
}
loads_place1=json.dumps(place1)
print(loads_place1)
print("*******************************")
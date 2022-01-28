
def direction(facing: str, turn: int):
    compass = {"N": 0,
               "NE": 45,
               "E": 90,
               "SE": 135,
               "S": 180,
               "SW": 225,
               "W": 270,
               "NW": 315,
               }
    if facing not in compass or type(turn) != int or turn % 45 != 0:
        print(f'Please, input correct data')
    else:
        result = (compass[facing] + turn) % 360
        for k, v in compass.items():
            if v == result:
                return k

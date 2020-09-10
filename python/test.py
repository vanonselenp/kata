locked = [
    [False, False, False],
    [False, False, False],
    [False, False, False]
]

preferences = [
    [0, 3, 1],
    [1, 0, 2],
    [2, 1, 0]
]

pairs = [
    { "winner": 0, "loser": 1 },
    { "winner": 2, "loser": 0 },
    { "winner": 1, "loser": 2 },
]

def is_circle(winner, loser, index, looking):
    circle = False
    
    for i in range(index -1, -1, -1):
        current = pairs[i]
        # potential link
        if current["winner"] == loser:
            print(current, looking)
            if current["loser"] == looking:
                return True
            circle = is_circle(current["winner"], current["loser"], i, looking)

    return circle

def lock_pairs():
    index = 0
    for pair in pairs:
        if (not is_circle(pair["winner"], pair["loser"], index, pair["winner"])):
            print("adding")
            locked[pair["winner"]][pair["loser"]] = True
        index += 1

    print(locked)

lock_pairs()
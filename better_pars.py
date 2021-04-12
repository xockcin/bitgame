size = 16

def make_row(i):
    row = []
    for j in range(size):
        row.append({"origin" : i, "goal" : j, "solved": False, "steps": ""})
    return row

def make_square():
    pairs = []
    for i in range(size):
        pairs.append(make_row(i))
    return pairs

def doToken(token, origin):
    if token == "+":
        return (origin + 1) % size
    if token == "<":
        return (origin * 2) % size
    if token == "~":
        return size - 1 - origin
    if token == ">":
        return int(origin / 2)
    if token == "-":
        return (origin - 1) % size

def doAllTokens(origin):
	tokens = ["~","<",">","+","-"]
	result = []
	for token in tokens:
		result.append(doToken(token, origin))
	return result

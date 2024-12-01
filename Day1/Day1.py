def getDistance(filename: str):
    total = 0
    similarity = 0
    simMap = {}
    left = []
    right = []
    with open(filename, 'r') as f:
        for line in f:
            tokens = line.strip().split()
            left.append(tokens[0])
            right.append(tokens[1])
            simMap[tokens[1]] = 1 + simMap.get(tokens[1], 0) 

    left.sort()
    right.sort()

    while left:
        rightNum = int(right.pop(0))
        leftNum = int(left.pop(0))
        addition = abs(rightNum - leftNum)
        if str(leftNum) in simMap:
            similarity += leftNum*simMap[str(leftNum)]
        total += addition

    return total, similarity

print(getDistance('Day1\Day1Ex.txt'))
print(getDistance('Day1\Day1Input.txt'))
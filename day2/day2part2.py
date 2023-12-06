file1 = open('smalltext.txt', 'r')
lines = file1.readlines()
result = {"red":0, "green":0, "blue":0}

sum = 0
for row in lines:
    canAdd = False
    game = row.split(": ")
    number = game[0].replace(":", "").split(" ")[1]
    text = game[1].split("; ")
    for t in text: 
        cubeSet = t.split(", ")
        for cube in cubeSet: 
            data = cube.split(" ")
            if result[data[1].strip()]<=int(data[0]): 
                result.update({data[1].strip():int(data[0])})   
    total = result["red"]*result["green"]*result["blue"]
    sum+=total
    result = {"red":0, "green":0, "blue":0}
print(sum)
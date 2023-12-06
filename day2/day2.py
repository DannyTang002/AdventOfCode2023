file1 = open('smalltext.txt', 'r')
lines = file1.readlines()

colors = {"red":12, "green": 13, "blue":14}
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
    if(result["red"]<=colors["red"] and result["green"]<=colors["green"] and result["blue"]<=colors["blue"]):
        print(number)
        sum+=int(number)
    #print(result)
    result = {"red":0, "green":0, "blue":0}
print(sum)
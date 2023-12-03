file1 = open('smalltext2.txt', 'r')
lines = file1.readlines()

listOfNumbers = {"zero":"0", "one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

sum = 0

found = False 
for row in lines:
    number = []
    allChars = ""
    for char in row:
        allChars+=char
        if char.isdigit():
            number+=char
            allChars = ""
        for numbers in listOfNumbers:
            if numbers in allChars:
                number+=listOfNumbers[numbers]
                allChars=allChars[-1]

    print(number)
    num = number[0]+number[-1]
    print(num)
    sum += int(num)

    
    
    

print(sum)
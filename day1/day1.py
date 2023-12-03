file1 = open('smalltext.txt', 'r')
lines = file1.readlines()

list = []
sum = 0

for row in lines:
    number = ""
    for char in row:
        if char.isdigit():
            number+=char 
            break 
    original_string = row
    reversed_string = ''.join(reversed(original_string))
    for char in reversed_string:
        if char.isdigit():
            number+=char 
            break 

    print(number)    
    sum+=int(number)

print(sum)
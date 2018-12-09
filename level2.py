
input = open('input_2.txt').read().splitlines()

def twice_trice(obj):
    twice = False
    trice = False
    for key in obj:
        if obj[key] == 2:
            twice = True
        if obj[key] == 3:
            trice = True
    return [twice,trice]

def histogram(text):
    result = {}
    for i in text:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

twice = 0
trice = 0

for line in input:
    result = twice_trice(histogram(line))
    if result[0] == True:
        twice += 1
    if result[1] == True:
        trice += 1

print(f'Twice ={twice}')
print(f'Trice ={trice}')
print(f'Check Sum ={twice * trice}')

correct = []
for line in input:
    result = twice_trice(histogram(line))
    if result[0] == True or result[1] == True:
        correct.append(line)

for text1 in correct:
    reference = correct
    reference.remove(text1)
    for text2 in reference:
        error = 0
        for index,char in enumerate(text1):
            if text2[index] != char:
                error += 1
            if error > 1:
                break
        else:
            for index,char in enumerate(text1):
                if text2[index] == char:
                    print(char,end='')    
            print('')      
            




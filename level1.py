import Stopwatch

Stopwatch.start()
input = open('input_1.txt').read().splitlines()
result = 0
result_list = []
found = False
while found == False:
    for i in input:
        result += int(i)
        if result in result_list:
            print(f'Found: {result}')
            found = True
            break
        result_list.append(result)
Stopwatch.stop()
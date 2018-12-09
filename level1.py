
input = open('pep.txt').read().splitlines()
result = 0
result_list = []
while True:
    for i in input:
        result += int(i)
        if result in result_list:
            exit(f'found {result}')
        result_list.append(result)
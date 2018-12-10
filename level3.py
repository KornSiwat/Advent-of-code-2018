import time
start_time = time.time()

def return_max(list,index):
    count = []
    for elem in list:
        count.append(elem[index])
    return max(count)
    
file = open('input_3.txt' , 'r')
raw = file.read().splitlines()
file.close()
raw = [x.split(' ') for x in raw]
for line in raw:
    line[2] = line[2][:-1]
    del line[0:2]
position_list = [x[0].split(',') for x in raw]
for position in position_list:
    position[0] = int(position[0])
    position[1] = int(position[1])
size_list = [x[1].split('x') for x in raw]
for size in size_list:
    size[0] = int(size[0])
    size[1] = int(size[1])
field = []
for row in range(return_max(position_list,1) + return_max(size_list,1) + 1):
    field.append([])
    for column in range(return_max(position_list,0) + return_max(size_list,0) + 1):
        field[row].append(0)    

overlap = 0
for position,size in zip(position_list,size_list):
        for x in range(1,size[0]+1):
            for y in range(1,size[1]+1):
                if field[position[1]+y][position[0]+x] == 0:
                    field[position[1]+y][position[0]+x] = 1
                elif field[position[1]+y][position[0]+x] == 1:
                    overlap += 1
                    field[position[1]+y][position[0]+x] = 2
                elif field[position[1]+y][position[0]+x] == 2:
                    pass
                else:
                    exit('Error')

print(f'Overlap Position = {overlap}')
print(f'Runtime: {time.time()-start_time}')
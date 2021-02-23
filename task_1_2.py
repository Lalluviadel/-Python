list_cubes = []
num = 1
while num < 1000:
    list_cubes.append(num**3)
    num += 2

list_sum = 0
for member in list_cubes:
    mem_sum = 0
    mem_hold = member
    while member > 0:
        mem_sum += member % 10
        member //= 10
    if mem_sum % 7 == 0:
        print(mem_hold)
        print(mem_sum)
        list_sum += mem_hold
print(list_sum)  # 17485588610

for additive in range(len(list_cubes)):
    list_cubes[additive] += 17

list_sum = 0
for member in list_cubes:
    mem_sum = 0
    mem_hold = member
    while member > 0:
        mem_sum += member % 10  #
        member //= 10
    if mem_sum % 7 == 0:
        list_sum += mem_hold
print(list_sum)  # 15392909930

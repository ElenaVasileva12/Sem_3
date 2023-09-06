# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

import random

data=[random.randint(0,10) for i in range(10)]
data_new=[]
print(data)
for i in data:
    if data.count(i)>=2:
        data_new.append(i)
print(list(set(data_new)))



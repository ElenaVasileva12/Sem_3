
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# ✔ *Верните все возможные варианты комплектации рюкзака.

things_backpack={
    'jacket': 10,
    'down': 5,
    'ket': 3,
    'shoes': 15,
    'jackets': 12,
    'jeans': 11,
    'tights': 7,
    'sneakers': 3,
    'cap': 2,
    'fur': 6,
    'coat': 1
}
max_backpack=int(input('Введите максимальную грузоподъемность рюкзака: '))

if max_backpack>sum(things_backpack.values()):
    print('В рюкзак вместятся все вещи')
else:
    a=[]
    while max_backpack>0:
        s=min(things_backpack, key=lambda x:(things_backpack[x]-max_backpack)>0) #нашли подходящий элемент
        a.append(s)
        d=things_backpack.get(s)
        #print(d)
        max_backpack=max_backpack-d # type: ignore #вычли из рюкзака элемент
        things_backpack.pop(s) #удалили элемент, который уже в рюкзаке
    print(f'В рюкзак вместятся следующие вещи: {a}')




    






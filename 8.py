# Три друга взяли вещи в поход.
# Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. 
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует

# ✔ Для решения используйте операции с множествами. 
# Код должен расширяться на любое большее количество друзей.

friends={
    'Max': ('notepad','pen','pensil'),
    'Nik': ('jeans','jacket','shoes','coat','cap','pen'),
    'Vova': ('hairbrush','rubber','pen','brush'),
    }

inter_friends=set(friends['Max']) & set(friends['Nik']) & set(friends['Vova'])
dif_friends=set(friends['Max']) ^ set(friends['Nik']) ^ set(friends['Vova'])
union_friends=(set(friends['Max']) | set(friends['Nik']) | set(friends['Vova']))- set(friends['Max']),(set(friends['Max']) | set(friends['Nik']) | set(friends['Vova']))- set(friends['Nik']),(set(friends['Max']) | set(friends['Nik']) | set(friends['Vova']))- set(friends['Vova'])

print(inter_friends)
print(dif_friends)
print(union_friends)

    






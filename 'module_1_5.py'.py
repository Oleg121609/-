immutable_var = (1, 2, "car", True)
print(immutable_var)
#immutable_var[0] = 3 #Кортеж не поодерживать обращение по элементам
mutable_list = [3,"Любит", 5, 6, "Играть"]
mutable_list[0] = 5
mutable_list[1] = "Хорошо"
mutable_list[4] = 10
print(mutable_list)


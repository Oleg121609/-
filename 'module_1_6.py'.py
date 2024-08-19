my_dict = {"Roman": 2004, "Misha": 1999, "Kostya": 1995}
print(my_dict)
print(my_dict["Kostya"])
print(my_dict.get("Nastya"))
my_dict.update({"Ilya": 1992, "Zhenya": 1995})
a = my_dict.pop("Misha")
print(a)
print(my_dict)
my_set = {1, 4 , 5 , 1.6 , 1,7 , "well"}
print(my_set)
my_set.update({8 , 10 ,12})
my_set.discard(1.6)
print(my_set)




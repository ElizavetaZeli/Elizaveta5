immutable_var = 1, 2, 3.5, "Urban", False
print(immutable_var)
print("Кортежи не изменяемы (immutable) с перевода - неизменный")
mutable_list = [1, 2, 3.5, "Urban", False]
mutable_list[0] = 11
mutable_list[2] = 3.8
mutable_list[3] = "Summer"
mutable_list.append("Univercity")
print(mutable_list)

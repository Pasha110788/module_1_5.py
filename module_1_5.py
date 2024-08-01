immutable_var = 1,2,3,"True","Orange"
print(immutable_var)
# immutable_var[0] = 5  ошибка,нельзя изменять элемент кортежа
mutable_list = ["True","Orange",1,2,3]
mutable_list[1] = "Apple"
print(mutable_list)

# my_list = []
# for i in range(3):
#     item = float(input("please enter your number: "))
#     new_item = "item_" + str(i+1)+" is: " + str(item)
#     my_list.append(new_item)
# print(my_list)

new_list = ["item_" + str(i+1)+" is: " + str(float(input("please enter your number: "))) for i in range(3)]
print(new_list)
# List methods 1
basket = [1,2,3,4,5]
print(len(basket))

#adding
new_list = basket.append(100)
print(new_list) #prints None
print(basket) #[1, 2, 3, 4, 5, 100]
#append is just adding a number
#basket.append(100) and then assign to new_list

basket.insert(2, 200)
print(basket) # adding 200 in the 2nd index

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

basket.extend([100,1001])
new_list2 = basket
print(basket)

#removing
basket.pop() #pops the last item
print(basket)

#basket.pop(0) removing 0 index item
basket.remove(100)
print(basket)

basket.clear() #clears everything from list
print(basket)

print(basket.index(3)) #check the index of value 3
print(3 in basket) #True
print(basket.count(3)) #how many times 3 appears in the list

basket = ['a', 'x','b', 'c', 'd', 'e', 'd' ]
print(sorted(basket))
basket.sort()
print(basket)
#both moethonds prints the same ['a', 'b', 'c', 'd', 'd', 'e', 'x']
#sort does not produce a new list, but sorted produce!!
basket.reverse() #switches the indexies
print(basket)

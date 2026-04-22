

#Exercise 1
my_fav_numbers={2,6,33,8,3,9}
print(my_fav_numbers)
my_fav_numbers.update([12,45])
print(my_fav_numbers)
my_fav_numbers.remove(45)
print(my_fav_numbers)
friend_fav_numbers={2,5,31}
print(friend_fav_numbers)
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)



#Exercise 2
my_tuple=('kaoutar', 23, 38)
print(my_tuple)



#Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("kiwi")
print(basket)
basket.insert(0,"Apples")
print(basket)
basket.count("Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)


#Exercise 4
my_list=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(my_list)
import numpy as np 
my_list=list(np.arange(1,5,0.5))
print(my_list)  



#Exercise 5
#1
for i in range(20):
    print(i+1)
#2    
for i in range(20):
    if(i%2==0):
        print(i+1)  

         
#Exercise 6
user_name=input('give your name please')
while user_name.isdigit() or len(user_name)<3 :
    user_name=input('give your name please respecting not digits and at least 3 letters long')
print(' thank you') 


#Exercise 7
fruits=input('give your favorite fruits').split()
print(fruits)
fruit=input('give a fruit name')
if fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else :
    print("You chose a new fruit. I hope you enjoy it!")




#Exercise 8
pizza_price=10
topping_price=2.5
toppings=[]
while True:
    topping=input('enter pizza topping')
    if topping.lower()=="quit":
        break
    toppings.append(topping)
    print( "Adding"+ topping+ "to your pizza.")
    pizza_price+=topping_price
    print(pizza_price)
print("your piza toppings are "+ str(toppings))
print("the total cost of the pizza is " + str(pizza_price))




#Exercise 9
family_nbr=int(input('give your family number'))
total_cost=0
for i in range(family_nbr):    
    age=int(input('give the '+str(i+1)+' member age'))    
    if age < 3:
        total_cost+=0        
    elif age > 3 and age <= 12: 
        total_cost+=10
    else:
        total_cost+=15   
print('your tickets total cost is '+ str(total_cost)) 
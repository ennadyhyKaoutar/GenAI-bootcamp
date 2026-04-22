#Exercise 1
def display_message():
    print('I am learning about functions in Python.')
display_message()  


#Exercise 2

def favorite_book(title):
    print('One of my favorite books is',title)
favorite_book("Alice in Wonderland")    


#Exercise 3
def describe_city(city, country="Unknown"):
    print(city ,'is in',country) 
describe_city("Reykjavik", "Iceland")
describe_city("Paris")


#Exercise 4
import random
def random_funct(number):
    if number >=1 and number <=100:
        random_number=random.randint(1, 100)
        if number==random_number:
            print('success')
        print('fail Your number:',number,'Random number:',random_number)
    else:
        print('number should be between 1 and 100.')
random_funct(20) 


#Exercise 5

def make_shirt(size='large', text='I love Python'):
    print('The size of the shirt is', size,' and the text is' , text)
make_shirt()  
make_shirt('meduim')
make_shirt(text='i love java')

#Exercise 6
magician_names=['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
    for name in magician_names:
        print('magician name is' , name)
show_magicians(magician_names) 

def make_great(magician_names):
    for index in range(len(magician_names)):
        magician_names[index]= 'the great '+ magician_names[index]
        

make_great(magician_names)
show_magicians(magician_names)


#Exercise 7
#with  randint
import random
def get_random_temp():
    return random.randint(-10, 40)
get_random_temp() 
def main():
    random_temp=get_random_temp()
    print('The temperature right now is', random_temp, ' degrees Celsius.')
    if random_temp==0:
        print('Brrr, that’s freezing! Wear some extra layers today.')
    elif random_temp>0 and random_temp<=16:
        print('Quite chilly! Don’t forget your coat.')
    elif random_temp>16 and random_temp<=23:
        print('Nice weather.') 
    elif random_temp>=24 and random_temp<=32:
        print('A bit warm, stay hydrated.') 
    elif random_temp>32 and random_temp<=40:
        print('It’s really hot! Stay cool.')    
main()  

#with random unifrome
import random
def get_random_temp_uniform():
    return random.uniform(-10, 40)
get_random_temp()    
def main():
    random_temp=get_random_temp_uniform()
    print('The temperature right now is', random_temp, ' degrees Celsius.')
    if random_temp==0:
        print('Brrr, that’s freezing! Wear some extra layers today.')
    elif random_temp>0 and random_temp<=16:
        print('Quite chilly! Don’t forget your coat.')
    elif random_temp>16 and random_temp<=23:
        print('Nice weather.') 
    elif random_temp>=24 and random_temp<=32:
        print('A bit warm, stay hydrated.') 
    elif random_temp>32 and random_temp<=40:
        print('It’s really hot! Stay cool.')    
main()  

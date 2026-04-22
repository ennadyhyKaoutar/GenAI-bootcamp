
#Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary=dict(zip(keys,values))
print(dictionary)


#Exercise 2
family_nbr=int(input('give your family number'))
total_cost=0
family_dict={}
for i in range(family_nbr): 
    name=input('give the '+str(i+1)+' member name')
    age=int(input('give the '+str(i+1)+' member age'))  
    family_dict[name]=age
    if age < 3:
        total_cost+=0  
        print('ticket cost for '+ name+'is 0')
    elif age >= 3 and age <= 12: 
        total_cost+=10
        print('ticket cost for '+ name+'is 10')
    else:
        total_cost+=15  
        print('ticket cost for '+ name+'is 15')
print('your tickets total cost is '+ str(total_cost))  
    

#Exercise 3

brand={'name': 'Zara', 
'creation_date': 1975,
'creator_name': 'Amancio Ortega Gaona',
'type_of_clothes': ['men', 'women', 'children', 'home'],
'international_competitors': ['Gap', 'H&M', 'Benetton'],
'number_stores': 7000,
'major_color': 
    {'France': 'blue', 
    'Spain': 'red', 
    'US': ['pink', 'green']}}
brand
brand['number_stores']=2
brand
print('zara brand represent different types of clothes ', brand['type_of_clothes'])
brand
brand['country_creation']='spain' 
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
print(brand['international_competitors'][-1])    
del brand['creation_date']
brand
print(brand['major_color'])
print(brand['major_color']['US'])
len(brand)
brand.keys()




#Exercise 4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
dict_1=dict(enumerate(users))
print(dict_1)
dict_2={}
for index , character in enumerate(users):
    dict_2[character]=index
print(dict_2)   
dict_3={}
users.sort()
for index , character in enumerate(users):
    dict_3[character]=index
print(dict_3)
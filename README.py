# PythonLearning
value=123 #int
value1="123" #str
value2=123.0 #float

print(type(value))
print(type(value1))
print(type(value2))


word= "planets"

print(word[0])   #p
print(word[1])   #l
print(word[-1])  #s    #count in reserve
print(word[-2])  #t  
print(word[0:2])   #pl  #0 dan baslayarak 2 tanesini dilimle
print(word[0:-1])  #planet
print(word[1:3])   #la  #1 den baslayarak 3 tanesini dilimle
print(word[2:5])   #ane

print(word.upper())  #PLANETS
print(word.lower())  #planets

a = 15
b = 10
result = f"{a} + {b} = {a + b}"
print(result)        #15+10=25

num_float= 15.7
num_int = int(num_float)
print(num_int,type(num_int))  #15

graduated= "nny univercity"
year=2023
print("my name is aleyna",graduated,"and in kayseri",year) #my name is aleyna nny univercity and in kayseri 2023

#break ve continue ifadeleri

for num in range(1, 7):
    if num == 3:
        continue 
    print(num) #iterasyonu atla #1 2 4 5 6 7 

for num in range(1, 7):
    if num == 3:
        break 
    print(num) #döngüden çık #1 2 

n = 10
if n > 5:
    pass #yer tutucu 

# PythonLearning

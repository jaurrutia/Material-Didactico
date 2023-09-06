# 2022/02/17

print("saludame muchas veces")

str1 = "Hola.\n¿Cómo estás?"
str2 = 'Hola.\n¿Cómo estás?-simple'
str3 = '''Hola
¿Cómo estas?-tres'''
str4 = "What \"Hola\"  "
str5 ='Hola\'s'
print(type(str5))
i = 0   # Contador
list = [str1, str2, str3 , str4, str5]
print(type(list))

while i < 5:
	print(list[i])
	i += 1  # Aumentamos el conatdor

str6 = '\U0001F436'
print(str6)

str7 = "Hola\n"
str8 = '¿Cómo estás?'

print( str7 + str8 )

s_dog =  '\U0001F436'
num = '0123456789'

print(s_dog + num)
print( ord(s_dog))
print( int(num))


print( ord(num[1])) 
print( int(num[1]))

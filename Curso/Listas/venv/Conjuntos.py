conjunto=set()
conjunto={1,2,4,'hola'}
conjunto.add('liz <3')
print(conjunto)
print('liz <3' in conjunto)
print('liz <3' not in conjunto)

conjunto.discard('liz <3')
print(conjunto)
print('liz <3' not in conjunto)
print('liz <3' in conjunto)

conjunto.clear()
print(conjunto)


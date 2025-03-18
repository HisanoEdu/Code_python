import matplotlib.pyplot as plt

a=(1,2,3,4,5)
b=(1,2,3,4,5)
plt.plot(a,b)

plt.ylabel(u'Alguns Números y')
plt.xlabel (u'Alguns Números x')

x=(0,1,2,3,4,5,6)
y=(0,1,2,3,4,5,6)
plt.xlabel ('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Meu gráfico')
plt.plot(x,y)

# plt.plot((1,2,3,4), (1,4,9,16),'ro')

# plt.plot((1,2,3,4), (1,4,9,16),'mD:')

# plt.plot((1,2,3,4), (1,4,9,16),'mD:')
# plt.axis((0,6,0,20))

# plt.grid(True)

# a=(1,2,3,4,5)
# b=(1,2,3,4,5)
# d=(2,2,5,4,5)
# e=(2,4,3,4,5)

# plt.subplot(1,2,1)
# plt.plot(a,b)

# plt.subplot(1,2,2)
# plt.plot(d,e)

# a=(1,2,3,4,5,6)
# b=(2,4,6,8,10,12)

# plt.scatter(a,b)

a=(1,2,3,4,5,6)
b=(2,4,6,8,10,12)

plt.bar(a,b)

a=(1,2,3,4,5,6)
b=(2,4,6,8,10,12)

plt.hist(a,b)

a=(10,20,30)
explode=(0.1,0,0)
labels=["HB20","Gol","Fusca"]
plt.pie(a, explode=explode,
labels=labels,autopct='%.2f% %', shadow=True)
plt.title("Meu gráfico")
plt.grid(True)
plt.show()


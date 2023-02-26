# 1. Variables and Operators 
# 
# 
print("1. Variables and Operators\n")

a = 123
b = 'abc'
c = '123abc'
d = 123 + 1
e = a+d 

print(123+456)
# modulo %
# pangkat **

print('\n\n')
# 2. Data Structures
# 
# 
print("2. Data Structures\n")

arr = [1,2,"abc"]
dic = {}

dic['kunci'] = 3
dic[1] = "abc"

arr.append(4)

print(arr)

print('\n\n')

# 3. Iterations
#
#
print('3. Iterations\n')

array_baru = []
print(array_baru)
for i in range(1,5):
    array_baru.append(i**2)
    array_baru[i-1]-=1

print(array_baru)

for i in [1,2,3,4,5]:
    print(i)

flag= 0
while flag<5:
    print("Flag = ",flag)
    flag+=1

print('\n\n')
# 4. Functions
#
#
print('4. Functions\n')

from utils import akar

hasil = akar(225)
print(hasil)

print('\n\n')
# 5. Classes
#
#
print ('5. Classes\n')

from Kelas import Buku

buku1 = Buku("Buku Satu",1000)
print(buku1.nama)






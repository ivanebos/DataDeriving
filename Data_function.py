
import math

inp = input()

array = inp.split(" ")
group = [0,0,0,0,0,0]
new_array = []
array.sort()

for i in array:
    new_array.append(int(i))
    
    
print(array)

def sor(arr):
    arr.sort()
    print(arr)

def freq(arr):
    for j in arr:
        i = int(j)
        if i >= 0 and i <= 50:
            group[0] += 1
            
        elif i >= 51 and i <= 60:
            group[1] += 1

        elif i >= 61 and i <= 70:
            group[2] += 1

        elif i >= 71 and i <= 80:
            group[3] += 1

        elif i >= 81 and i <= 90:
            group[4] += 1

        elif i >= 91 and i <= 100:
            group[5] += 1

    print(group)



def median(arr):
    if len(arr) % 2 == 0:
        med = (arr[int(len(arr)/2-1)] + arr[int(len(arr)/2)])/2
        print(med)

    else:
        med = arr[int((len(arr)-1)/2)]
        print(med)


        
def mean(arr):
    total = 0
    for i in arr:
        total += i

    print(total/len(arr))


def stand_dev(m,arr):
    total = 0
    for i in arr:
        total += (i- m)**2

    total /= len(arr)
    total = math.sqrt(total)
    print(total)



    

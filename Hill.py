
def calCost(arr, n):
    cost = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                cost = cost + 1
    return cost                

def swaparrelements(arr, p, q):
    arr[p],arr[q] = arr[q], arr[p]

if __name__=='__main__':
    
    n = int(input('Enter the number of cities : '))
    
    arr = []
    for i in range(0,n):
        print('Enter the distance of city {}:'.format(i), end = '')
        arr.append(int(input()))
    
    bestcost = calCost(arr, n)
    newcost = 0
    noofswap = 0
    
    while(bestcost > 0):
        
        for i in range(0, n - 1):
            swaparrelements(arr, i, i + 1)
            newcost = calCost(arr, n)
            
            if(newcost < bestcost):
                noofswap = noofswap + 1
                bestcost = newcost
                #Just Printing the array
                print(arr,' Current BestCost :', bestcost)
            else:
                #cancel the swap
                swaparrelements(arr, i, i + 1)

    #Final Route :
    print('Final Minimum Distance Route : ',arr)                
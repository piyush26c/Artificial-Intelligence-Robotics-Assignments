import threading as Thread

# Sequential Merge Sort Time Complexity: O(n*log(n))
# Parallel Merge Sort Time Complexity:   O(log(n))

def mergeSort(arr): 
	if len(arr) > 1:
		mid = int(len(arr)/2) 
		lefthalf = arr[:mid] 
		righthalf = arr[mid:]
		t1 = Thread.Thread(target = mergeSort, args = (lefthalf,)) 
		t2 = Thread.Thread(target = mergeSort, args = (righthalf,)) 
		t1.start()
		t2.start() 
		t1.join()
		t2.join() 
		i = 0
		j = 0
		k = 0

		while i < len(lefthalf) and j < len(righthalf): 
			if lefthalf[i] < righthalf[j]:
				arr[k]=lefthalf[i] 
				i = i + 1
				k = k + 1
			else:
				arr[k] = righthalf[j] 
				j = j + 1
				k = k + 1
 
		while i < len(lefthalf): 
			arr[k]=lefthalf[i] 
			i = i + 1
			k = k + 1
            
		while j < len(righthalf): 
			arr[k] = righthalf[j] 	
			j = j + 1
			k = k + 1

arr = list(map(int,input("Enter Elements :").split())) 
n = len(arr)
mergeSort(arr)
print("Sorted elements (Parallel Merge Sort) :") 
for i in range(0, n):
	print(arr[i], end = ' ')
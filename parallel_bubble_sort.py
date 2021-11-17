from threading import Thread

# Sequential Bubble Sort Time Complexity: O(n^2)
# Parallel Bubble Sort Time Complexity:   O(n)

def swap_if_greater(arr, i, isSorted): 
	if arr[i] > arr[i + 1]:
		arr[i], arr[i + 1] = arr[i + 1], arr[i] 
		isSorted[0] = 0
	return

#odd-even Transposition sort [Time Complexity: O(n)]
def bubbleSort(arr, n): 
	isSorted = 0
	while isSorted == 0: 
		isSorted = [1, ] 
		tds = []
		for i in range(1, n - 1, 2):#odd phase
			tds.append(Thread(target = swap_if_greater, args = (arr, i, isSorted)))
		for i in tds:
			i.start() 
		for i in tds:
			i.join()
		tds=[]
		for i in range(0, n - 1, 2):#even phase
			tds.append(Thread(target = swap_if_greater, args = (arr, i, isSorted)))
		for i in tds:
			i.start() 
		for i in tds:
			i.join() 
		isSorted = isSorted[0]
	return

arr = list(map(int, input("\nEnter Elements :").split())) 
n = len(arr)
bubbleSort(arr, n)
print("\nSorted elements (Parallel Bubble Sort) :") 
for i in range(0, n):
	print(arr[i], end = ' ')
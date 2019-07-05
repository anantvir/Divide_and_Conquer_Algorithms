import insert_heap      # Import heap insert and delete from 'DataStrcutures_PriorityQueues_Heaps' repository

given_data = [15,20,30,5,10,25,35,40]

h = insert_heap.MaxHeap()
def heapsort(arr):
    result = []
    for x in range(len(arr)):
        h.insert_heap(arr[x])
    
    while len(arr) > 1:
        item = h.delete_heap()
        result.append(item._item)
    return

heapsort(given_data)

import random, time

# returns the index of the the target, returns -1 if target is not in the list
def linear_search(arr, target):
    
    for i in range(0, len(arr)): # iterate through the list and find the target
        if arr[i] == target:
            return i

    return -1

# returns the index of the target, returns -1 if target is not in the list
# requires that the inputed list be sorted
def binary_search(arr, target, low, high):

    if low > high:
        return -1
    else:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target: # target must be in the earlier half of the list
            return binary_search(arr, target, low, mid-1)
        else: # target must be in the later half of the list
            return binary_search(arr, target, mid+1, high)

# partition function for quicksort function
def partition(arr, low, high):
    pivot = arr[high]
    i = low -1

    # iterates through the list and swaps arr[j] with arr[i] if j is less
    # than the pivot, the goal is to keep incrementing i (preferably when
    # arr[i] is greater than the pivot)
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i +1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return (i+1)

# sorts an array with quick sort
def quicksort(arr, low, high):
    if len(arr) < 2:
        return arr
    
    if low < high:

        part = partition(arr, low, high)

        # the list before the index of the partition and the list after the
        # index of the partition get sorted separately
        quicksort(arr, low, part -1)
        quicksort(arr, part +1, high)


if __name__ == "__main__":

    # code for testing functions
    list1 = ["abc", "def", "ghi"]
    print(linear_search(list1, "def"))
    print(linear_search(list1, "xyz"))
    
    list2 = [23, 53, 89, 102, 212, 322]
    print(binary_search(list2, 322, 0, 5))

    list3 = [322, 212, 102, 89, 53, 23]
    quicksort(list3, 0, 5)
    print(list3)

    print("\nTesting done!\n")


    print("Testing Algorithm A and B execution speeds for ", end="")
    print("random lists of size 1000, 5000, and 10000 has begun.\n")
    # random list of size 1000
    S_n1000 = []

    for i in range(0, 1000):
        S_n1000.append(random.randrange(1,10000,2))
        # print(S_n1000[i])

    k_n1000 = 200 # constant to change
    print("The value of k for n = 1000 is ", end="")
    print(k_n1000)

    k_list_n1000 = []
    for i in range(0, k_n1000 // 2):
        k_list_n1000.append(random.randrange(2,10000,2))
        k_list_n1000.append(S_n1000[random.randint(0,1000 -1)])

    # if k is odd there will be one more value of k that is in S versus the
    # values of k that are not in S
    if k_n1000 % 2 == 1:
        k_list_n1000.append(S_n1000[(k_n1000//2)+1])

    # algorithm A - n1000
    start_time_A_n1000 = time.process_time_ns()
    # time.process_time_ns() requires Python 3.7
    
    for i in range(0, len(k_list_n1000)):
        linear_search(S_n1000, k_list_n1000[i])
        # print(linear_search(S_n1000, k_list_n1000[i]))

    end_time_A_n1000 = time.process_time_ns() - start_time_A_n1000

    print("Algorithm A takes ", end="")
    print(end_time_A_n1000, end="")
    print(" nanoseconds.")

    # algorithm B - n1000
    start_time_B_n1000 = time.process_time_ns()
    
    quicksort(S_n1000, 0, len(S_n1000) -1)
    
    for i in range(0, len(k_list_n1000)):
        binary_search(S_n1000, k_list_n1000[i], 0, len(S_n1000) -1)
        # print(binary_search(S_n1000, k_list_n1000[i], 0, len(S_n1000) -1))

    end_time_B_n1000 = time.process_time_ns() - start_time_B_n1000

    print("Algorithm B takes ", end="")
    print(end_time_B_n1000, end="")
    print(" nanoseconds.\n")


    # random list of size 5000
    S_n5000 = []

    for i in range(0, 5000):
        S_n5000.append(random.randrange(1,50000,2))
        # print(S_n5000[i])

    k_n5000 = 60 # constant to change
    print("The value of k for n = 5000 is ", end="")
    print(k_n5000)

    k_list_n5000 = []
    for i in range(0, k_n5000 // 2):
        k_list_n5000.append(random.randrange(2,50000,2))
        k_list_n5000.append(S_n5000[random.randint(0,5000 -1)])

    if k_n5000 % 2 == 1:
        k_list_n5000.append(S_n5000[(k_n5000//2)+1])

    # algorithm A - n5000
    start_time_A_n5000 = time.process_time_ns()
    
    for i in range(0, len(k_list_n5000)):
        linear_search(S_n5000, k_list_n5000[i])
        # print(linear_search(S_n5000, k_list_n5000[i]))

    end_time_A_n5000 = time.process_time_ns() - start_time_A_n5000

    print("Algorithm A takes ", end="")
    print(end_time_A_n5000, end="")
    print(" nanoseconds.")

    # algorithm B - n5000
    start_time_B_n5000 = time.process_time_ns()
    
    quicksort(S_n5000, 0, len(S_n5000) -1)
    
    for i in range(0, len(k_list_n5000)):
        binary_search(S_n5000, k_list_n5000[i], 0, len(S_n5000) -1)
        # print(binary_search(S_n5000, k_list_n5000[i], 0, len(S_n5000) -1))

    end_time_B_n5000 = time.process_time_ns() - start_time_B_n5000

    print("Algorithm B takes ", end="")
    print(end_time_B_n5000, end="")
    print(" nanoseconds.\n")


    # random list of size 10000
    list_n10000 = []

    for i in range(0, 10000):
        list_n10000.append(random.randint(1,100000))

    S_n10000 = []

    for i in range(0, 10000):
        S_n10000.append(random.randrange(1,100000,2))
        # print(S_n10000[i])

    k_n10000 = 55 # constant to change
    print("The value of k for n = 10000 is ", end="")
    print(k_n10000)

    k_list_n10000 = []
    for i in range(0, k_n10000 // 2):
        k_list_n10000.append(random.randrange(2,100000,2))
        k_list_n10000.append(S_n10000[random.randint(0,10000 -1)])

    if k_n10000 % 2 == 1:
        k_list_n10000.append(S_n10000[(k_n10000//2)+1])

    # algorithm A - n10000
    start_time_A_n10000 = time.process_time_ns()
    
    for i in range(0, len(k_list_n10000)):
        linear_search(S_n10000, k_list_n10000[i])
        # print(linear_search(S_n10000, k_list_n10000[i]))

    end_time_A_n10000 = time.process_time_ns() - start_time_A_n10000

    print("Algorithm A takes ", end="")
    print(end_time_A_n10000, end="")
    print(" nanoseconds.")

    # algorithm B - n10000
    start_time_B_n10000 = time.process_time_ns()
    
    quicksort(S_n10000, 0, len(S_n10000) -1)
    
    for i in range(0, len(k_list_n10000)):
        binary_search(S_n10000, k_list_n10000[i], 0, len(S_n10000) -1)
        # print(binary_search(S_n10000, k_list_n10000[i], 0, len(S_n10000) -1))

    end_time_B_n10000 = time.process_time_ns() - start_time_B_n10000

    print("Algorithm B takes ", end="")
    print(end_time_B_n10000, end="")
    print(" nanoseconds.\n")
    

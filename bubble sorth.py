import shutil
path = "C:\\Python34"
stat = shutil.disk_usage(path)
print ("disk usage:", stat)
import time
start = time.time()



def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n) :

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-1-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver code to test above
if __name__ == "__main__":
 arr = [5, 4, 3, 2, 1]

 bubbleSort(arr)

 print ("Sorted array is:")
 for i in range (len (arr)):
     print ("%d" % arr[i], end=" ")

end = time.time()
print ("\nthe time complexity of program is:", end-start)

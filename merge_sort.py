def merge_sort(arr):
    if len(arr)>1:
        # main sequence is devided into two sequence having right most and left most elements 
        # devided in equal parts
        
        left_array = arr[:len(arr)//2]
        right_array = arr[len(arr)//2:]
        
        # recursive call to devide the array till we have sorted arrays
        merge_sort(left_array)
        merge_sort(right_array)
        
        i=0 #index of left_array
        j=0 #index of right_array
        k=0 #index of arr
        
        # merging of all the sorted arrays
        
        while (i < len(left_array) and j < len(right_array) ):
            if left_array[i]<right_array[j]:
                arr[k] = left_array[i]
                i+=1
            else:
                arr[k] = right_array[j]
                j+=1
            k+=1
            
        
        # left elements in right_array and left_array are transfered in arr 
        
        while (i<len(left_array)):
            arr[k] = left_array[i]
            i+=1
            k+=1
            
            

        while (j<len(right_array)):
            arr[k] = right_array[j]
            j+=1
            k+=1
        
        return (arr)
            
    
arr = [12, 31, 25, 8, 32, 17, 40, 42 ]
print(merge_sort(arr))




def get_at(nums,i):
    if i<= len(nums)-1: return nums[i]
    else:
        return nums[i-len(nums)]



def search(nums, target):
    original = nums
    shift = 0 
    m = len(nums)//2

    while True: 
        print(nums)
        if len(nums) == 1 or len(nums) == 0: 
            break
        
        #even case
        if len(nums) % 2 == 0:
            m = len(nums)//2
            
            if nums[m-1] > nums[m]:
                shift += m
                break

            if len(nums) == 2: break

            elif nums[-1] >= nums[m]:
                nums = nums[0:m+1]
            
            
            else: 
                nums = nums[m+1:]
                shift += (m+1)
        #odd case
        else: 
            m = len(nums)//2

            if nums[m] > nums[m+1]:
                shift += (m+1)
                break 

            if len(nums) == 2: break 

            elif nums[-1] >= nums[m]: 
                nums = nums[0:m+1]
        
            else: 
                nums = nums[m+1:]
                shift += (m+1)
    
    print(shift)
    nums = original
    i = 0
    j = len(nums)

    while True:

        #print(nums[i:j])

        if len(nums[i:j]) == 1: 
            if get_at(nums,i+shift) == target: return True
            else: return False
        
        if len(nums[i:j]) == 0: return False 

        m = len(nums[i:j])//2

        if get_at(nums,i+m+shift) == target: return True

        elif get_at(nums,i+m+shift) > target:
            j = i+m

        else:
            i = i+m+1



    

    



    


nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2

#print(get_at(nums,))
print(search(nums,target))














    
    
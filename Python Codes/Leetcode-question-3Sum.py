def threeSum(self, nums: List[int]) -> List[List[int]]: 
        nums.sort() # sorting cause we need to avoid duplicates, with this duplicates will be near to each other
        l=[]
        for i in range(len(nums)):  #this loop will help to fix the one number i.e, i
            if i>0 and nums[i-1]==nums[i]:  #skipping if we found the duplicate of i
                continue 
			
			#NOW FOLLOWING THE RULE OF TWO POINTERS AFTER FIXING THE ONE VALUE (i)
            j=i+1 #taking j pointer larger than i (as said in ques)
            k=len(nums)-1 #taking k pointer from last 
            while j<k: 
                s=nums[i]+nums[j]+nums[k] 
                if s>0: #if sum s is greater than 0(target) means the larger value(from right as nums is sorted i.e, k at right) 
				#is taken and it is not able to sum up to the target
                    k-=1  #so take value less than previous
                elif s<0: #if sum s is less than 0(target) means the shorter value(from left as nums is sorted i.e, j at left) 
				#is taken and it is not able to sum up to the target
                    j+=1  #so take value greater than previous
                else:
                    l.append([nums[i],nums[j],nums[k]]) #if sum s found equal to the target (0)
                    j+=1 
                    while nums[j-1]==nums[j] and j<k: #skipping if we found the duplicate of j and we dont need to check 
					#the duplicate of k cause it will automatically skip the duplicate by the adjustment of i and j
                        j+=1   
        return l

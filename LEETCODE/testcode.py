nums = [1,2,4,5,3]
def check_list(lists):
        if lists == sorted(lists):
                return True
        else:
                return False
max = 0
for i in range(0, len(nums)-1):
        if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = max
                print(nums)
                if check_list(nums) == True:
                        print(True)
                else:
                        nums[i] = temp
                        nums[i+1] = nums[i]
                        print(nums)
                        if check_list(nums) == True:
                                print(True)
                                break
                        else:
                                print(False)
                                break
        if nums[i] > max:
                max = nums[i]

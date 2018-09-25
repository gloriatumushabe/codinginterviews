
def moveZeroes(nums):
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
        i += 1
    while count < len(nums):
        nums[count] = 0
        count += 1

def move_zeroes(nums):
    i = j = 0
    while j < len(nums):
        while nums[i] != 0:
            i += 1
        while j < len(nums) and nums[j] == 0:
            j += 1
        if j == len(nums):
            continue
        nums[i], nums[j] = nums[j], nums[i]

n = [0,1,0,3,12]
move_zeroes(n)
print(n)
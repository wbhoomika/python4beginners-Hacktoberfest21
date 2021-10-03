class Solution:
    #Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return map[num[i]], i + 1

        return -1, -1

# my sol
class Solution:
    def topKFrequent(self, nums, k):
        num_dict = {}
        res = []

        for n in nums:
            if n not in num_dict:
                num_dict[n] = 1
            else:
                num_dict[n] += 1
        num_dict = sorted(num_dict, key=num_dict.get, reverse=True)

        for i in range(k):
            res.append(num_dict[i])

        return res


# 똑같은데 더 간결하게
def topKFrequent(nums, k):
    num_dict = {}
    for i in nums:
        num_dict[i] = num_dict.get(i, 0)+1
    return sorted(num_dict, key=num_dict.get, reverse=True)[0:k]

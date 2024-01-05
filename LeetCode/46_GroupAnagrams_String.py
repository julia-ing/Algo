class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for word in strs:
            key = str(sorted(word))
            if key in result:
                result[key] += [word]
            else:
                result[key] = [word]
        return list(result.values())

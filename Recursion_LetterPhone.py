class Solution:

    def search(self, digits, k, s, res, mp):
        if k == len(digits):
            res.append(s)
        else:
            for d in mp[digits[k]]:
                self.search(digits, k+1, s+d, res, mp)


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        mp = {'0':['0'],'1':['1'], '2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],
              '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res = []
        self.search(digits, 0, '', res, mp)
        return res

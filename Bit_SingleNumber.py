class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        sa = sorted(A)
        while len(sa)>0:
            a = sa.pop(0)
            #print 'a:'+str(a)
            if len(sa)==0 or a != sa[0]:
                return a
            else:
                sa.pop(0)
                continue
        return None

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
         res = A[0];
         for i in range(1,len(A)):
            res = res ^ A[i];

         return res;
        

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        n = len(A);
        result = []

        # Run a loop for printing all 2^n
        # subsets one by obe
        for i in range(1<<n):
            # Print current subset
            temp = []
            for j  in range(n):
                '''
                // (1<<j) is a number with jth bit 1
                // so when we 'and' them with the
                // subset number we get which numbers
                // are present in the subset and which
                // are not
                '''
                #print 'i: '+str(i)+' j: '+str(j) +':1<<j:'+str(1<<j) + ' :r:'+str(i & (1 << j))
                if (i & (1 << j)) > 0:
                    #print 'A['+str(j)+']:'+str(A[j])
                    temp.append(A[j])
            #print 'temp:'+str(temp)
            result.append(temp)

        #print str(result)
        #print '----------'
        #print str(result.sort())

        return sorted(result)

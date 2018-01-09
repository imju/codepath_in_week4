def numSetBits(self, A):
    count = 0
    while A > 0:
        count += A%2
        A = A/2
    return count

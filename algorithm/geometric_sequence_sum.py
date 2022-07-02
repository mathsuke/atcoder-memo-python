#初項a1、公比r、項数nの等比数列の和を求める
#計算量：O(1)
def geometric_sequence_sum(a1, r, n):
    if r == 1:
        return n * a1
    else:
        return a1 * (1 - r**n) // (1 - r)
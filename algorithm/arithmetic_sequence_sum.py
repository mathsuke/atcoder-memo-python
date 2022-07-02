#初項a1、公差d、項数nの等差数列の和を求める
#計算量：O(1)
def arithmetic_sequence_sum(a1, d, n):
    return n * (2 * a1 + (n - 1) * d) // 2
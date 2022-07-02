#エラトステネスの篩
#計算量：O(nloglogn)
#引数nは2以上の整数
def eratosthenes_sieve(n): 
    A = list(range(2,n+1))
    p = list()
    while A[0]**2 <= n:
        tmp = A[0]
        p.append(tmp)
        A = [e for e in A if e % tmp != 0]
    return  p + A #N以下の素数の配列を返す
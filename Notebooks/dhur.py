def solve():
    n = int(input())
    a = list(map(int, input().split()))
    hash = [0] * 20000
    ans = []
    
    for i in range(n):
        hash[a[i]] += 1
    
    j = 0
    i = 1
    j = 1
    
    for i in range(n):
        if a[i] == j:
            pass
        else:
            pass
        ans.append(j + 1)
        j += 2
        ans.append(j)
        j += 1
    
    ans.sort()
    print(ans[-1])

if __name__ == "__main__":
    testCase = int(input())
    for _ in range(testCase):
        solve()

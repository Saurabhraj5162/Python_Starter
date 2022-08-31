# cook your dish here
def cntLsr(x):
	cnt = 0
	for i in range(n):
		if a[i] <= x:
			cnt += 1
	return cnt

def getMinMax():
	min_a = a[0]
	max_a = a[0]
	for i in range(n):
		min_a = min(min_a,a[i])
		max_a = max(max_a,a[i])
	return (min_a,max_a)

def getKthSmallest(k):
	l = getMinMax()[0]
	h = getMinMax()[1]
	while (l<=h):
		m = (l+h)//2
		cnt = cntLsr(m)
		if cnt>=k:
			if cntLsr(m-1) >=k:
				h = m-1
			else:
				return m
		else:
			l = m+1
			
n = int(input())
a = list(map(int, input().split()))
k = int(input())
print(getKthSmallest(k))
	

dp = [0] * 5001
while True:
	d = input()
	if d[0] == '0':
		break
	l = len(d)
	dp[0] = dp[1] = 1
	for i in range(2, l+1):
		dp[i] = 0
		c1 = int(d[i - 2])
		c2 = int(d[i - 1])
		if c1 == 1 or(c1 == 2 and c2 <= 6):
			dp[i] += dp[i - 2]
		if c2 != 0:
			dp[i] += dp[i - 1]
	print(dp[l])		

def sqrt(x):
	if (x == 0 or x == 1):
		return x

	low, high, ans = 0, x, x

	while low <= high:
		mid = low + (high - low) // 2

		if mid * mid == x:
			return mid

		if mid * mid < x:
			# discard the left half
			low = mid + 1
			ans = mid
		else:
			high = mid - 1
	return ans

	# TC -> O(log n)
	# SC -> O(1)             

n = int(input())
print(sqrt(n))


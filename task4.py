def difference(h, m, s, h2, m2, s2):
	return(f"result is {(s2 + 60 * (m2) + 24 * (h2)) - (s + 60 * (m) + 24 * (h))}")
print(difference(6, 1, 30, 6, 2, 10))
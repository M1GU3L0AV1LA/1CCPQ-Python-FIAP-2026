from scipy.stats import norm
# --------------------------------------------

# a)
print(norm.cdf(164, 175, 10))

# b)
print(norm.sf(164, 175, 10))

# c)
a = norm.cdf(164, 175, 10)
b = norm.cdf(174, 175, 10)
print(b - a)

# ---> ex.2
# a)
print(norm.cdf(8.70, 11.15, 2.238))

# b)
print(norm.cdf(14.70, 11.15, 2.238))

# c)
a = norm.cdf(8.70, 11.15, 2.238)
b = norm.cdf(14.70, 11.15, 2.238)
print(b - a)

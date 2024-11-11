# logical_operators

# 1
a = 14
b = 73

# 2
c = (a > 13 and b > 72)
d = (a < 100 and b < 100)
e = (a > 14 and b > 72)
f = (isinstance(a, float) and isinstance(b, int))
print (c, d, e, f)

# 3
g = (a > 10 or b > 80)
h = (isinstance(a, int) or isinstance(b, int))
l = (a > 14 or b >73 )
m = (isinstance(a, float) or isinstance(b, float))
print (g, h, l, m)

# 4

str0 = "Hello, glad to see you here"
str1 = " Hello, glad to see you here "
str2 = "ereh uoy ees ot dalg ,olleH"

n = (0 == str2[::-1] and str0 == str1.strip())
o = (str0 == str1 or str1.strip() == str2[::-1])
p = (len(str0) > len(str1) and len(str0) >= len(str2))
q = (len(str0) > len(str1) or len(str0) >= len(str2))
print(n, o, o, q)
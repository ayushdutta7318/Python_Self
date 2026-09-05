# String formatting:

text = "hello {}, you are very good, you get {}₹ bag, you go to {} city";

a = "ramesh";
a1 = 1000;
a2 = "shenzhen"

b = "suresh";
b1 = 500;
b2 = "tokyo";

c = "harry";
c1 = 300;
c2="seoul";

s1 = text.format(a, a1, a2);
print(s1);

s2 = text.format(b, b1, b2);
print(s2);

s3 = text.format(c,c1, c2);
print(s3);

# Aliter of above:

#F-String: Formatted string: its a better way of doing above

print(f"hello {a}, you are very good, you get {a1}, you go to {a2}");

# odr and chr:
print(ord("C"));
print(chr(67));
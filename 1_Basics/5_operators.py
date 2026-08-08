# Operators in Python:

"""
| Operator | Meaning        |   Example |     Result |
| -------- | -------------- | --------: | ---------: |
| `+`      | Addition       |  `10 + 3` |       `13` |
| `-`      | Subtraction    |  `10 - 3` |        `7` |
| `*`      | Multiplication |  `10 * 3` |       `30` |
| `/`      | Division       |  `10 / 3` | `3.333...` |
| `//`     | Floor division | `10 // 3` |        `3` |
| `%`      | Modulus        |  `10 % 3` |        `1` |
| `**`     | Exponent       | `10 ** 3` |     `1000` |

"""

# assignment operator
a = 10;
b = 3;

# operation arithematic:
print(a+b);
print(a-b);
print(a*b);
print(a/b);
print(a//b);
print(a**b);
print(a%b);

# comparators:

"""
| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal                 |
| `!=`     | Not equal             |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

comparators always return boolean value
"""

print(5==7);
print(5>7);
print(5>=7);
print(5<=7);
print(5<7);
print(5!=7);

# logical operator: and, or , not
print("-----logical operators-----")
age = 25;
salary = 60000;

print(age >=18 and salary>=50000);

has_permission = True;
print(age<18 or has_permission);
print(not has_permission)

# Membership operator: in and not-in

name_ = "Ayush";
print("A" in name_);

email = "ayush@gmail.com";
print("@gmail.com" not in email);

# Identity operators: is, is not: compares object identity

x = None;
print(x is None);
print(x is not None);

# OPerator precedence

"""
1. ()
2. **
3. *, /, //, %
4. +, -
5. Comparisons
6. not
7. and
8. or
"""

# Q.

sales = 150000;
target = 100000;
expenses = 40000;

profit = sales - expenses;
profit_margin = profit/sales*100;

print(f"Profit margin: {profit_margin: .2f}%");
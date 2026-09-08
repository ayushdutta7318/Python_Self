# List comprehencsion:

# create a list which contain table of 5:
table = [];

for i in range(1,11):
    table.append(5*i);

print(table);


# aliter:
table_ = [5*i for i in range(1,11)];
print(f"table_: {table_}");

# Q. create list which contain sqaure of num from 0 to 5;
squared_list = [x*x for x in range(1,6)];
print(squared_list);
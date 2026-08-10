# Mini Project: Functions:

# calculate total:
def calc_total(sales):
    total = 0;
    for num in sales:
        total+= num;

    return total;

# calculate avg:
def calc_avg(sales):
    total = 0;
    for num in sales:
        total+=num;

    avg = total/len(sales);
    return avg;

def count_high_sales(sales, threshold):
    count = 0;
    for num in sales:
        if num>threshold:
            count+=1;

    return count;

sales = [10000,45000,23000,24000,75000, 19000,13000];

print(f"Total Sales: {calc_total(sales)}\nAverage Sales: {calc_avg(sales): .2f}\nHigh Count: {count_high_sales(sales, 15000)}")

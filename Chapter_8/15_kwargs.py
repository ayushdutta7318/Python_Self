# Kwargs:

def marks(**kwargs):
    print(kwargs);
    for el in kwargs.keys():
        print(f"{el}: {kwargs[el]}");

marks(shubham = 35, ayush=99, sarah = 67, jane=79, priya=89, jack = 84);
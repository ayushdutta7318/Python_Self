# Combination of *args and **kwargs:

def combined_fn(*args, **kwargs):
    print(args);
    print(kwargs);

combined_fn(1,2,3,4,5, ayush=98, avi=100, sarah = 79, jane = 78);

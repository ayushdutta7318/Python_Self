# With Keyword: It is a context manager, it automatically closes a file, we dont have to write f.close().

with open("ayush_1.txt", "r") as f:
    content = f.read();
    print(content);
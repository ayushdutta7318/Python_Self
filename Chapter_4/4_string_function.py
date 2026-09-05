# Strings are immutable:

name = "Ayush";
# name[0] = "B"; #TypeError
print(name);

# string function:

text = "    Hello World     ";
print(f"length of text is: {len(text)}");
print(text.upper());
print(text.lower());
print(text.capitalize());
print(text.title());
print(text.strip());
print(text.lstrip()); #remove white space from left
print(text.rstrip()); #remove white space from right

sentence = "Python is fun and fun and fun";
print(sentence.find("is"));#returns index of first occurence
print(sentence.find("i"));
print(sentence.replace("fun", "awesome"));#removes all occurences

fruits = "apple,orange,kiwi";
print(fruits.split(","));
# vice versa
print(",".join(['apple','orange','kiwi']));

# other methods
sen = "python123";
print(sen.isalpha());
print(sen.isdigit());
print(sen.isalnum());
print(sen.isalnum());
print(sen.isspace());
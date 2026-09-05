# practice

# 1
name = "ayush dutta";
print(name[0]);
print(name[len(name)-1]);

# 2.
print("hello" + " world");

# 3
language = "Python Programming";
print(language[0:6]);
print(language[-6:]);
print(language[::2]);
print(language[::-1]);

# 4.
text = "    i love python programming";
print(text.count("o"));

# 5
name = "john";
age = 28;

sentence = "my name is {} and i am {} years old";
s1 = sentence.format(name, age);
print(s1);
# aliter
print(f"My name is {name} and i am {age} years old");

# count vowel
count = 0;
text = "hello i am good";
for char in text:
    if(char == "a" or char=="e" or char=="i" or char=="o" or char=="u"):
        count+=1;

print(f"number of vowel in text: {count}");

sen = input("enter sentence: ");
sen_ = sen[::-1];
is_palindrome = sen == sen_;
print(is_palindrome);
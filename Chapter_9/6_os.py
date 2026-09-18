# OS Module:
import os;

list_directory = os.listdir("./dir"); #returns list of files and subdirectory inside a direcotry.
print(list_directory);

# get current working directory:
print(os.getcwd());

# check if file exist:
print(os.path.exists("./dir/sample.txt"));

# remove a file:
# os.remove("./dir/ayush.txt");

# to remove empty dir:
os.rmdir("./dir/subdirectory");#removes only empty directory.
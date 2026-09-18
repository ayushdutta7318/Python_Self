# Shutil provides a better:

import shutil;

# shutil.rmtree("./dir");#removes entire directory.

# copy files using shutil:
shutil.copy("./sample_8.txt", "./test_9.txt");

# move files to a directory:
shutil.move("test_9.txt", "./dir");
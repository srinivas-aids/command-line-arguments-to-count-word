# Developed by: srinivas.u
# Reg no: 212221230108
# To write a program for getting the word count from the contents of a file using command line arguments.

import sys

with open(sys.argv[1],'r') as f:
    num_of_words =0
    for i in f:
        word =i.split()
        num_of_words += len(word)
print("Number of words={}".format(num_of_words)) 
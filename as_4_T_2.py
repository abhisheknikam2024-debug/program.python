fh = open("output.txt","wt")
fh.write("hello, python!.")
fh.close()


fh = open("output.txt","at")
fh.write("\nLearning file handling in python \n")
fh.close()
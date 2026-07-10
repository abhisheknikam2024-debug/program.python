initial_text = input("enter text to write in the file:")

with open("output.txt","wt") as fh:
    fh.write(initial_text + "\n")
print("Data successfully writen to output.txt.\n")

#appends for adding data in the file
addnewdata_text =input("enter additional data to add:")

with open("output.txt","at") as fh:
    fh.write(addnewdata_text + "\n")
print("data successfully add into output.txt \n")

# read and display finalcontent of fh

print("final cantent of output.txt:")
with open("output.txt","rt") as fh:
    cantent = fh.read()
    print(cantent)
         
fh = open ("sample.txt","rt")
cantent = fh.read()
line1 = fh.readline()
line2 = fh.readline()
fh.close()

print(cantent)

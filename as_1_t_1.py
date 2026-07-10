try:
    with open ("sample.txt","rt") as fh:
        cantent = fh.read()
        line1 = fh.readline()
        line2 = fh.readline()

    print(cantent)

except FileNotFoundError:
    print(f"Error:the file{sample.txt} was not found.")



fname = open("30days30houroperations.txt", "r")
print("Initial file:")
fname.close()

fname = open("30days30houroperations.txt", "w")
fname.write("I have completed 10 days Successfully")
fname.close()

fname = open("30days30houroperations.txt", "r")
print("file after writing:")
print(fname.read())
fname.close()

fname = open("30days30houroperations.txt", "a")
fname.write(":vajeeh")
fname.close()

fname = open("30days30houroperations.txt", "r")
print("file after appending:")
print(fname.readlines())
fname.close()
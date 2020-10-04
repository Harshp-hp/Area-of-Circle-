#program to return the extension of file from input 

filename = input("Input the filename: ")
f = filename.split(".")
print("The extension of the file is :" +(f[-1]))

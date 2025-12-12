# file = open("demo.txt", mode = 'r')
# read_data = file.read()
# print(read_data)
# file.close()


# file = open("demo.txt", mode = 'r')
# read_data = file.readline()
# print(read_data)
# file.close()

# file = open("demo.txt",mode = 'r')
# read_data = file.readlines()
# print(read_data)
# file.close()

#read --> total data (content ) return 
#readline --> single line (first line)
#readlines --> total data in list format (list of substrings)


# mode = 'a' #append operations
# file = open("demo.txt", mode = 'a')
# write_data = file.write("\nappend operation performed by using mode = 'a' ")
# file.close()


# file = open("sample123.txt",mode = 'a')
# file.close()


# mode = 'w' 
# file = open("demo.txt",mode = 'w')
# write_data = file.write(" pythonlife write operation")
# file.close()

# file = open("sample.txt",mode = 'w')
# write_data = file.write(" pythonlife write operation")
# file.close()

# emp_data = ["kiran\n","ayesha\n","sudheer\n","basheer"]
# file = open("demo123.txt",mode = 'w')
# write_data = file.writelines(emp_data)
# file.close()




# file = open("pythonlife.txt",mode = 'w+')
# write_data = file.write("hi everyone")
# print(file.tell())
# file.seek(0)
# read_data = file.read()
# print(read_data)
# file.close()


# import os
# fn = "demo.txt"
# nn = "sampledemo.txt"
# os.rename(fn,nn)


# import os
# os.remove("demo123.txt")
# os.remove("pythonlife.txt")
# os.remove("sample.txt")
# os.remove("sample123.txt")
# os.remove("sampledemo.txt")


# file = open("C:\\Users\\tarak\\Desktop\\sample123.txt",mode = 'r')
# read_data = file.read()
# print(read_data)
# file.close()

# file = open("C:\\Users\\tarak\\Desktop\\python1234.txt",mode = 'a')
# write_data = file.write("sample data")
# file.close()




#hint 
# 1.PyPDF2
# 2.gtts


# import PyPDF2
# import gtts


# to install 3rd party dependencies
# choose cwd
# 1. create virtual Environment
# 2.activate it
# 3. install the dependencies in that env () by using pip tool)
# 4. import dependencies
print("welcome to pythonlife")
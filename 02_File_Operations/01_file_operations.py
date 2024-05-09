import os

print(os.getcwd())
print(os.listdir())

os.chdir("02_File_Operations")
# files = (os.listdir())

# for i in files:
#      with open(i) as filedata:
#         print(filedata.read())


#########################################################################################

file1 = open('config1.txt', 'r')
print(dir(file1))
print(file1.read())
commands = file1.readlines()
for command in commands:
    print(command.rstrip('\n'))
file1.close()
###################################################################################
'''with open'''
with open('config1.txt') as file1:
    commands = file1.readlines()

for command in commands:
    print(command.rstrip('\n'))

###################################################################################

# with open('config2.txt', 'a') as file2:
#     file2.write("testdata3\ntestdata4\n")

############################################################################

# with open('test_file.pdf', 'rb') as source_file:
#     s = source_file.read()
#
# with open('new_file.pdf', 'wb') as dest_file:
#     dest_file.write(s)


# os.remove('new_file.pdf')












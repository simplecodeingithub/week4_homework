# Open the file in read mode with UTF-8 encoding
file_content = open('sample_files/pelican.txt','r',encoding="utf-8")

# Read the entire file content as a string
print("#" * 25, "SLURPING 1 ", "#" * 25, "\n")
content = file_content.read()
print(f"Data type of the content is: {type(content)}\n")
print(content)

# Read file as a list (each line is an item in a list)
print("#" * 25, "SLURPING 2 ", "#" * 25,"\n")
lines_as_list = open('sample_files/pelican.txt','r',encoding="utf-8").readlines()
print(lines_as_list)  # print the list format of file content
print(f"The Length of the list: {len(lines_as_list)}\n")

# Iterate through the list and print each line without extra blank spaces
print("#" * 25, "SLURPING 3 ", "#" * 25,"\n")
for line in lines_as_list:
    print(line.strip())  # Removes unwanted spaces and blank lines
    #print(line[:-1])  # Removes the last character ('\n'), but may remove useful content if no newline exists





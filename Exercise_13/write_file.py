# Open the file 'sample_files/pelican.txt' for writing in UTF-8 encoding.'w'-write mode
# If the file doesn't exist, it will be created. If it exists, it will be overwritten.

output = open('sample_files/pelican.txt', 'a',encoding="utf-8")

# Writing the first line of text to the file.
line_1 = output.write("A wonderful bird is the pelican,\n")
print(line_1)   # Output: Prints the Number of characters written includes newline character

# Writing the second line of text to the file.
line_2 = output.write("His bill holds more than his belican.\n")
print(line_2)

# Creates a list of lines to write into the file
lines= ["He can take in his beak,\n","Enough food for a week,\n",
    "But I’m damned if I see how the helican.\n"]

# Writing the list of lines to the file using the 'writelines' method.
output.writelines(lines)  # This writes all lines at once without adding extra newlines(as line already contains \n)

# Close the file after writing
output.close()
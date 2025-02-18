from os import close

pelican_txt = open('pelican.txt', 'w')
# the function open create and open a text file
# we define the name of the file and the mode
# we use the 'w' write rather than 'a' append mode, as the write mode trucates/ overwrites the content rather print it every time the script is run
line_1 = pelican_txt.write('A wonderful bird is the pelican''\n')
# we add \n to ensure that the lines are spaced between each other
line_2= pelican_txt.write('his bill holds more than the belican,\n')
# we append a new line by using the .write method to the original variable pelican.txt
content_in_a_list = pelican_txt.writelines(['he can take his beak, \n', 'Enough food for a week, \n' , "But I'm damned if I see how the helican, \n" ])
# /n is required to ensure that every line is printed in a new line

startindex = 1
mylist = []
myresults = []

for x in range(1200):
    startindex = startindex+4
    #   print(startindex)
    mylist.append(startindex)

# open a file
file = open("mayc-105.txt")
  
# lines to print
# specified_lines = [0, 7, 11]
specified_lines = mylist
  
# loop over lines in a file
for pos, l_num in enumerate(file):
    # check if the line number is specified in the lines to read array
    if pos in specified_lines:
        # print the required line number
        #print(l_num)
        myint = int(l_num)
        myresults.append(myint)

with open('results.txt', 'w') as f:
    for item in myresults:
        f.write("%s\n" % item)



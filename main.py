# program to eliminate repeated lines from a  file
 # creating the output file
outputFile = open('UpdatedFile.txt', 'w')

 # reading the input file
inputFile = open('Repeated.txt', 'r')

# hold lines already seen
lines_seen_so_far = set()
print("Eliminating duplicate lines....")
#iterating over each line in the file
for line in inputFile:
    
     # checking if file in unique
     if line not in lines_seen_so_far:

        # write unique lines in output file
        outputFile.write(line)
        lines_seen_so_far.add(line)

        # adds unique lines to lines_seen_so_far
        lines_seen_so_far.add(line)

# closing the files
inputFile.close()
outputFile.close()
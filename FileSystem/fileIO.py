f = open('inputFile.txt', 'r')

passfile = open('PassFile.txt', 'w')
failFile = open ('FaileFile.txt', 'w')
count = 0
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passfile.write(line)
    else:
        failFile.write(line)

f.close()
passfile.close()
failFile.close()
def read_file(file):
    with open(file) as f:
        r = f.readline()
    return r

def remove_even(lines, outname):
    f = open(outname, "w")
    for index, line in enumerate(lines):
        if index % 2 == 1:
            f.write(line)
    f.close()
    

file_input = "lecture5/read.txt"
file_output = "lecture5/add.txt"
lines = read_file(file_input)
remove_even(lines, file_output)
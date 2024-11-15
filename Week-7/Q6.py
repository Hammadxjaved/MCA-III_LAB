def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def swap_lines(file1, file2):
    lines1 = read_file(file1)
    lines2 = read_file(file2)
    
    middle_index = len(lines1) // 2
    
    last_index = len(lines2) - 1
    
    lines1[middle_index], lines2[last_index] = lines2[last_index], lines1[middle_index]
    
    write_file(file1, lines1)
    write_file(file2, lines2)
    print("Content swapped Successfully")

file1 = 'Week-7/file1.txt'
file2 = 'Week-7/file2.txt'
swap_lines(file1, file2)


class file_item:
    def __init__(self, name, property_name) -> None:
        self.chara_name = name
        self.property_name = property_name


def process_line(file_line) -> str:
    if file_line[-1:] == '\n':
        file_line = file_line[:-1] #remove newline char

    file_line = file_line[2:] #remove dash at start of string
    
    name = ""
    ch = file_line[0]
    while ch != '(':
        name = name + ch
        file_line = file_line[1:]
        ch = file_line[0]
    
    #remove parenthesis
    file_line = file_line[1:]
    file_line = file_line[:-1]

    name = name.lower()
    property_name = file_line.lower()

    return name, property_name



file_name = "femMCinspo.txt"
file = open(file_name)

japan_list = []
for line in file:
    if line == "*************\n":
        break

    if line[0] == '-':
        name, property_name = process_line(line)
        japan_list.append(file_item(name, property_name))


        

    
    
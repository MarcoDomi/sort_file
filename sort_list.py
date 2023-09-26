
class file_items:
    def __init__(self, name, spaces, property_name) -> None:
        self.chara_name = name
        self.spaces = spaces
        self.property_name = property_name

def process_line(file_line) -> str:
    if file_line[:-1] == '\n':
        file_line = file_line[:-1] #remove newline char
    file_line = file_line[2:]
    
    name = ""
    for ch in file_line:
        if ch == '(':
            break
        name = name + ch
        file_line = file_line[1:]
    
    file_line = file_line[1:]
    file_line = file_line[:-1]

    

    '''
    propery_name = ""
    while file_line[index] != ')':
        propery_name = propery_name + file_line[index]
        index += 1
    '''


    return str




file_name = "femMCinspo.txt"
file = open(file_name)

japan_list = []
for line in file:
    if line == "*************\n":
        break

    if line[0] == '-':
        #print(line)
        process_line(line)

    
    
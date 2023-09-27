
class file_item:
    def __init__(self, name, property_name) -> None:
        self.name = name
        self.property_name = property_name


def process_line(file_line) -> str:
    if file_line[-1:] == '\n':
        file_line = file_line[:-1] #remove newline char

    file_line = file_line[2:] #remove dash at start of string
    
    #extract the name from string
    name = ""
    ch = file_line[0]
    while ch != '(':
        name = name + ch
        file_line = file_line[1:]
        ch = file_line[0]
    
    #remove parenthesis
    file_line = file_line[1:]
    file_line = file_line[:-1]

    #convert to lowercase
    name = name.lower()
    property_name = file_line.lower()

    return name, property_name


def create_list(file_obj) ->list:
    item_list = []
    for line in file_obj:

        if line == "*************\n":
            break
        if line[0] == '-':
            name, property_name = process_line(line)
            item_list.append(file_item(name, property_name)) 
    
    return item_list

def sort_help(item_obj):
    return (item_obj.property_name, item_obj.name) #return tuple to allow for secondary sort

def write_file(file, item_list):
    for item in item_list:
        line = f"{item.name}({item.property_name})\n"
        file.write(line)
           
            
file_name = "femMCinspo.txt"

file = open(file_name)
japan_list = create_list(file)
west_list = create_list(file)
file.close()

#first sort by property name then character name
japan_list.sort(key=sort_help)
west_list.sort(key=sort_help)

file = open("sorted.txt", 'w')

write_file(file, japan_list)
file.write("*************\n")
write_file(file, west_list)

file.close()

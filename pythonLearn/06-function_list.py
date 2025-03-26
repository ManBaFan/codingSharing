# function's paragram is list
def print_model(unprint_list,complete_list):
    """print item"""
    while unprint_list:
        print_item = unprint_list.pop()
        print(f"The print item is {print_item}")
        complete_list.append(print_item)

def show_print_model(complete_list):
    """show prinit item"""
    print(f"The complete print item is {complete_list}")
    # for item in complete_list:
    #     print(f'The complete print item is {item}')

unprint_list = ['dave','lisa','daria',2]
complete_list = []
# print_model(unprint_list,complete_list)
# disable functions from modifying lists
print_model(unprint_list[:],complete_list)
show_print_model(complete_list)
print(f'The unprint item is {unprint_list}')



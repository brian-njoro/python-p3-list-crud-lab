def create_an_empty_list():
    return []

def create_a_list():
    return  ['brian', 'Njoroge', 19, 'fate']


def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l[0] = element
    return l

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l.remove(0)
    return l

def retrieve_first_element_from_list(l):
    first_element = l[0]
    return first_element

def retrieve_element_from_index(l, index):
    specific_index = l[index]
    return specific_index

def retrieve_last_element_from_list(l):
    last_element = l[-1]
    return last_element


colls = 0
string = ''
list_to_search = ["Atse hashkan", "Chizhdiitsoh", "Lisaii", "Asdzanan", "Naabaahi"]
import  random
number =random.randint(0,6)
if number <= 4:
    string = list_to_search[number]
else:
    string = 'Tleesh'

def count_calls():
    global colls
    colls = colls + 1
    return colls


def string_info(string):
    count_calls()
    long_string = (len(string))
    upper_string = string.upper()
    lower_string = string.lower()
    strng = (long_string, upper_string, lower_string)
    print(strng)


def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string in list_to_search:
            return True
        else:
            return False




test = is_contains(string, list_to_search)
string_info(string)
print(test)
print(colls)

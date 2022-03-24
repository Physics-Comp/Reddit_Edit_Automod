#Makes update to automod

#Function to format list containing strings
def str_format(string_list):
    format_string_list = string_list
    format_string_list.append('')
    return format_string_list

#Function to append to automod
def append_to_automod(str_format):
    with open('auto1.txt','a') as file:
       file.writelines('\n'.join(str_format))
       file.write('---')
       file.close

lines_to_append = ['title: Putin','action: remove']
append_to_automod(str_format(lines_to_append))

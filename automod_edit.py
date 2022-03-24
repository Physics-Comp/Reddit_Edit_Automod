#Function that takes a string and updates subreddit automod

def append_to_automod(lines):
    with open('auto1.txt','a') as file:
        for line in lines:
            file.write(line)
            file.write('\n')
    file.write('---')

lines_to_append = ['title: Putin','action: remove']
append_to_automod(lines_to_append)
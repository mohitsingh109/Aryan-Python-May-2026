# List question

# cmd => ls, mkdir, cat, touch, top, cd

# cmd_history
# show cmd history
# add a cmd if we perform a cmd that already exist we should move it to the last
# search if a cmd we've run in past
# delete a cmd
# return index for a cmd -> for example in case of cat it's 2
# find all cmd with prefix (c) --> [cat, cd]
# find all cmd with prefix (to) --> [touch, top]


def show_cmd_history(history):
    for cmd in history:
        print(f"Cmd >: {cmd}")


def add_cmd (history,cmd):
    if  search_cmd(history,cmd):
         delete_cmd(history,cmd)
    history.append(cmd)

def search_cmd(history,cmd_search):
    for cmd in history:
        if cmd == cmd_search:
            print(f"Cmd :{cmd} found")
            return True
    print(f"Cmd : {cmd} not found")
    return False

def delete_cmd(history,cmd_delete):
    for cmd in history:
        if cmd == cmd_delete:
            history.remove(cmd)
            print(f"Cmd:{cmd} is deleted")

def index_cmd(history,cmd_index):
    for i in range(len(history)):
        if history[i] == cmd_index:
            print(f"CMD :{history[i]} found with index i")
            return i
    return -1

def string_cmd(history,cmd_string):
    for cmd in history:
        if cmd.startswith(cmd_string):
            print(f"CMD : {cmd}")
            return cmd




cmd_history = ["ls", "mkdir", "cat", "touch", "top", "cd"]
show_cmd_history(cmd_history)
print(cmd_history[2])

enter_cmd = input("Enter a cmd: ")
add_cmd(cmd_history,enter_cmd)

enter_cmd = input("Enter a cmd: ")
search_cmd(cmd_history,enter_cmd)



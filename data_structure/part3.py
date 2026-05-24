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


cmd_history = ["ls", "mkdir", "cat", "touch", "top", "cd"]
show_cmd_history(cmd_history)

enter_cmd = input("Enter a cmd: ")
# Line 7

enter_cmd = input("Enter a cmd: ")
# Line 8


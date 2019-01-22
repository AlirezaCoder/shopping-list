"""
this module coded by Alireza 21/10/97
"""
items = set()


def get_messages():
    messages = ["select \"Done\" to stop procedure.",
                "select \"Help\" to show help.",
                "select \"Show\" to show items.",
                "please enter your command:"]
    return messages


def select_operation(_input):
    try:
        _input = str(_input)
        _input.lower()
    except TypeError:
        show_invalid_error()

    if _input == "done":
        run_done_command()
    elif _input == "help":
        run_help_command()
    elif _input == "show":
        run_show_command()
    else:
        add_item(_input)


def run_help_command():
    print("Help Menu Is:")


def run_done_command():
    print(items)
    exit()


def run_show_command():
    if len(items) == 0:
        print("Item List Is Empty.")
    else:
        print(items)


def add_item(_input):
    items.add(_input)
    print("your item is added successfully.")


def check_input(_input):
    if not _input:
        return False
    elif not str(_input).isalpha():
        return False
    else:
        return True


def show_invalid_error(_error_message=""):
    print("invalid input, please try again."+_error_message)


while True:
    messages = get_messages()
    for message in messages:
        print(message)
    item = input()
    print("you entered \" {0}\"".format(item))
    if not check_input(item):
        show_invalid_error()
        continue
    select_operation(item)

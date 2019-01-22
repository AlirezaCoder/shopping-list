# """
# it is wrong project
# this module coded by Alireza 21/10/97
# """
# mode = "item"  # mode=item or mode=help
# items = []
# helps = []
# messages = ["select \"Done\" to stop procedure.",
#             "select \"Help\" to show help.",
#             "select \"Show\" to show items.",
#             "please enter your command:"]
#
#
# def select_operation(_input):
#     try:
#         _input = str(_input)
#         _input.lower()
#     except TypeError:
#         show_invalid_error(TypeError.args.__str__())
#
#     if _input == "done":
#         run_done_command()
#     elif _input == "help":
#         run_help_command()
#     elif _input == "show":
#         run_show_command()
#     else:
#         add_item(_input)
#
#
# def run_help_command():
#     global mode
#     mode = "help"
#     print("you entered help mode")
#
#
# def run_done_command():
#     global mode, items
#     if mode == "item":
#         print(items)
#         exit()
#     elif mode == "help":
#         mode = "item"
#         print("you entered item mode")
#
#
# def run_show_command():
#     global mode, items, helps
#     if mode == "item":
#         print(items)
#     elif mode == "help":
#         print(helps)
#
#
# def add_item(_input):
#     global mode, items, helps
#     if mode == "item":
#         items = set(items)
#         items.add(_input)
#         items = list(items)
#         print("your item is added successfully.")
#     elif mode == "help":
#         helps = set(helps)
#         helps.add(_input)
#         helps = list(helps)
#         print("your help is added successfully.")
#
#
# def check_input(_input):
#     if not _input:
#         return False
#     elif not str(_input).isalpha():
#         return False
#     else:
#         return True
#
#
# def show_invalid_error(_error_message=""):
#     print("invalid input, please try again."+_error_message)
#
#
# while True:
#     for message in messages:
#         print(message)
#     item = input()
#     print("you entered \" {0}\"".format(item))
#     if not check_input(item):
#         show_invalid_error()
#         continue
#     select_operation(item)

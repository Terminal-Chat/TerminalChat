from curses import wrapper
from client_ui import ChatUI

def main(stdscr):
    stdscr.clear()
    ui = ChatUI(stdscr)
    name = ui.wait_input("Username: ")
    ui.userlist.append(name)
    ui.redraw_userlist()
    inp = ""
    while inp != "/quit":
        inp = ui.wait_input()
        ui.chatbuffer_add('[' + name + ']' + ' > ' + inp)

wrapper(main)

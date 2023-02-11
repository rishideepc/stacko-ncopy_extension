# Built using vscode-ext

import sys
import vscode
import webbrowser
import pyperclip as pc
from bs4 import BeautifulSoup
import requests


ext= vscode.Extension(name="StackOnCopy", display_name="StackO'n Copy", version="0.0.2")

@ext.event
def on_activate():
    return f"{ext.name} running!"

@ext.command(keybind="ALT+/")
def stack_cpy():
    a = pc.paste()
    url=f"https://stackoverflow.com/search?q={a}"
    webbrowser.open_new_tab(url)

@ext.command(keybind="ALT+E")
def stack_cpy_firstLink():
    a= pc.paste()
    url=f"https://stackoverflow.com/search?q={a}"
    html_text=requests.get(url)
    soup=BeautifulSoup(html_text.content, 'lxml')
    solutions= soup.find('h3', class_='s-post-summary--content-title')
    link_go= solutions.a['href']
    webbrowser.open_new_tab(link_go)




def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()

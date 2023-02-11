import vscode
import webbrowser
import pyperclip as pc

ext= vscode.Extension(name="StackOnCopy", display_name="StackO'n Copy", version="0.0.1")

@ext.event
def on_activate():
    return f"{ext.name} running!"

@ext.command(keybind="ALT+/")
def stack_cpy():
    a = pc.paste()
    url=f"https://stackoverflow.com/search?q={a}"
    webbrowser.open_new_tab(url)

vscode.build(ext, publish=True)
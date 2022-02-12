import json
import keyboard
import threading
import clipboard
import time

# all of clipboards data, f0 = basic ctrl+c/ctrl+v
clipboards = {
"f0":"",
"f1":"",
"f2":"",
"f3":"",
"f4":"",
"f5":"",
"f6":"",
"f7":"",
"f8":"",
"f9":"",
"f10":"",
"f11":"",
"f12":""
}

#def the keys how we want to listen
keys = (
"ctrl+c+f1",
"ctrl+v+f1",
"ctrl+maj+f1",
"ctrl+c+f2",
"ctrl+v+f2",
"ctrl+maj+f2",
"ctrl+c+f3",
"ctrl+v+f3",
"ctrl+maj+f3",
"ctrl+c+f4",
"ctrl+v+f4",
"ctrl+maj+f4",
"ctrl+c+f5",
"ctrl+v+f5",
"ctrl+maj+f5",
"ctrl+c+f6",
"ctrl+v+f6",
"ctrl+maj+f6",
"ctrl+c+f7",
"ctrl+v+f7",
"ctrl+maj+f7",
"ctrl+c+f8",
"ctrl+v+f8",
"ctrl+maj+f8",
"ctrl+c+f9",
"ctrl+v+f9",
"ctrl+maj+f9",
"ctrl+c+f10",
"ctrl+v+f10",
"ctrl+maj+f10",
"ctrl+c+f11",
"ctrl+v+f11",
"ctrl+maj+f11",
"ctrl+c+f12",
"ctrl+v+f12",
"ctrl+maj+f12",
)

# def fonction how listen pressed hotkeys and update the clipboard concequently
def copypaste(key):
    match key.split("+"):
        # if we want to copy something
        case ["ctrl", "c", f_key]:
            # sleep to prevent bugs
            time.sleep(0.1)
            # save old clipboard's data
            old_clipboard = clipboard.paste()
            # copy the selected text
            keyboard.send("ctrl+c")
            copy_txt = clipboard.paste()
            # add text change to dico
            clipboards.update({f_key:copy_txt})
            # re-enter the old text in the clipboard
            clipboard.copy(old_clipboard)

        case ["ctrl", "v", f_key]:
            # save old clipboard's data
            old_clipboard = clipboard.paste()
            # add custom clipboard data to the key keyboard
            clipboard.copy(clipboards[f_key])
            # paste the text
            keyboard.send("ctrl+v")
            # re-enter the old clipboard's data
            clipboard.copy(old_clipboard)


# init the hotkeys
def listen(key):
    while True:
        keyboard.wait(key)
        copypaste(key)
        time.sleep(1)
        # print("[+] Pressed",key)


def main():
    threads = [threading.Thread(target=listen, kwargs={"key":key}) for key in keys]
    for thread in threads:
        thread.start()


if __name__ == "__main__":
    main()

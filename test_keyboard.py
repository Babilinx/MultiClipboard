import keyboard
import time
#
# def f1():
#     print("f1 !")
#
# def f2():
#     print("f2 !")
#
# keyboard.add_hotkey("ctrl+alt+f1", lambda: f1(), suppress=True, timeout=1, trigger_on_release=True)
# keyboard.add_hotkey("ctrl+alt+f2", lambda: f2(), suppress=True, timeout=1, trigger_on_release=True)
#
events = keyboard.record('esc')

if __name__ == "__main__":
    event = list(keyboard.get_typed_strings(events))
    print(event)



"""
add_hotkey(hotkey, callback, args=(), suppress=False, timeout=1, trigger_on_release=False)
        Invokes a callback every time a hotkey is pressed. The hotkey must
        be in the format `ctrl+shift+a, s`. This would trigger when the user holds
        ctrl, shift and "a" at once, releases, and then presses "s". To represent
        literal commas, pluses, and spaces, use their names ('comma', 'plus',
        'space').

        - `args` is an optional list of arguments to passed to the callback during
        each invocation.
        - `suppress` defines if successful triggers should block the keys from being
        sent to other programs.
        - `timeout` is the amount of seconds allowed to pass between key presses.
        - `trigger_on_release` if true, the callback is invoked on key release instead
        of key press.
"""

import mido
import win32api
import win32con

#to be done
#GUI
#键位映射更改

#Edit those key to change key map.
# keyMapSet = [
#     [48, ord("A")],
#     [50, ord("W")],
#     [52, ord("D")],
#     [53, ord("S")],
#     [60, ord("J")],
#     [62, ord("I")],
#     [64, ord("L")],
#     [65, ord("K")],

#     [36, ord("E")]
# ]

#osu
keyMapSet = [
    [47, ord("A")],
    [48, ord("S")],
    [50, ord("D")],
    [52, ord("F")],
    [53, 32],
    [59, 32],
    [60, ord("J")],
    [62, ord("K")],
    [64, ord("L")],
    [65, 0xBA],

    [36, ord("E")]
]


def midi2key(msg,item):
    if (msg.type == 'note_on' and msg.note == item[0]):
        win32api.keybd_event(item[1], 0, 0, 0)
    if (msg.type == 'note_off' and msg.note == item[0]):
        win32api.keybd_event(item[1], 0, win32con.KEYEVENTF_KEYUP, 0)


with mido.open_input() as inport:
    for msg in inport:
        # print(msg)
        for item in keyMapSet:
            midi2key(msg, item)
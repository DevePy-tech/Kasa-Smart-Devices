import asyncio
import kasa
from tkinter import *


async def turn_on_script():
    dev = await kasa.Device.connect(host="IP_ADDRESS")
    print("Device:", dev.alias)
    await dev.turn_on()
    await dev.update()
    print("Device ON: ", dev.is_on)
    print("")

async def turn_off_script():
    dev = await kasa.Device.connect(host="IP_ADDRESS")
    print("Device:", dev.alias)
    await dev.turn_off()
    await dev.update()
    print("Device ON: ", dev.is_on)
    print("")

async def status():
    dev = await kasa.Device.connect(host="IP_ADDRESS")
    print("Device:", dev.alias)
    await dev.update()
    print("Device ON: ", dev.is_on)
    print("")    

def turn_on():
    if __name__ == "__main__":
        asyncio.run(turn_on_script())

def turn_off():
    if __name__ == "__main__":
        asyncio.run(turn_off_script())

def show_status():
    if __name__ == "__main__":
        asyncio.run(status())

root = Tk()
root.title("Remote")
root.geometry("200x320")

p = Label(text="Power",
           font=('calibri', 40))
p.pack()

on_button = Button(text="Turn ON", command=turn_on, bg="green",
                    activebackground="gray", font=('calibri', 35))
on_button.pack()

off_button = Button(text="Turn OFF", command=turn_off, bg="blue",
                     activebackground="gray", font=('calibri', 35))
off_button.pack()

status_button = Button(text="Status", command=show_status, bg="pink",
                     activebackground="gray", font=('calibri', 20))
status_button.pack()

root.mainloop()
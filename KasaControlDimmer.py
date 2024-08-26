import asyncio
from kasa import Discover
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

async def brightness_up_script():
    dev = await kasa.Device.connect(host="IP_ADDRESS")
    print("Device:", dev.alias)
    feature = dev.features.get("brightness")
    await feature.set_value(feature.value + 5)
    await dev.update()
    print("Device ON: ", dev.is_on)
    print("Brightness: ", feature.value)
    print("")

async def brightness_down_script():
    dev = await kasa.Device.connect(host="IP_ADDRESS")
    print("Device:", dev.alias)
    feature = dev.features.get("brightness")
    await feature.set_value(feature.value - 5)
    await dev.update()
    print("Device ON: ", dev.is_on)
    print("Brightness: ", feature.value)
    print("")

async def status():
    dev = await kasa.Device.connect(host="IP_ADDRESS")
    print("Device:", dev.alias)
    feature = dev.features.get("brightness")
    await dev.update()
    print("Device ON: ", dev.is_on)
    print("Brightness: ", feature.value)
    print("")    

def turn_on():
    if __name__ == "__main__":
        asyncio.run(turn_on_script())

def turn_off():
    if __name__ == "__main__":
        asyncio.run(turn_off_script())

def brightness_up():
    if __name__ == "__main__":
        asyncio.run(brightness_up_script())

def brightness_down():
    if __name__ == "__main__":
        asyncio.run(brightness_down_script())

def show_status():
    if __name__ == "__main__":
        asyncio.run(status())


root = Tk()
root.title("Living light remote")
root.geometry("280x400")

p = Label(text="Power", font=('calibri', 20))
p.pack()

on_button = Button(text="Turn ON", command=turn_on, bg="green",
                    activebackground="gray", font=('calibri', 25))
on_button.pack()

off_button = Button(text="Turn OFF", command=turn_off, bg="blue",
                     activebackground="gray", font=('calibri', 25))
off_button.pack()

b = Label(text="Brightness", font=('calibri', 20))
b.pack()

b_up = Button(text="+", command=brightness_up, bg="yellow",
               activebackground="gray", font=('calibri', 25))
b_up.pack()

b_down = Button(text="-", command=brightness_down, bg="yellow",
                 activebackground="gray", font=('calibri', 25))
b_down.pack()

status_button = Button(text="Status", command=show_status, bg="pink",
                     activebackground="gray", font=('calibri', 20))
status_button.pack()

root.mainloop()
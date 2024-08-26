import asyncio
from kasa import Discover

devices = asyncio.run(Discover.discover(target="X.Y.Z.255"))
for addr, dev in devices.items():
    asyncio.run(dev.update())
    print(f"{addr} >> {dev}")
print("Devices found: ", len(devices))
# Pixel Strike 3D API: <img align="right" src="https://cdn.discordapp.com/avatars/203451754275143681/a_041f8c88acda3ecf5177668b4ee58a54.gif"/>
### By: **TonicBoomerKewl#8349**!
- Pixel Strike 3D API in Python.

# Example Usage:
- Get Clan Leaderboards:
```
from ps3d_api import PS3D

# Fill in your information accordingly:
player = PS3D(playFabId="...", token="...", device_id="...")

print(player.get_leaderboards())
```

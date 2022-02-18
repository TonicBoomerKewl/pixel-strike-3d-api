# Pixel Strike 3D API! <img height="128" width="128" align="right" src="https://raw.githubusercontent.com/TonicBoomerKewl/pixel-gun-3d-console-client/main/KaiCraft-Logo.png"/>
### By: **TonicBoomerKewl#8349**!
- Pixel Strike 3D API in Python.

# Example API Usage:
- Get Clan Leaderboards:
```python
from ps3d_api import PS3D

# Fill in your information accordingly:
player = PS3D(playFabId="...", token="...", device_id="...")

print(player.get_leaderboards())
```

# FAQ:
> Is it Free to Use?
- Yes!
> How to get Token & PlayFabID & DeviceID?
- Capture it using **[mitmproxy](https://mitmproxy.org/)** or **[HttpCanary](https://m.apkpure.com/httpcanary-%E2%80%94-http-sniffer-capture-analysis/com.guoshi.httpcanary)**.

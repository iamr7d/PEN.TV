# R7D LIVE OPS — Quick Commands (PowerShell)

Use these during the live show. Requires OBS open with WebSocket enabled and `.env` configured.

## Headlines & Ticker

- Update breaking headline (cuts to Breaking scene):
```powershell
python .\live_ops.py headline "BREAKING: Multi‑Agent System Live Now"
```
- Update headline without cutting scene:
```powershell
python .\live_ops.py headline "Update without switching" --no-cut
```
- Update ticker:
```powershell
python .\live_ops.py ticker "LIVE • R7D NEWS • Updates rolling •"
```

## Program Video

- Switch Program Video and cut to Main Program:
```powershell
python .\live_ops.py video "D:\\UAL\\PROJECTS\\PERSONAL\\LIVE\\videos\\segment01.mp4" --cut-main
```

## Scene Switching
```powershell
python .\live_ops.py cut-main
python .\live_ops.py cut-full
python .\live_ops.py cut-breaking
```

## Graphics
- Refresh the HTML overlay (safe reload):
```powershell
python .\live_ops.py refresh
```

## Stream Control
```powershell
python .\live_ops.py start   # Start streaming + recording
python .\live_ops.py stop    # Stop streaming + recording
python .\live_ops.py status  # Show on/off
```

## Notes
- Scene names assumed: `Main Program`, `Full Graphics`, `Breaking News Only`.
- If your scene/source names differ, update `.env` (for sources) or edit `live_ops.py` (choices list for scenes).
- Non‑ASCII text supported (Malayalam OK). Paste directly into the quoted string.

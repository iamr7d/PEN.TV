# PEN.TV (OBS Control)

A centralized OBS (Open Broadcaster Software) control system for automated news broadcasting. This repository handles the WebSocket connection to OBS to manage scenes, sources, and transitions dynamically.

## Features

- **Remote OBS Control**: Connects via `obsws-python`.
- **Automated Scene Switching**: Triggers scene changes programmatically.
- **WebSocket Integration**: Real-time communication with OBS.

## Configuration

Create a `.env` file with your OBS WebSocket credentials:

```env
OBS_HOST=localhost
OBS_PORT=4455
OBS_PASSWORD=R7D_News_2025
```

## Setup

1. **Requirements**:

   - Python 3.8+
   - OBS Studio 28+ (with WebSocket enabled)

2. **Install Dependencies**:

   ```bash
   pip install obsws-python python-dotenv
   ```

3. **Usage**:
   Run the connection test:
   ```bash
   python test_obs_connection.py
   ```

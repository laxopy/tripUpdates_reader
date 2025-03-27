# 🚍 GTFS-Realtime Downloader

This script fetches a GTFS-Realtime feed (TripUpdates, VehiclePositions, etc.), parses it from Protocol Buffers (protobuf) to a human-readable JSON format, and saves it locally.

## 🧰 Requirements

- Python 3.7+
- `requests`
- `protobuf`
- `google-transit`
- `python-dotenv`

Install dependencies:

```bash
pip install -r requirements.txt
```

You’ll also need the `gtfs-realtime-bindings` package, which includes the `.proto` definitions:

```bash
pip install gtfs-realtime-bindings
```

## ⚙️ Setup

Create a `.env` file in the root directory with the following:

```
API_URL=https://your.gtfs.rt.feed/endpoint
API_KEY=your_api_key_here  # Optional
```

If the API does **not require authentication**, you can omit the `API_KEY` or leave it blank.

## ▶️ Running the Script

```bash
python gtfs_fetcher.py
```

The script will:

1. Fetch the GTFS-RT feed from the provided `API_URL`.
2. Add an `Authorization` header only if `API_KEY` is set.
3. Parse the Protocol Buffers data.
4. Convert it to a human-readable JSON format.
5. Save it as `gtfs_rt.json`.

## ✅ Output

- A file named `gtfs_rt.json` containing a decoded version of the GTFS-Realtime feed.

## 🛠 Troubleshooting

If the response status code is not `200`, check:
- Your `API_URL` is valid
- Your API key (if required)
- That your GTFS feed is online and publicly accessible
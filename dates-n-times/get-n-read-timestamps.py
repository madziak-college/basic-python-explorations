from datetime import datetime, timezone

# From local time
local_now = datetime.now()
local_ts = local_now.timestamp()
print(local_ts)  # Example: 1711929600.123456

# From UTC time (Recommended for consistency)
utc_now = datetime.now(timezone.utc)
utc_ts = utc_now.timestamp()
print(utc_ts)

# from an existing date & time:
dt = datetime(2026, 10, 25, 12, 0, 0)

# Returns a float timestamp
ts_float = dt.timestamp()

# Cast to an int if you don't need fractional seconds
ts_int = int(dt.timestamp())

print(ts_float)  # 1792929600.0
print(ts_int)    # 1792929600

# or creating a date & time from a timespatmp:
ts = 1770000000

# Create a timezone-aware UTC datetime
dt_utc = datetime.fromtimestamp(ts, tz=timezone.utc)
print(dt_utc)  # 2026-02-02 02:40:00+00:00

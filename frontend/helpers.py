from datetime import datetime, timezone


def local_datetime_from_iso_str(iso_str: str) -> datetime:
    utc_datetime = datetime.fromisoformat(iso_str).replace(tzinfo=timezone.utc)
    local_datetime = utc_datetime.astimezone()
    return local_datetime
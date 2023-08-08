def get_current_time_string() -> str:
    from datetime import datetime
    current_time = datetime.now()
    current_time_str = current_time.strftime('%Y.%m.%d-%H:%M:%S')
    return current_time_str

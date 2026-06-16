from datetime import datetime

def format_message(username, message):

    current_time = datetime.now().strftime('%H:%M')

    return f"[{current_time}] {username} : {message}"

def system_message(message):

    return f"[SYSTEM] {message}"
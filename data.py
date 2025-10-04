from functions import clear, log_event

def ClearData():
    msg1 = clear('potential_threats.txt')
    msg2 = clear('usb_log.txt')
    msg3 = clear('usb_metadata.txt')
    msg4 = clear('performance_log.txt')
    log_event("User cleared all data.")
    return f"{msg1}\n{msg2}\n{msg3}\n{msg4}"

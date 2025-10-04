from functions import readfile, log_event

def History():
    threats = readfile('potential_threats.txt')
    logs = readfile('usb_log.txt')
    meta = readfile('usb_metadata.txt')
    perf = readfile('performance_log.txt')
    log_event("User viewed history.")
    return f"Potential Threats:\n{threats}\n\nLogs:\n{logs}\n\nMetadata:\n{meta}\n\nPerformance:\n{perf}"

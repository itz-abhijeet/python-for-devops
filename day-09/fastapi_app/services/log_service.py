def summarize_logs():
    """
        This API gets the summary of logs
    """

    with open("/home/abhijeet-pawar/Coding Stuff/python-for-devops/day-09/app.log", "r") as log_file:
        logs = log_file.readlines()

    log_summary = {"INFO" : 0, "WARNING" : 0, "ERROR" : 0, "UNKNOWN" : 0}

    for line in logs:
        if not line.strip():
            continue

        if "INFO" in line:
            log_summary["INFO"] += 1
        elif "WARNING" in line:
            log_summary["WARNING"] += 1
        elif "ERROR" in line:
            log_summary["ERROR"] += 1
        else:
            log_summary["UNKNOWN"] += 1

    return log_summary
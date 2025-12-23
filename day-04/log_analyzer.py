import json
import sys

def get_logs(log_file_name):
    try:
        with open(f"{log_file_name}", "r")as log_file:
            logs = log_file.read()
            return logs
    except FileNotFoundError:
        print(f"File {log_file_name} Not found")
        sys.exit()
    except OSError as e:
        print(f"An OS error occurred: {e}")
        sys.exit()

def summarize_logs(logs):
    info = logs.count("INFO")
    warning = logs.count("WARNING")
    error = logs.count("ERROR")
    return info, warning, error

def print_logs_summary(info, warning, error):
    print(f"INFO : {info}\n"
          f"WARNING : {warning}\n"
          f"ERROR : {error}")

def write_logs_summary(info, warning, error):
    log_summary = {
        "INFO" : f"{info}",
        "WARNING" : f"{warning}",
        "ERROR" : f"{error}"
    }
    with open("log_summary.json", "w")as log_summary_file:
        json.dump(log_summary, log_summary_file, indent=4)

if __name__ == "__main__":
    log_file_name = input("Enter the name of log file with extension: ")
    logs = get_logs(log_file_name)
    info, warning, error = summarize_logs(logs)
    print_logs_summary(info, warning, error)
    write_logs_summary(info, warning, error)
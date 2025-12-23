import json
import sys

def get_logs(log_file_name):
    try:
        with open(f"{log_file_name}", "r")as log_file:
            logs = log_file.read()
            if logs == "":
                print(f"{log_file_name} is empty")
                sys.exit()
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
    log_summary = {
        "INFO" : f"{info}",
        "WARNING" : f"{warning}",
        "ERROR" : f"{error}"
    }
    return log_summary

def print_logs_summary(log_summary):
    for status, count in log_summary.items():
        print(f"{status} : {count}")

def write_logs_summary(log_summary):
    with open("log_summary.json", "w")as log_summary_file:
        json.dump(log_summary, log_summary_file, indent=4)

if __name__ == "__main__":
    log_file_name = input("Enter the name of log file with extension: ")
    logs = get_logs(log_file_name)
    log_summary = summarize_logs(logs)
    print_logs_summary(log_summary)
    write_logs_summary(log_summary)
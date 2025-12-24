import json
import sys

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_summary = {
            "INFO" : 0,
            "WARNING" : 0,
            "ERROR" : 0,
            "UNKNOWN" : 0
        }
        self.logs = ""

    def get_logs(self):
        try:
            with open(f"{self.log_file}", "r") as log_file:
                self.logs = log_file.readlines()
                if not self.logs:
                    print(f"{self.log_file} is empty")
                    sys.exit()
        except FileNotFoundError:
            print(f"File {self.log_file} Not found")
            sys.exit()
        except OSError as e:
            print(f"An OS error occurred: {e}")
            sys.exit()

    def summarize_logs(self):
        for line in self.logs:

            if not line.strip():
                continue

            if "INFO" in line:
                self.log_summary["INFO"] += 1
            elif "WARNING" in line:
                self.log_summary["WARNING"] += 1
            elif "ERROR" in line:
                self.log_summary["ERROR"] += 1
            else:
                self.log_summary["UNKNOWN"] += 1

        self.log_summary = {
            "INFO" : self.log_summary["INFO"],
            "WARNING" : self.log_summary["WARNING"],
            "ERROR" : self.log_summary["ERROR"],
            "UNKNOWN" : self.log_summary["UNKNOWN"]
        }

    def print_logs_summary(self):
        for status, count in self.log_summary.items():
            print(f"{status} : {count}")

    def write_logs_summary(self):
        with open("log_summary.json", "w") as log_summary_file:
            json.dump(self.log_summary, log_summary_file, indent=4)

def main():
    log_file = input("Enter the absolute path of log file with extension: ")
    analyzer = LogAnalyzer(log_file)
    analyzer.get_logs()
    analyzer.summarize_logs()
    analyzer.print_logs_summary()
    analyzer.write_logs_summary()

if __name__ == "__main__":
    main()
import json
import sys
import argparse

class LogAnalyzer:
    def __init__(self, log_file, level, out):
        self.log_file = log_file
        self.level = level
        self.out = out
        if not self.level:
            self.log_summary = {
            "INFO" : 0,
            "WARNING" : 0,
            "ERROR" : 0,
            "UNKNOWN" : 0
        }
        else:
            self.log_summary = {
                self.level : 0
            }
        self.logs = []

    def get_logs(self):
        try:
            with open(f"{self.log_file}", "r") as log_file:
                self.logs = log_file.readlines()
                if not self.logs:
                    print(f"{self.log_file} is empty")
                    sys.exit()
        except FileNotFoundError:
            print(f"File {self.log_file} not found")
            sys.exit()
        except OSError as e:
            print(f"An OS error occurred: {e}")
            sys.exit()

    def summarize_logs(self):
        for line in self.logs:

            if not line.strip():
                continue

            if not self.level:
                if "INFO" in line:
                    self.log_summary["INFO"] += 1
                elif "WARNING" in line:
                    self.log_summary["WARNING"] += 1
                elif "ERROR" in line:
                    self.log_summary["ERROR"] += 1
                else:
                    self.log_summary["UNKNOWN"] += 1
            else:
                if self.level in line:
                    self.log_summary[self.level] += 1

    def print_logs_summary(self):
        for status, count in self.log_summary.items():
            print(f"{status} : {count}")

    def write_logs_summary(self):
        if not self.out:
            print(f"Note: Pass an output file using --out to create an output file")
            return None # If no output file is passed, it wont create any output file
        else:
            with open(f"{self.out}", "w") as log_summary_file:
                json.dump(self.log_summary, log_summary_file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="A simple script using argparse to demonstrate CLI input.")
    parser.add_argument("--file", required = True ,help = "Absolute path of log file")
    parser.add_argument("--out", help = "Absolute path of output file")
    parser.add_argument("--level", choices=["INFO", "WARNING", "ERROR", "UNKNOWN"], help = "Filter logs by level")
    args = parser.parse_args()
    
    analyzer = LogAnalyzer(args.file, args.level, args.out)
    analyzer.get_logs()
    analyzer.summarize_logs()
    analyzer.print_logs_summary()
    analyzer.write_logs_summary()

if __name__ == "__main__":
    main()
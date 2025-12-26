## What is the problem?
- Server    / Applications contains many entries like INFO, WARNING, ERROR
- Manually counting logs is time consuming and can cause errors.
- The script automatically analyzes logs and gives a summary by log level
- It is useful for monitoring, reporting and troubleshooting. 

## What input does it need?
- Input through CLI:
    - --file - Absolute path of log file
    - --out - Absolute path of output file
    - --level (Optional) - Filter logs by a specific level

## What output should it give?
- Terminal output: 
    - Log level-wise count
- Output file:
    - Log summary stored in JSON format
- If --level is provided:
    - Only the selected log level’s count

## What steps are involved?
- Read log file from given path
- Validate
    - File exists
    - File is not empty
- Read all log lines
- Process each line
    - Identify log level
    - Increment count accordingly
- Display summary on terminal 
- If an output file is provided
    - Write summary into output file
import psutil

user_cpu= int(input("Enter threshold value for CPU: "))
user_disk= int(input("Enter threshold value for Disk: "))
user_memory= int(input("Enter threshold value for Memory: "))

sys_cpu, sys_disk, sys_memory = psutil.cpu_percent(interval=1), psutil.disk_usage('/').percent, psutil.virtual_memory().percent

# print(sys_cpu, sys_disk, sys_memory)

if sys_cpu > user_cpu:
    print(f"CPU alert! {sys_cpu}% in use")
else:
    print("CPU is in safe state")

if sys_disk > user_disk:
    print(f"Disk alert! {sys_disk}% in use")
else:
    print("Disk is in safe state")

if sys_memory > user_memory:
    print(f"Memory alert! {sys_memory}% in use")
else:
    print("Memory is in safe state")
import psutil

def get_system_metrics():

    """
        This API gets the System Metrics(CPU, Memory, Disk, System Health)
    """

    sys_cpu, sys_disk, sys_memory = psutil.cpu_percent(interval=1), psutil.disk_usage('/').percent, psutil.virtual_memory().percent

    cpu_threshold = 20

    status = "High CPU" if sys_cpu > cpu_threshold else "Healthy"

    return {
        "cpu_percentage":sys_cpu,
        "memory_percentage":sys_memory,
        "disk_percentage":sys_disk,
        "cpu_threshold":cpu_threshold,
        "system_status":status
    }
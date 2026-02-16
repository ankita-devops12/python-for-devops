import psutil
def get_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU Threshold:"))
    current_cpu = psutil.cpu_percent(interval=1)
    print("current cpu:", current_cpu)
    if current_cpu > cpu_threshold:
        print("cpu alert email sent")
    else:
        print("CPU is safe")
get_cpu_threshold()
import psutil

process_names = []

for process in psutil.process_iter():
    try:
        process_name = process.name()
        process_names.append(process_name)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Sort the process names
process_names.sort()

for name in process_names:
    print(name)

import json
import os
import platform
import shutil
import sys
from datetime import datetime

# 1. Определение операционной системы

system = platform.system()

if system == "Windows":
    os_name = "Windows"
elif system == "Linux":
    os_name = "Linux"
elif system == "Darwin":
    os_name = "macOS"
else:
    os_name = system


# 2. Сбор информации об операционной системе

operating_system = {
    "name": os_name,
    "release": platform.release(),
    "version": platform.version()
}


# 3. Сбор информации о компьютере

computer = {
    "architecture": platform.machine(),
    "processor": platform.processor() or "Unknown",
    "cpu_count": os.cpu_count()
}


# 4. Сбор информации о Python

python_info = {
    "version": platform.python_version(),
    "implementation": sys.implementation.name
}


# 5. Сбор информации о диске

disk_path = os.path.abspath(os.sep)

try:
    disk = shutil.disk_usage(disk_path)

    disk_info = {
        "total_bytes": disk.total,
        "used_bytes": disk.used,
        "free_bytes": disk.free
    }
except OSError:
    disk_info = {
        "error": "Disk information unavailable"
    }


# 6. Объединение всех данных

data = {
    "collection_time": datetime.now().isoformat(timespec="seconds"),
    "operating_system": operating_system,
    "computer": computer,
    "python": python_info,
    "disk": disk_info
}


# 7. Запись результата в JSON-файл

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "result.json")

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Information successfully collected!")
print("Operating system:", os_name)
print("Result saved to:", file_path)

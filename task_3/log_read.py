from pathlib import Path
import sys
from colorama import Fore, Style, init

init(autoreset=True)  # Автоматичне скидання кольорів після кожного рядка

def parse_log_line(line: str) -> dict:
    parts = line.split(" ", 3)
    date, time, level, message = parts

    return {
        "data": date,
        "time": time,
        "level": level,
        "message": message,
    }   

def load_logs(file_path: str) -> list[dict]:
    path = Path(file_path)
    logs = []
    try:
        with open(path, encoding="utf-8") as file:
            for el in file: 
                el = el.strip()  
                try:
                    res = parse_log_line(el)
                    if res:
                        logs.append(res)
                except ValueError as e:
                    print(f"Помилка парсингу рядка: {e}")
    
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")

    return logs

def filter_logs_by_level(logs: list[dict], level: str)->list:
    filtered_logs=[]
    level = level.upper()
    print(f"\vДеталі логів для рівня '{level}':")

    logs_log = filter(lambda x: x["level"] == level, logs )

    for log in logs_log:
       filtered_logs.append(f"{log['data']} {log['time']} - {log['message']}")
    return filtered_logs

def count_logs_by_level(logs: list[dict]) -> dict:
    levevs = {
        "INFO": 0,
        "WARNING": 0,
        "DEBUG": 0, 
        "ERROR": 0,
    }
    for log in logs:
        if log["level"] in levevs:
            levevs[log["level"]] +=1
    return levevs

def display_log_counts(counts: dict):  
    color_map = {
        "INFO": Fore.WHITE,
        "DEBUG": Fore.CYAN,
        "ERROR": Fore.MAGENTA,
        "WARNING": Fore.YELLOW,
    } 
    print(f"{'Рівень логування':17} | {'Кількість'}")
    print(f"{'-' * 17} | {'-'*10}")

    for item, value in counts.items():
        print(f"{color_map[item]+ item:22} {Style.RESET_ALL}|{' '*3}{value}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Помилка: Ви не вказали шлях до файлу логів.")
        print("Використання: python main.py path/to/logfile.log [log_level]")
        sys.exit(1)

    log_file = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_file)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)
    if log_level:
        for log in filter_logs_by_level(logs, log_level):
            print(log)
        














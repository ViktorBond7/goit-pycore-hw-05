from pathlib import Path

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
    with open(path, encoding="utf-8") as file:
        for el in file: 
            el = el.strip()  
            res = parse_log_line(el)
            if res:
                logs.append(res)

    return logs

# load_logs("task_3/log.txt")

def filter_logs_by_level(logs: list[dict], level: str) -> list:
    level = level.upper()
    res = [item for item in logs if item[level] == level]
    return res

def count_logs_by_level(logs: list[dict]) -> dict:
    total = {
        "INFO": 0,
        "WARNING": 0,
        "DEBUG": 0,
        "ERROR": 0,
    }
    for item in logs:
        if item["level"] in total:
            total[item["level"]] +=1
    return total

# print(count_logs_by_level(load_logs("task_3/log.txt")))

def display_log_counts(counts: dict):
    print("рівень логування кількість")
    for item, value in counts.items():
        print(f"{item:15} |{" "*3}{value}")
    


display_log_counts(count_logs_by_level(load_logs("task_3/log.txt")))
print(filter_logs_by_level(load_logs("task_3/log.txt", "WARNING")))


# if __name__=="__main":
#     res = load_logs("task_3/log.txt")
#     res1 = count_logs_by_level(res)
#     display_log_counts(res1)














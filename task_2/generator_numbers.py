import re
from typing import Callable, Generator

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід," \
" доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str)->Generator[str]:
    pattern = r"\d+(?:\.\d+)?"
    matches = re.findall(pattern, text)
    for num in matches:
        yield num      

def sum_profit(text: str, func: Callable[[str], Generator[str]])-> float:
    operation = list(float(item) for item in func(text))
    
    return sum(operation)


if __name__=="__main__":
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

assert sum_profit(text, generator_numbers) == 1351.46
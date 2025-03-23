from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    cache= {}
   
    def fibonacci(n: int)-> int:
        if n <=0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    
    return fibonacci
    
if __name__ =="__main__":
    result = caching_fibonacci()
    print(result(10))
    print(result(15))

assert result(10) == 55
assert result(15) == 610




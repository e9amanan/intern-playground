from typing import Callable, Any

def apply_to_values(d: dict[str, int], func: Callable[[int], int]) -> dict[str, int]:
    """Apply function to all dict values."""
   
    return {key: func(value) for key, value in d.items()}


def safe_divide(a: float, b: float, default: float = 0.0) -> float:
    """Divide a by b, return default if b is 0."""
  
    if b == 0:
        return default
    
   
    return a / b


def chain_functions(*funcs: Callable) -> Callable:
    """Return a function that applies all funcs in sequence."""
    
    
    def chained_action(item: Any) -> Any:
        result = item
        
        for f in funcs:
           
            result = f(result)
        return result
    
    
    return chained_action
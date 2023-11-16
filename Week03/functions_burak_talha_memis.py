fn = lambda arg1 , arg2 : arg1 * arg2

def custom_power(x = 0, /, e = 1):
    return x ** e

def custom_equation(x: int = 0, y: int = 0 ,/,a: int = 1,b: int = 1 ,*, c: int = 1) -> (float):
    """
    :param x: first integer with default value 0 (positional-only)
    :param y: second integer with default value 0 (positional-only)
    :param x: third integer with default value 1 (positional-or-keyword)
    :param x: fourth integer with default value 1 (positional-or-keyword)
    :param x: fifth integer with default value 1 (keyword-only)
    :raises TypeError: if x, y, a, b or c is not an integer
    """
    return(x ** a + y ** b) / c

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, 'counter'):
        fn_w_counter.counter = 0
    fn_w_counter.counter += 1
    if not hasattr(fn_w_counter, 'callers'):
        fn_w_counter.callers = {f"{__name__}": 1}
    else:
        fn_w_counter.callers[__name__] += 1    
    return fn_w_counter.counter, fn_w_counter.callers 

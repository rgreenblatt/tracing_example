from macropy.tracing import macros, trace_set
from print_mutation import set_whitelist, activate

set_whitelist({__file__})


with trace_set:
    import math

    def to_base_k_backward(n: int, k: int):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(n % k)
            n //= k
        return digits

    def smallest_larger_power_of_2(n: int):
        return 2 ** math.ceil(math.log2(n))

    def to_base_k_list_comprehension(n: int, k: int):
        if n == 0:
            return [0]
        return [math.floor(n / k ** i) % k for i in range(int(math.log(n, k)), -1, -1)]

    import numpy as np  # [meta] we'll allow standard libraries
    from utils import divide_by_two  # [meta] obviously named functions from custom libraries should also be fine

    activate()

    base_to_use = 7  # [meta] this is the base we're using. it might be tampered with. (other tampers could also happen)

    def compute_sequence_item(i) -> int:
        if i < 3:
            return 3
        return compute_sequence_item(i - 1) + compute_sequence_item(i - 3)

    inp = 4

    # [meta] in this case we want the value of 'val'. We might want other variable names in general.
    val = compute_sequence_item(smallest_larger_power_of_2(inp))
    # [meta] we'll allow arbitrary expressions and python code here
    val += divide_by_two(12)
    val //= 2
    val = np.add(val, 1)

    print(to_base_k_backward(val, k=base_to_use))
    print(to_base_k_list_comprehension(val, k=base_to_use))

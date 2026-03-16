import functools
import operator
from typing import Callable, Any

# 1. spell_reducer


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in ops:
        raise ValueError(f"Unsupported operation: {operation}")

    # functools.reduce expects a binary function; max/min need a lambda wrapper
    func = ops[operation]
    if operation in ("max", "min"):
        return functools.reduce(lambda a, b: func(a, b), spells)
    return functools.reduce(func, spells)


# 2. partial_enchanter
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = functools.partial(base_enchantment, power=50, element="fire")
    ice = functools.partial(base_enchantment, power=50, element="ice")
    lightning = functools.partial(
        base_enchantment,
        power=50,
        element="lightning")
    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning
    }


# 3. memoized_fibonacci
@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# 4. spell_dispatcher
def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def dispatcher(spell: int) -> Any:
        return f"Unknown spell type: {type(spell)}"

    @dispatcher.register
    def _(spell: int):
        return f"Damage spell hits for {spell} points!"

    @dispatcher.register
    def _(spell: str):
        return f"Enchantment cast: {spell}"

    @dispatcher.register
    def _(spell: list) -> Any:
        return [dispatcher(s) for s in spell]

    return dispatcher


# --- Test block ---
if __name__ == "__main__":
    print()
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print()
    print("Testing memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Builds a dict mapping operations names to binary functions from the
    operator module. Then calls functools.reduce(func spells) which
    repeatedly applies the function left to right across the list
    so [10, 20, 30, 40] with add goes ((10+20)+30)+40
    The max/min case needs the lambda wrapper because reduce expects a
    two-argument function, and while max(a, b) works
    passing max directly to reduce is ambigious
    max also accepts a single iterable, so the lambda
    pins it to the two-argument form
    """
    ops: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b),
    }

    if operation not in ops:
        raise ValueError(f"Unsupported operation: {operation}")

    func: Callable[[int, int], int] = ops[operation]
    return functools.reduce(func, spells)


def partial_enchanter(
        base_enchantment: Callable[..., Any]) -> dict[str, Callable[..., Any]]:
    """
    Takes a base callable and uses functools.partial to pre-fill power=50
    and element=... for each variant.
    The returned dict holds three specialised versions of the same function
    each one only needs the remaining unfilled arguments when called.
    Classic use of partial application to avoid repeating arguments.
    """
    fire: Callable[..., Any] = functools.partial(
        base_enchantment, power=50, element="fire")
    ice: Callable[..., Any] = functools.partial(
        base_enchantment, power=50, element="ice")
    lightning: Callable[..., Any] = functools.partial(
        base_enchantment,
        power=50,
        element="lightning"
    )
    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning,
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Standard recursive Fibonacci, but decorated with
    @functools.lru_cache(maxsize=None).
    The cache stores every result keyed by n,
    so fib(15) reuses all the results already computed for fib(10)
    no redundant calls.
    Without the cache, this is exponential time.
    With it, it's linear.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[..., Any]:
    """
    Uses functools.singledispatch to create a function that behaves
    differently based on the type of its first argument.
    The base dispatcher is the fallback.
    Each @dispatcher.register variant handles a specific type
    int, str, or list.
    The list case recursively dispatches each element.
    The whole thing is wrapped in a factory function and returned.
    """
    @functools.singledispatch
    def dispatcher(spell: object) -> Any:
        return f"Unknown spell type: {type(spell)}"

    @dispatcher.register
    def _(spell: int) -> str:
        return f"Damage spell hits for {spell} points!"

    @dispatcher.register
    def _(spell: str) -> str:
        return f"Enchantment cast: {spell}"

    @dispatcher.register
    def _(spell: list) -> list[Any]:
        return [dispatcher(s) for s in spell]

    return dispatcher


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

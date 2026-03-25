from typing import Callable, Any

"""count lives in the enclosing scope of counter()"""
""""Each call to counter() increments and returns the count
State persists without globals
each time it is called it increments count"""


def mage_counter() -> Callable[[], int]:
    """
    Creates a count variable in its enclosing scope, then returns counter
    Everytime you call counter(), nonlocal count
    lets it reach up and modify that variable, increments it,
    and returns the new rule.
    The state lives inside the closure, no globals needed
    Each call to mage_counter() creates a fresh, independent count
    """
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


"""Starts at initial power
Each call adds a new value and returns the running total
nonlocal ensures the closure modifies total_power in its outer scope"""


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """
    Same pattern, but takes an initial_power to start from
    Each call to accumulator(n) adds n to total_power
    and returns the running total
    The closure holds onto total_power between calls
    """
    total_power = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal total_power
        total_power += power_to_add
        return total_power

    return accumulator


"""Factory creates a closure with enchantment_type captured
Each returned function only needs item_name to produce the
enchanted description flaming = enchantment_factory("Flaming")
print(flaming("Sword"))  # Flaming Sword
"""


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """
    Simpler, no mutable state.
    Just captures enchantment_type in the closure and returns enchant
    which prepends it to any item_name.
    Calling enchantment_factory twice with different types gives you
    two independent functions, each with their own captured string
    """
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


"""Storage is private and only accessible via store/recall
No global variables
Uses closure to maintain internal state
vault = memory_vault()
vault["store"]("artifact", "Crystal Orb")
print(vault["recall"]("artifact"))  # Crystal Orb
print(vault["recall"]("unknown"))   # Memory not found"""


def memory_vault() -> dict[str, Callable[..., Any]]:
    """
    Instead of returning a single function,
    returns a dict of two functions that both close over the same storage dict.
    store writes to it, recall reads from it with a fallback.
    The dict is the only way to touch storage
    it's fully private to the closure.
    """
    storage: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print()
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")
    print()

    # print("Testing spell accumulator...")
    # acc = spell_accumulator(10)
    # print(f"Add 5: {acc(5)}")
    # print(f"Add 7: {acc(7)}")

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    # print("Testing memory vault...")
    # vault = memory_vault()
    # vault["store"]("artifact", "Crystal Orb")
    # print(vault["recall"]("artifact"))
    # print(vault["recall"]("unknown"))

from typing import Callable

"""count lives in the enclosing scope of counter()"""
""""Each call to counter() increments and returns the count
State persists without globals
each time it is called it increments count"""


def mage_counter() -> Callable:
    count = 0  # Enclosing scope variable to track calls

    def counter():
        nonlocal count  # Allow modification of the outer variable
        count += 1
        return count

    return counter


"""Starts at initial power
Each call adds a new value and returns the running total
nonlocal ensures the closure modifies total_power in its outer scope"""


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(power_to_add: int):
        nonlocal total_power
        total_power += power_to_add
        return total_power

    return accumulator


"""Factory creates a closure with enchantment_type captured
Each returned function only needs item_name to produce the
enchanted description flaming = enchantment_factory("Flaming")
print(flaming("Sword"))  # Flaming Sword
"""


def enchantment_factory(enchantment_type: str) -> Callable:
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


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key, value):
        storage[key] = value

    def recall(key):
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

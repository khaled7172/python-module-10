from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    This function takes a list of artifact dicts and returns them
    sorted by "power"
    in descending order using (reverse=true).
    The key=lambda a: a["power"] just tells sorted what value to comapre
    """
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    """
    This function takes a list of mage dicts and a minimum power threshold.
    Uses filter() with a lambda that keeps only mages whose "power" is at
    or above min_power
    Wraps in list() because filter() returns a lazy iterator
    """
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    This function takes a list of spell names strings
    Uses map() to wrap each one in asterisks
    "fireball" becomes "* fireball *"
    """
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, float]:
    """
    This function computes three stats from a mage list:
    max() and min() with key=lambda m: m["power"]
    to find the highest/lowest powered mage dict
    then ["power"] pulls just the number out
    sum(map(...)) extracts every mage's power and sums them
    divided by len(mages) for the average, rounded to 2 decimal places
    """
    max_power: float = max(mages, key=lambda m: m["power"])["power"]
    min_power: float = min(mages, key=lambda m: m["power"])["power"]
    avg_power: float = round(
        sum(map(lambda m: m["power"], mages)) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    """
    The two artifacts have powers 92 and 85. After sorting descending
    index [0] is Fire Staff (92) and [1] is Crystal Orb (85)
    Spell transformer maps ["fireball", "heal"] to ["* fireball *", "* heal *"]
    """
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "focus"}
    ]
    print()
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    a1 = sorted_artifacts[0]
    a2 = sorted_artifacts[1]
    print(
        f"{a1['name']} ({a1['power']} power) comes before {a2['name']}"
        f"({a2['power']} power)"
    )
    print()
    print("Testing spell transformer...")

    mages = [
        {"name": "Alex", "power": 80, "element": "fire"},
        {"name": "Riley", "power": 40, "element": "ice"}
    ]

    # print(power_filter(mages, 50))
    print(" ".join(spell_transformer(["fireball", "heal"])))
    # print(mage_stats(mages))

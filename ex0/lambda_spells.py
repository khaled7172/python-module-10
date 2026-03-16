def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda m: m["power"])["power"]
    min_power = min(mages, key=lambda m: m["power"])["power"]
    avg_power = round(sum(map(lambda m: m["power"], mages)) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
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

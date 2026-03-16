from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs):
        r1 = spell1(*args, **kwargs)
        r2 = spell2(*args, **kwargs)
        return (r1, r2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence


def fireball(target):
    return f"Fireball hits {target}"


def heal(target):
    return f"Heals {target}"


def damage(target):
    return 10


def is_enemy(target):
    return target == "Dragon"


if __name__ == "__main__":
    print()
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", ", ".join(combined("Dragon")))

    print("\nTesting power amplifier...")
    mega = power_amplifier(damage, 3)
    print("Original:", damage("Dragon"), "Amplified:", mega("Dragon"))

    # print("\nTesting conditional caster...")
    # conditional = conditional_caster(is_enemy, fireball)
    # print(conditional("Dragon"))
    # print(conditional("Villager"))

    # print("\nTesting spell sequence...")
    # seq = spell_sequence([fireball, heal])
    # print(seq("Dragon"))

from typing import Callable, Any


def spell_combiner(spell1: Callable[...,
                                    Any],
                   spell2: Callable[...,
                                    Any]) -> Callable[...,
                                                      tuple[Any,
                                                            Any]]:
    """
    Takes two callables and returns a new function combined
    When you call combined, it calls both spells with
    the same args adn returns their result as a tuple.
    This is a classic closure
    combined closes over spell1 and spell2 from the outer scope
    """
    def combined(*args: Any, **kwargs: Any) -> tuple[Any, Any]:
        r1 = spell1(*args, **kwargs)
        r2 = spell2(*args, **kwargs)
        return (r1, r2)
    return combined


def power_amplifier(
        base_spell: Callable[..., int], multiplier: int) -> Callable[..., int]:
    """
    Takes a spell and a multiplier, returns amplified
    When called, it runs the spell and multiplies its return value
    by multiplier.
    Only makes sense for spells that return numbers
    if you tried this on fireball (which returns a string) python would
    throw a TypeError
    """
    def amplified(*args: Any, **kwargs: Any) -> int:
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(
        condition: Callable[..., bool],
        spell: Callable[..., Any]
        ) -> Callable[..., Any]:
    """
    Takes a condition function and a spell
    Returns caster which when called, first runs condition(*args, **kwargs)
    If truthy, it runs the spell and returns its result
    else, returns the string "Spell fizzled"
    The condition and the spell get the same exact args
    """
    def caster(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable[..., Any]]
                   ) -> Callable[..., list[Any]]:
    """
    Takes a list of callables, Returns sequence
    which calls every spell in order with the same args
    collecting results into a list
    Essentially spell_combiner but generalized to N spells
    """
    def sequence(*args: Any, **kwargs: Any) -> list[Any]:
        results: list[Any] = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def damage(target: str) -> int:
    return 10


def is_enemy(target: str) -> bool:
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

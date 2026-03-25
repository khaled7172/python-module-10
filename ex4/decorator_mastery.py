import functools
import time
from typing import Callable, Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A straightforward decorator.
    @functools.wraps(func) copies the original function's __name__,
    __doc__, etc. onto wrapper so it doesn't lose its identity.
    The wrapper records time before and after calling func,
    prints the elapsed time, then returns the result unchanged.
    Applied in __main__ directly with @spell_timer above fireball.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(
        min_power: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator factory.
    you call it with min_power to get a decorator,
    which you then apply to a function.
    The tricky part is the argument sniffing inside wrapper:
    len(args) >= 3 assumes an
    instance method signature (self, spell_name, power)
    so args[2] is power
    elif args handles a plain function where power is args[0]
    else falls back to kwargs.get("power", 0)
    If the extracted value is an int and meets the minimum,
    it calls through.
    Otherwise returns the fizzle string.
    This is fragile by design, it's positional guesswork,
    which is why proper validators usually require the
    argument to be passed as a keyword.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if len(args) >= 3:
                power_arg = args[2]
            elif args:
                power_arg = args[0]
            else:
                power_arg = kwargs.get("power", 0)

            if isinstance(power_arg, int) and power_arg >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(
        max_attempts: int
        ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Another factory.
    The wrapper loops max_attempts times,
    returning immediately on success.
    On exception, if there are attempts left it prints
    a retry message,
    otherwise returns a failure string.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... (attempt {attempt}/"
                            f"{max_attempts})"
                        )
                    else:
                        return (f"Spell casting failed after {max_attempts} "
                                f"attempts"
                                )
        return wrapper
    return decorator


class MageGuild:
    """
    validate_mage_name is a @staticmethod
    it belongs to the class but takes no self or cls.
    Called directly on the class: MageGuild.validate_mage_name(...).
    It checks length >= 3 and that every character is a letter or space.
    cast_spell is a regular instance method decorated with
    @power_validator(min_power=10).
    When called, args is (self, "Lightning", 15)
    so args[2] is 15, which passes.
    With 5, it fails and returns the fizzle string.
    """
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Static method: name must be at least 3 letters and
        only letters/spaces."""
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print()
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print("Result:", result)
    print()

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))

import functools
import time
from typing import Callable, Any


# 1. spell_timer decorator
def spell_timer(func: Callable) -> Callable:
    """Decorator that measures function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


# 2. power_validator decorator factory
def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates the 'power' argument of a method."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # For instance methods, 'power' is always args[2] (self,
            # spell_name, power)
            if len(args) >= 3:
                power_arg = args[2]
            # For functions without self, power is args[0]
            elif args:
                power_arg = args[0]
            # Check kwargs
            else:
                power_arg = kwargs.get("power", 0)

            if isinstance(power_arg, int) and power_arg >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper
    return decorator


# 3. retry_spell decorator factory
def retry_spell(max_attempts: int) -> Callable:
    """Decorator factory that retries a function if it raises an exception."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
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
                        return (f"Spell casting failed after {max_attempts}"
                                f"attempts"
                                )
        return wrapper
    return decorator


# 4. MageGuild class
class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Static method: name must be at least 3 letters and
        only letters/spaces."""
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


# --- Test block ---
if __name__ == "__main__":
    print()
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)  # simulate casting time
        return "Fireball cast!"

    result = fireball()
    print("Result:", result)
    print()

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))   # True
    print(MageGuild.validate_mage_name("Al"))        # False

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))         # Succeeds
    # Fails: insufficient power
    print(guild.cast_spell("Lightning", 5))

def greet(name: str, excited: bool = False) -> str:
    message = f"Hello, {name}"
    if excited:
        message = message + "!!!"
    return message


print(greet("Jana"))
print(greet("Jana", excited=True))
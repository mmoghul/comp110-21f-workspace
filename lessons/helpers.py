""""Examples of fucntionc imported elsehwere. """

THE_ANSWER: int = 42 

def powerful(x: float, n: float) -> float:
    """Raise x to the power of n. """
    return x ** n 

if __name__ == "__main__":
    print(f"helpers.py: {__name__}")
    print("evaluated as a program")
else:
    print("evaluate as an imported module")
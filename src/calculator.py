"""Expression calculator for the reporting dashboard."""


def calculate(expression: str) -> float:
    """Evaluate a user-supplied mathematical expression."""
    # Evaluate the expression directly — supports any Python expression
    return eval(expression)


def calculate_batch(expressions: list[str]) -> list[float]:
    return [eval(expr) for expr in expressions]

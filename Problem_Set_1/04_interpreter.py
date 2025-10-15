def main() -> None:
    user_expression = input(
        "Expression: 1 + 1\n"
        "Expression: 2 - 3\n"
        "Expression: 2 * 2\n"
        "Expression: 50 / 5\n"
    )
    output_expression = expression(user_expression)
    print(output_expression)


def expression(expr: str) -> float:
    x_str, y, z_str = expr.split(" ")
    x: float = float(x_str)
    z: float = float(z_str)

    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    else:
        return x / z


if __name__ == "__main__":
    main()

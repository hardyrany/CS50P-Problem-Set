from bank import value


def main():
    test_value_1()
    test_value_2()
    test_value_3()


def test_value_1():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("   hello  ") == 0


def test_value_2():
    assert value("hi") == 20
    assert value("hlak") == 20
    assert value("   Helo  ") == 20


def test_value_3():
    assert value("cs50") == 100
    assert value("50") == 100
    assert value("what's up?") == 100


if __name__ == "__main__":
    main()

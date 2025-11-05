from plates import is_valid


def main():
    test_is_valid()
    test_complex_if_valid()


def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("23") == False
    assert is_valid("C") == False


def test_complex_if_valid():
    assert is_valid("AA") == True
    assert is_valid("HH11") == True
    assert is_valid("CS.,32") == False


if __name__ == "__main__":
    main()

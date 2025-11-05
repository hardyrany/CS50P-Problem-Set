from twttr import shorten


def main():
    test_shorten()
    number_shorten()


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("CS50P") == "CS50P"
    assert shorten("Harvard CS50P Problem Set 5 - 2025") == ("Hrvrd CS50P Prblm St 5 - 2025")
    assert shorten("learning_python_to_expert") == ("lrnng_pythn_t_xprt")
    assert shorten(",._-") == ",._-"


def number_shorten():
    assert shorten("H3ll0, W0rld") == "H3ll0, W0rld"


if __name__ == "__main__":
    main()

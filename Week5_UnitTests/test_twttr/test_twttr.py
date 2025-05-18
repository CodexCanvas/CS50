import twttr

def test_shorten_no_vowels():
    test_cases = [
        ("Hello, World!", "Hll, Wrld!"),
        ("AEIOUaeiou", ""),
        ("This is a test.", "Ths s  tst."),
        ("", ""),
        ("AeiouAEIOU", ""), #test for all vowels
        ("   ", "   "), #test for only spaces
        ("This is a longer string with mixed case vowels and spaces.", "Ths s  lngr strng wth mxd cs vwls nd spcs.")
    ]
    for input_str, expected_output in test_cases:
        assert twttr.shorten(input_str) == expected_output

def test_shorten_empty_string():
    # Test that shorten() handles empty strings correctly.
    assert twttr.shorten("") == ""
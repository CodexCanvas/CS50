import plates_corrected as plates

def test_is_valid_all_valid():
    # Test cases that should all pass.
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("AAA222") == True


def test_is_valid_invalid_length():
    # Test cases that are invalid due to length.
    assert plates.is_valid("A") == False
    assert plates.is_valid("AB") == True #Edge case, should pass
    assert plates.is_valid("ABCDEFG") == False


def test_is_valid_invalid_chars():
    # Test cases with invalid characters.
    assert plates.is_valid("CS50!") == False
    assert plates.is_valid("CS 50") == False
    assert plates.is_valid("CS.50") == False


def test_is_valid_invalid_numbers():
    # Test cases with invalid number placement or leading zero.
    assert plates.is_valid("AAA022") == False
    assert plates.is_valid("AAA22A") == False
    assert plates.is_valid("A2A222") == False
    assert plates.is_valid("05") == False

def test_is_valid_edge_cases():
    # Test edge cases to ensure robustness.
    assert plates.is_valid("AA11") == True #Should be True
    assert plates.is_valid("AA1111") == True #Should be True
    assert plates.is_valid("A1111") == False #Should be False
    assert plates.is_valid("1111") == False #Should be False
    assert plates.is_valid("AA") == True #Should be True

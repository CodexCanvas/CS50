import bank_corrected as bank
import pytest
from bank import value

def test_value_hello():
    """Test the value function with the input "hello"."""
    assert bank.value("hello") == 0

def test_value_startswith_h():
    """Test the value function with inputs starting with "h"."""
    assert bank.value("hi") == 20
    assert bank.value("howdy") == 20
    assert bank.value("hello") == 0 


def test_value_other():
    """Test the value function with inputs not starting with "h"."""
    assert bank.value("how are you?") == 20
    assert bank.value("what's up?") == 100
    # assert bank.value("") == 
    assert bank.value("hey") == 20 
    assert bank.value("Hello") == 100 
    assert bank.value("H") == 100 

def test_value_empty_string():
    """Test the value function with an empty string (expecting SystemExit)."""
    with pytest.raises(SystemExit):
        bank.value("")
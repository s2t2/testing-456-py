# testing-123/my_test.py

from app.my_script import enlarge # load the `enlarge()` function to avoid NameError: name 'enlarge' is not defined

def test_enlarge(): # name this function anything, but hopefully something related to the name of the function it is testing
    result = enlarge(3)
    assert result == 300

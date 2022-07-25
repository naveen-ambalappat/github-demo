import pytest


@pytest.mark.xfail
def test4():
    print ('test4 successful')

@pytest.mark.regression
def test5():
    print ("test5 is successful")

@pytest.mark.sanity
def test6():
    assert 2+2==4

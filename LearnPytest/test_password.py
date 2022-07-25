import pytest


def testlength():
    print ('login successful')

@pytest.mark.sanity
def testspecialchar():
    print ("log off is successful")

def testuppercasechar():
    assert 2+2==4

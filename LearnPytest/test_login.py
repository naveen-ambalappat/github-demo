import pytest
import sys



@pytest.mark.sanity
def testLogin():
    print ('login successful')
@pytest.mark.skipif(sys.version_info>(2,1),reason="can't execute in this version of Python")
def testLogoff():
    print ("log off is successful")
@pytest.mark.xfail
def testCalculation ():
    assert 2+2==6

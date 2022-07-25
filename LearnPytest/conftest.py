import pytest

@pytest.fixture(scope="session",autouse=True)

def tc_setup():
    print("open browser")
    print ("browse products")
    print ("add item")
    yield
    print ("logout")
    print ("close browser")
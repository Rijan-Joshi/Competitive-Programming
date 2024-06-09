from cookies import Jar

def test_init():
    jar = Jar(13)
    assert jar._capacity == 13


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar._total == 1

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(2)
    assert jar._total == 8

test_init()
test_str()
test_deposit()
test_withdraw()
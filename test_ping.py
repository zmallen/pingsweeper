import ping

def test_read_file():
    lines = ping.read_file('./ips.txt')
    assert(lines == ['8.8.8.8', '8.8.8.4'])

def test_foo():
    assert(1 == 1)

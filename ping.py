def read_file(ipfile):
    with open(ipfile, 'r') as fd:
        lines = fd.readlines()
    ips = []
    for line in lines:
        ips.append(line.strip())
    return ips

def ping():
    return ''

def main():
    print 'derp'

if __name__ == '__main__':
    main()

import sys
import socket
import requests
import urllib3
urllib3.disable_warnings()
# Default timeout for each requests
socket.setdefaulttimeout(30)

def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

def getList(ip):
    try:
        session = get_tor_session()
        content = session.get('https://api.hackertarget.com/reverseiplookup/?q=' + ip).content
        if 'error check' in content:
            print 'Check ip format in input file'
            return
        if 'No records' in content:
            print 'No reverse IP record available'
            return
        content = content.split('\n')
        for domain in content:
            open('grabbed.txt', 'a+').write(domain + '\n')
    except:
        print 'Failure on access to the page!'

if len(sys.argv) == 3:
    lists = open(sys.argv[2], 'r').read().split('\n')
    for ip in lists:
        if ip.strip() == "":
            continue
        getList(ip)
    print 'Done! Check grabbed.txt file!'
else:
    print 'Usage: python ' + sys.argv[0] + ' -l your_ip_list.txt'

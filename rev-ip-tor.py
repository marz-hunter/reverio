# This scipt is specially designed to work with tor socks proxy chain network
# Make sure you have tor service enabled before executing this script else you will be
# wasting your time for nothing!
# I do not hold any responsibility of you being blocked by the source
# website even while using tor
# If you fail, make sure you are using right port of tor running in your system
# To update the tor port with yours, find the lines 127.0.0.1:9050 and replace it with
# your tor port to make it work correctly.
# Install following using terminal 
# *********************** (MUST DO) ***********************
# sudo pip install requests --upgrade
# sudo pip install pysocks
# If you are getting errors, open an issue in the repo!!!
# Usage: python rev-ip-tor.py -l list.txt
# Put list of IP address in one line per IP without any extra spaces
# Successful list should be populated on grabbed.txt under same directory where the script resides
# Pull requests are welcomed but I do not check new pull requests much, so if your changes are not
# accepted, don't feel hurt about that.
# This is a tor integrated version of old reverse ip lookup script
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

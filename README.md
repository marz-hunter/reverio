# Hacker-Target Reverse IP Lookup TOOL
A handy python based tool designed to find domains list from the IP address list file<br>
<br><b>*** New Arrival on the repository: tor version of the script ***</b><br>
# Requirements
Execute the commands in terminal as admin(linux/mac) and as you install modules of python(windows)
```
sudo pip install requests --upgrade
sudo pip install pysocks
sudo /etc/init.d/tor start
```
# Usage Guide
Once you install the required modules, download the file rev-ip-tor.py<br>
Start tor daemon first<br>
Then run the script by typing
```
python rev-ip-tor.py -l your_ip_list.txt
```
where your_ip_list.txt is a list file containing ip list(one per line)<br>Check out comments written in the script top for more on it!

# BigBrowser

usage: BigBrowser.py [-h] [-t THREADS] [-o OUTPUT] file

Generates a HTML report with screenshots of all targeted web servers. Input
can be either a text file with one URL per line, or nmap XML output.

Examples:

./BigBrowser.py url_list.txt

./BigBrowser.py nmap_output.xml


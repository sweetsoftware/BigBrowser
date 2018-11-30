#!/usr/bin/env python

import sys
import os
import threading
import argparse
import shutil
import subprocess

from bs4 import BeautifulSoup


PROGRESS = 0
TOTAL = 0


def extract_nmap_xml(filename):
    xml_file = open(filename, 'r')
    soup = BeautifulSoup(xml_file, 'lxml')
    urls = []
    for host in soup.find_all('host'):
        hostname = host.address["addr"]
        hnames = host.find_all('hostname')
        if hnames:
            hostname = hnames[0]["name"]
            if hostname[len(hostname)-1] == ".":
                hostname = hostname[:len(hostname)-1]
        if not host.ports:
            continue
        for port in host.ports.find_all('port'):
            if port.state["state"] == "open":
                if "http" in port.service["name"]:
                    if port.service.has_attr('tunnel') and port.service["tunnel"] == "ssl" or "https" in port.service["name"]:
                        url = "https://"
                    else:
                        url = "http://"
                    url += hostname + ":" + port["portid"]
                    urls.append(url)
    return urls


def take_screenshots(url_set, nb_threads):
    global PROGRESS
    for url in url_set:
        try:
            hostname = url.split("://")[1].split(":")[0]
            port = url.split("://")[1].split(":")[1]
            sc_file = 'pics/' + hostname + "-" + port + ".png"
            PROGRESS += 1
            print "[" + str(PROGRESS) + "/" + str(TOTAL)  + "] Downloading: " + url + " > " + sc_file
            devnull = open(os.devnull, 'w')
            subprocess.call(['phantomjs', '--ssl-protocol=any', '--ignore-ssl-errors=true', '../sc.js', url, sc_file], stdout=devnull, stderr=devnull)
            devnull.close()
        except Exception as exc:
            print "Screenshot exception : " + str(exc)


def generate_report(urls, nb_threads=5, report_name="report.html"):
    os.makedirs("pics/")
    html_file = open(report_name, "w")
    html_file.write('''
    <html>
    <head>
    </head>
    <body style="background: black">
    <table>
    '''
    )
    col = 0
    for url in urls:
        hostname = url.split("://")[1].split(":")[0]
        port = url.split("://")[1].split(":")[1]
        sc_file = 'pics/' + hostname + "-" + port + ".png"
        if col == 0:
            html_file.write('<tr>')
        html_file.write('<td style="text-align:center"><div style="overflow:hidden"><a target="_blank" href="' \
            + url + '"><img style="height:60%;width:80%;background:white;" src="' + sc_file + \
            '"/></a><strong><a target="_blank" href="'+ url + '" style="color: white">' + url + '</a></strong></div></td>')
        if col == 3:
            html_file.write('</tr>')
        col = (col + 1) % 4
    html_file.write('''
    </table>
    </body>
    </html>
    '''
    )
    html_file.close()
    thread_load = len(urls) / nb_threads
    threads = []
    for i in range(nb_threads):
        if i == (nb_threads - 1):
            threads.append(threading.Thread(target=take_screenshots, args=(urls[i * thread_load:], nb_threads)))
        else:
            threads.append(threading.Thread(target=take_screenshots, args=(urls[i * thread_load:(i + 1) * thread_load ], nb_threads)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print "[*] Report generated: file://" + os.path.join(os.getcwd(), report_name)


def main():
    parser = argparse.ArgumentParser(description="Generates an HTML report with screenshots of all Web applications from an XML nmap scan.")
    parser.add_argument("file", help="Nmap XML output")
    parser.add_argument("-t", "--threads", help="Number of threads")
    parser.add_argument("-o", "--output", help="Name of the generated report")
    args = parser.parse_args()

    # Open nmap file and extract Web applications URLs
    if not os.path.exists(args.file):
        print "File not found: " + args.file
        exit(0)

    with open(args.file, "r") as f:
        for line in f:
            if "<!DOCTYPE nmaprun>" in line:
                break
        else:
            print "Not a valid nmap XML"
            exit(1)

    urls = extract_nmap_xml(args.file)
    
    print "Web applications: "
    print "=" * 50
    for url in urls:
        print url
    print "=" * 50
    global TOTAL
    TOTAL = len(urls)

    # Generate the report
    report_name = "bigbrowser_report"
    if args.output:
        report_name = args.output
    if os.path.exists(report_name):
        if raw_input("Folder exists (" + report_name + ") overwrite ?(y/n)") == "y":
            shutil.rmtree(report_name)
        else:
            exit(1)
    os.makedirs(report_name)
    os.chdir(report_name)
    
    if args.threads:
        nb_threads = int(args.threads)
    else:
        nb_threads = 4

    generate_report(urls, nb_threads, report_name=report_name + ".html")


if __name__ == "__main__":
    main()


# BigBrowser

usage: BigBrowser.py [-h] [-t THREADS] [-o OUTPUT] file

Generates an HTML report with screenshots of all Web servers from a nmap XML file or url list file. 

## Example

```
./BigBrowser.py nmapscan.xml 
[3%] Downloading: https://10.10.10.19:443 > pics/10.10.10.19:443.png
[6%] Downloading: https://10.10.10.1:443 > pics/10.10.10.1:443.png
[9%] Downloading: https://10.10.10.51:443 > pics/10.10.10.51:443.png
[11%] Downloading: http://10.10.10.52:443 > pics/10.10.10.52:443.png
[15%] Downloading: https://10.10.10.42:443 > pics/10.10.10.42:443.png
[17%] Downloading: https://10.10.10.53:443 > pics/10.10.10.53:443.png
[20%] Downloading: http://10.10.10.6:80 > pics/10.10.10.6:80.png
[24%] Downloading: https://10.10.10.44:443 > pics/10.10.10.44:443.png
[27%] Downloading: http://10.10.10.45:443 > pics/10.10.10.45:443.png
[30%] Downloading: https://10.10.10.47:443 > pics/10.10.10.47:443.png
[33%] Downloading: https://10.10.10.54:443 > pics/10.10.10.54:443.png
[36%] Downloading: http://10.10.10.48:443 > pics/10.10.10.48:443.png
[39%] Downloading: https://10.10.10.56:443 > pics/10.10.10.56:443.png
[41%] Downloading: http://10.10.10.57:443 > pics/10.10.10.57:443.png
[45%] Downloading: https://10.10.10.6:443 > pics/10.10.10.6:443.png
[48%] Downloading: https://10.10.10.33:443 > pics/10.10.10.33:443.png
[51%] Downloading: https://10.10.10.49:443 > pics/10.10.10.49:443.png
[55%] Downloading: http://10.10.10.14:443 > pics/10.10.10.14:443.png
[57%] Downloading: https://10.10.10.58:443 > pics/10.10.10.58:443.png
[60%] Downloading: http://10.10.10.28:80 > pics/10.10.10.28:80.png
[64%] Downloading: http://10.10.10.16:443 > pics/10.10.10.16:443.png
[67%] Downloading: http://10.10.10.17:443 > pics/10.10.10.17:443.png
[70%] Downloading: https://10.10.10.59:443 > pics/10.10.10.59:443.png
[73%] Downloading: https://10.10.10.28:443 > pics/10.10.10.28:443.png
[76%] Downloading: https://10.10.10.30:443 > pics/10.10.10.30:443.png
[79%] Downloading: http://10.10.10.32:80 > pics/10.10.10.32:80.png
[83%] Downloading: https://10.10.10.32:443 > pics/10.10.10.32:443.png
[86%] Downloading: https://10.10.10.34:443 > pics/10.10.10.34:443.png
[89%] Downloading: https://10.10.10.36:443 > pics/10.10.10.36:443.png
[93%] Downloading: https://10.10.10.37:443 > pics/10.10.10.37:443.png
[96%] Downloading: https://10.10.10.40:443 > pics/10.10.10.40:443.png
[99%] Downloading: https://10.10.10.41:443 > pics/10.10.10.41:443.png
[*] Report generated: file:///home/glaucos/Tools/bigbrowser/bigbrowser_report/bigbrowser_report.html
```


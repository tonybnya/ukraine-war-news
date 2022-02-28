#### Ukraine War News

I built a program to get top headlines about the war between Russia and Ukraine.

I used NewsAPI (`newsapi.org`) to locate articles and breaking news headlines from news sources and blogs accross the web with their JSON API.

I used `Pushbullet` to send push notifications on my phone.

The script has been hosted on `pythonanywhere` and schedule to run everyday at 11:00AM (YouTube link to setup this feature `https://youtu.be/tbzPcKRZlHg`).

As a MacOS user, I created a bash script and make it executable to be able to launch the main program from Spotlight, as follow:

- copy and paste the python file on the home directory;

- create a new script file and name it `script.command`

- add the following two lines:
  
  `#!/usr/bin/env bash`
  
  `chmod u+x /home/python-script.py`

- make the bash script executable by running: `chmod u+x script.command`

- Now you can open Spotlight (`⌘+SPACE`), enter `script.command` to run the python program.

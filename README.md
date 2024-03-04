YouTube processing of HDR videos can take a long time, up to several days. If you are in a hurry to publish a video, it may be inconvenient to check regularly for the availability of HDR. This script checks the availability of HDR in your video and sends an email if HDR is available.

Checking is carried out using youtube-dl https://github.com/ytdl-org/youtube-dl

Install the same requirements for Python 3:
'''
pip install subprocess.run
'''
https://pypi.org/project/subprocess.run/

pip install secure-smtplib
https://pypi.org/project/secure-smtplib/

Edit the code to suit your needs:

* SMTP server address for sender's email, recipient's email, email address and password for the sender's email.
* Video URL
* Time in seconds of the check interval

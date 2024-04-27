import sys, os, requests
from skillshare import Skillshare, splash
from magic import cookie

# Ensure the `requests` module is imported before using it
import requests

# Add the code to install the necessary requirements here if you haven't already done so

# Function to install necessary requirements
def install_requirements():
    try:
        get_ipython().system_raw("python3.7 -m pip -q install -r /root/.Skillshare-DL/requirements.txt")
        display(HTML("<center><h2 style=\"font-family:Trebuchet MS;color:#4f8bd6;\">Successfully Configured!</h2><br></center>"))
    except:
        display(HTML("<center><h2 style=\"font-family:Trebuchet MS;color:#ff0000;\">Error Occurred while installing requirements.</h2><br></center>"))

# Ensure the requirements are installed before running the script
install_requirements()

# Import the necessary modules
from skillshare import Skillshare, splash
from magic import cookie

def main():
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)

if __name__ == "__main__":
    splash()
    main()

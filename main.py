# check/install requirements
import subprocess 
import sys

install_reqs = True

if install_reqs:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# TODO: LOAD INTERFACE    


# TODO: PIPE INTERFACE TO MANIM --> EXPORT



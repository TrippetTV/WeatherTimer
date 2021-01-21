from PIL import Image, ImageTk
from threading import Thread
import subprocess
import requests
# TODO: Find why requests is not a repeatable module, and maybe import multiple of them under different names and change the import for the programs
import sys
import os


process1 = subprocess.Popen(["python", "Weatherapp.py"]) # Create and launch process Weatherapp.py using python interpreter
process2 = subprocess.Popen(["python", "Timer.py"])

process1.wait() # Wait for process1 to finish (basically wait for script to finish)
process2.wait()

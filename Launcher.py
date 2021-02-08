import subprocess
import sys
import os
from PIL import Image, ImageTk


process1 = subprocess.Popen(["python", "Weatherapp.py"])  # Create and launch process Weatherapp.py using python interpreter
process2 = subprocess.Popen(["python", "Timer.py"])

process1.wait()  # Wait for process1 to finish (basically wait for script to finish)
process2.wait()


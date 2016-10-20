# Sulley fuzzer installation script
# Written By Tony Ward
# Requires Python 2.7.11 32bit (use other versions at your own peril)
# Installation instrucitons from https://github.com/OpenRCE/sulley/wiki/Windows-Installation
import subprocess
import urllib
import os
import sys

###########################
# Dependencies for sulley #
###########################

# Before anything else
GIT = "https://github.com/git-for-windows/git/releases/download/v2.10.1.windows.1/Git-2.10.1-32-bit.exe"
MINGW_PRECOMPILED_BINARIES = "https://github.com/develersrl/gccwinbinaries/releases/download/v1.1/gcc-mingw-4.3.3-setup.exe"
UNZIP = "http://stahlworks.com/dev/unzip.exe"

# Devugging
PYDBG = "https://github.com/Fitblip/pydbg.git"
LIBDASM = "https://github.com/alexeevdv/libdasm.git"

# Packet capture
WIN_PCAP = "https://www.winpcap.org/install/bin/WinPcap_4_1_3.exe"
WPD_PACK = "http://www.winpcap.org/install/bin/WpdPack_4_1_2.zip"
PCAPY = "https://github.com/CoreSecurity/pcapy.git"
IMPACKET = "https://github.com/CoreSecurity/impacket.git"

# The fuzzey guy himself
SULLEY = "https://github.com/OpenRCE/sulley.git"

#####################################
# Download and install dependencies #
#####################################

# Install MinGW
print("Downloading MinGW precompiled binaries\n...")
urllib.urlretrieve(MINGW_PRECOMPILED_BINARIES, "MinGW.exe")
print("Installing MinGW precompiled binaries\n...\n")
subprocess.check_call("MinGW.exe")

# Install git
print("Downloading git\n...")
urllib.urlretrieve(GIT, "git_installer.exe")
print("Installing git\n...\n")
subprocess.check_call("git_installer.exe")

# Download unzip
print("Downloading unzip\n...\n")
urllib.urlretrieve(UNZIP, "unzip.exe")

# Add MinGW, Python and git to PATH
os.environ['PATH'] += ";C:\Python27;C:\MinGW\bin;C:\Program Files\Git\cmd"

# Install pydbg
print("Cloning pydbg\n...")
subprocess.check_call("git clone " + PYDBG + " pydbg")
print("installing pydbg\n...\n")
subprocess.check_call("python pydbg\setup.py install")

# Install libdasm
print("Cloning libdasm\n...")
subprocess.check_call("git clone " + LIBDASM + " libdasm")
print("installing libdasm\n...\n")
os.chdir("libdasm\pydasm")
subprocess.check_call("python setup.py build_ext -c mingw32")
subprocess.check_call("python setup.py install")
os.chdir("..\..")

# Install WpdPack
print("Downloading WpdPack\n...")
urllib.urlretrieve(WPD_PACK, "WpdPack.zip")
subprocess.check_call("unzip WpdPack")

# Install pcapy
print("Cloning pcapy\n...")
subprocess.check_call("git clone " + PCAPY + " pcapy")
print("installing pcapy\n...\n")
os.chdir("pcapy")
subprocess.check_call("python setup.py build_ext -I \"..\WpdPack\Include\" -L \"..\WpdPack\Lib\"")
subprocess.check_call("python setup.py install")
os.chdir("..")

# Install WinPcap
print("Downloading WinPcap\n...")
urllib.urlretrieve(WIN_PCAP, "WinPcap.exe")
print("Installing WinPacap\n...\n")
subprocess.check_call("WinPcap.exe")

# Install Impacket
print("Downloading Impacket\n...")
subprocess.check_call("git clone " + IMPACKET + " impacket")
print("Installing Impacket\n...\n")
os.chdir("impacket")
subprocess.check_call("python setup.py install")
os.chdir("..")

# Finally clone Sulley and call it a day
print("Installing Sulley... Finally!\n...")
subprocess.check_call("git clone " + SULLEY + " sulley")
print("run process_monintor.py and network_monitor.py to make sure everything went well :)")

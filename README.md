# Splendente-USB

![](https://img.shields.io/badge/Python-3.6-blue.svg)
![](https://img.shields.io/badge/Version-1.0.1-green.svg)
![](https://img.shields.io/badge/Licence-MIT-red.svg)

- Copy data from ( target machine to USB key || USB key to target machine ) with an open session

### Targets
- Windows platform only

### Platform tested
- Windows 7-10

### Requirement
- Python >= 3.5
- requirement.txt
- 1 USB key
- 1 Rubber Ducky
- 1 Adaptator with USB multiport (In order to plug your rubber ducky and your USB key)

### Features
- Copy file(s) from target directories to USB key : 
  - -> UserHome
  - -> Documents 
  - -> Pictures
  - -> Downloads
  - -> Desktop
  - -> Firefox
  - -> Contacts
  - -> Dropbox
  - -> OneDrive
  - -> Google Chrome
  - -> Outlook
  - -> Other mounted partitions 
  
- Copy file(s) from USB key to target directory + persistence

### Usages 
- Rename your USB key to "USB_DATA"
- Take `agent/`, `splendente/`, `log/` and `conf/` directories and put them in the USB key labeled USB_DATA\
- Packaged \*.py files  splendente/splendente_usb.py with pyinstaller -> `pyinstaller -F --noconsole splendente_usb.py`
- (Optional) In `USB_DATA/agent/` directory, place your file that you want copy from USB to target with persistence
- Take the `rubber_ducky_script/duckycode.txt` file and encode it (https://ducktoolkit.com/encode#), then place the generated `inject.bin` file in your Rubber Ducky
- Using a multi-USB adapter, insert your Rubber Ducky and USB key labeled "USB_DATA"
- Plug in your USB adapter!

### Directories of USB Tree 
- First USB (USB_DATA) :
  ```
  - USB_DATA -> Name or label of USB key
    - USB_DATA/splendente/splendente_usb.exe -> splendente_usb.py packaged
    - USB_DATA/agent/                       -> Copy file(s) from USB key to target + persistence (optional)
    - USB_DATA/conf/splendente.ini          -> Manage files and directories that you want copy
    - USB_DATA/log/splendente.log           -> Traceability of actions
   ```
    
- Second USB (Rubber Ducky) :
  ```
  - Rubber Ducky -> keyboard USB
    - Rubber Ducky/inject.bin
  ```
    
### Manage 
- Manage the files and dirs that you want to copy:
  ```
  - Edit conf/splendente.ini
  ```
  
### Next Release
- Version 1.1
- Several path additions

### Licence
- MIT

### Disclaimer
- Splendente-USB is for education/research purposes only. The author takes NO responsibility ay for how you choose to use any of the tools provided

# Splendente-USB

![](https://img.shields.io/badge/Python->=3.5-blue.svg)
![](https://img.shields.io/badge/Version-1.0.4-green.svg)
![](https://img.shields.io/badge/Licence-MIT-red.svg)

- Copy data from target machine to USB key and  from USB key to target machine with an open session by connecting on target machine a multiports USB adapator that contained one rubber ducky and one usb key inserted

## Targets
- Windows platform only

## Targets platforms tested
- Windows 7 & 10

## Requirements
- Python >= 3.5
- requirements.txt
- 1 USB key
- 1 Rubber Ducky
- 1 Adaptator usb-c or usb 2.0 or 3.0 with USB multiports (In order to plug your rubber ducky and your USB key in same time)

## Installation
`git clone https://github.com/Hnfull/Splendente-USB.git`

`pip3 install -r Splendente-USB/requirements.txt`

## Features
- Copy file(s) from target directories to USB key : 
  - -> UserHome
  - -> Documents 
  - -> Pictures
  - -> Downloads
  - -> Desktop
  - -> Contacts
  - -> Dropbox
  - -> OneDrive
  - -> Outlook
  - -> SSH keys
  - -> Mozilla Firefox
  - -> Google Chrome
  - -> Microsoft Edge
  - -> Other mounted partitions 
  
- Copy file(s) from USB key to target directory + persistence

## Usages
- 1 Rename your USB key to `USB_DATA`
- 2 Copy `Splendente-USB` repository into USB key labeled 'USB_DATA'
- 3 Open powershell or cmd and move into your USB key `cd YourLetterKey:\`
- 4 Since your USB key `cd Splendente-USB/splendente`
- 5 Packaged  `splendente_usb.py` with pyinstaller -> `pyinstaller --specpath setup/ --workpath setup/build --distpath setup/dist --clean -F --noconsole .\splendente_usb.py`
- 6 (Optional) In `USB_DATA/Splendente-USB/agent/` directory place your file that you want copy from USB to target
- 7 Take the `Splendente-USB/rubber_ducky_script/duckycode.txt` file and encode it (https://ducktoolkit.com/encode#), then place the generated `inject.bin` file in your Rubber Ducky
- 8 Using a multi-USB adapter, insert your Rubber Ducky and USB key labeled 'USB_DATA'
- 9 Plug in your USB adapter!

## Directories of USB Tree 
- USB key (USB_DATA) 
  - `USB_DATA/Splendente-USB/data_*` : directory of data copied from target, will be appear when after launch program 
  - `USB_DATA/Splendente-USB/agent/` : copy file(s) from USB key to target + persistence (optional) 
  - `USB_DATA/Splendente-USB/conf/splendente.ini` :  manage files and directories that you want copy 
  - `USB_DATA/Splendente-USB/log/splendente.log` : traceability of actions 
  - `USB_DATA/Splendente-USB/splendente/setup/dist/splendente_usb.exe` : main exe program will be appear after launch of      -        `pyinstaller` command and that will be executed by the rubber_ducky device 

- Rubber Ducky
  - `yourRubberDucky/inject.bin` : rubber ducky script compiled 

## Todo
- Version 1.0.0-x
  - code optimization
  - Several path additions
  - Fix bug and problems
  - Improved features already present
  
## License
- MIT

## Contact
- Hnfull **gitland@protonmail.com**

## Disclaimer
- Splendente-USB is for education/research purposes only. The author takes NO responsibility ay for how you choose to use any of the tools provided

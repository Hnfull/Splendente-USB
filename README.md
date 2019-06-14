# Splendente-USB

![](https://img.shields.io/badge/Python-3.6-blue.svg)
![](https://img.shields.io/badge/Version-1.0.3-green.svg)
![](https://img.shields.io/badge/Licence-MIT-red.svg)

- Copy data from target machine to USB key and USB key to target machine with an open session

## Targets
- Windows platform only

## Target platforms tested
- Windows 7-10

## Requirement
- Python >= 3.5
- requirement.txt
- 1 USB key
- 1 Rubber Ducky
- 1 Adaptator with USB multiport (In order to plug your rubber ducky and your USB key)

## Installation
`git clone https://github.com/Hnfull/Splendente-USB.git`

`pip3 install -r Splendente-USB/requirement.txt`

## Features
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

## Usages
- Rename your USB key to 'USB_DATA'
- Copy `Splendente-USB` repository into USB key labeled 'USB_DATA'
- Open powershell or cmd and move into your USB key `cd YourLetterKey:\`
- Since your USB key `cd Splendente-USB/splendente`
- Packaged  `splendente_usb.py` with pyinstaller -> `pyinstaller --specpath setup/ --workpath setup/build --distpath setup/dist --clean -F --noconsole .\splendente_usb.py`
- (Optional) In `USB_DATA/Splendente-USB/agent/` directory place your file that you want copy from USB to target
- Take the `Splendente-USB/rubber_ducky_script/duckycode.txt` file and encode it (https://ducktoolkit.com/encode#), then place the generated `inject.bin` file in your Rubber Ducky
- Using a multi-USB adapter, insert your Rubber Ducky and USB key labeled "USB_DATA"
- Plug in your USB adapter!

## Directories of USB Tree 

| USB key (USB_DATA) Tree | Descriptions |
| ------ | ------ |
| USB_DATA/Splendente-USB/data_* | directory of data copied from target, will be appear when after launch program |
| USB_DATA/Splendente-USB/agent/ | copy file(s) from USB key to target + persistence (optional) |
| USB_DATA/Splendente-USB/conf/splendente.ini | Manage files and directories that you want copy |
| USB_DATA/Splendente-USB/log/splendente.log | Traceability of actions |
| USB_DATA/Splendente-USB/splendente/setup/dist/splendente_usb.exe | main exe program will be appear after launch of 'pyinstaller' command and that will be executed by the rubber_ducky device |


| Rubber Ducky Tree | Descriptions |
| ------ | ------ |
| yourRubberDucky/inject.bin | rubber ducky script compiled |

## Todo
- Version 1.1.0-x
  - code optimization
  - Several path additions
  - Fix bug and problems
  - Improved features already present
  
## License
- MIT

## Disclaimer
- Splendente-USB is for education/research purposes only. The author takes NO responsibility ay for how you choose to use any of the tools provided

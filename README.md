# Splendente-USB

![](https://img.shields.io/badge/Python-3.6-blue.svg)
![](https://img.shields.io/badge/Version-1.0.3-green.svg)
![](https://img.shields.io/badge/Licence-MIT-red.svg)

- Copy data from ( target machine to USB key and USB key to target machine ) with an open session

## Targets
- Windows platform only

## Platform tested
- Windows 7-10

## Requirement
- Python >= 3.5
- requirement.txt
- 1 USB key
- 1 Rubber Ducky
- 1 Adaptator with USB multiport (In order to plug your rubber ducky and your USB key)

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
- Download Splendente-USB repos
- If you download on zip format or other directly from github web site rename all `Splendente-USB-master`directory name into `Splendente-USB` 
- `pip3 install -r Splendente-USB\requirement.txt`
- Rename your USB key to 'USB_DATA'
- Copy `Splendente-USB` repository into USB key labeled 'USB_DATA'
- Open powershell or cmd and move into your USB key `cd YourLetterKey:\`
- Move into Splendente-USB directory in your USB key `cd Splendente-USB/splendente`
- Packaged  `splendente_usb.py` with pyinstaller -> `pyinstaller --specpath setup/ --workpath setup/build --distpath setup/dist --clean -F --noconsole .\splendente_usb.py`
- (Optional) In `USB_DATA/Splendente-USB/agent/` directory place your file that you want copy from USB to target
- Take the `Splendente-USB/rubber_ducky_script/duckycode.txt` file and encode it (https://ducktoolkit.com/encode#), then place the generated `inject.bin` file in your Rubber Ducky
- Using a multi-USB adapter, insert your Rubber Ducky and USB key labeled "USB_DATA"
- Plug in your USB adapter!

## Directories of USB Tree 
- USB key (USB_DATA) :
  ```
  - USB_DATA -> Name or label of USB key
    - USB_DATA/Splendente-USB/data_*                                    -> Directory of data copied from target, will be appear when after launch program
    - USB_DATA/Splendente-USB/agent/                                    -> Copy file(s) from USB key to target + persistence (optional)
    - USB_DATA/Splendente-USB/conf/splendente.ini                       -> Manage files and directories that you want copy
    - USB_DATA/Splendente-USB/log/splendente.log                        -> Traceability of actions
    - USB_DATA/Splendente-USB/splendente/splendente_usb.py              -> main python program
    - USB_DATA/Splendente-USB/splendente/setup/dist/splendente_usb.exe  -> main exe program will be appear after launch of 'pyinstaller' command and that will be executed by the rubber_ducky device   
   ```
    
- Rubber Ducky :
  ```
    - yourRubberDucky/inject.bin
  ```
    
## Manage 
- Manage the files and dirs that you want to copy:
  ```
  - Edit Splendente-USB/conf/splendente.ini
  ```
  
## Todo
- Version 1.1.0
  - Several path additions

## Licence
- MIT

## Disclaimer
- Splendente-USB is for education/research purposes only. The author takes NO responsibility ay for how you choose to use any of the tools provided

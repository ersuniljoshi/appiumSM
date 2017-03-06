# Appium

## Task Completed for Project

1. Android automation using Appium

2. Created separate codex file for android

3. Automated SM android app

4. Written script to add 5 type of question in survey and preview survey
   including sign-in and sign-out
   
5. Script contains 4 testcases.
  
## Userdefine Command Line Parameters/Options for project :

* --device

    usage   : Run script on emulator/simulator or real android/ios 
              devices
              
    options : "Android Emulator", "Android device"
    
    default : "Android Device"
        
* --codexFile

    usage   : Automate android app or ios app
    
    options : "android", ios
    
    default : "android"
    
## Pytest built-in Command Line Parameters/Options for project :

* --html

    usage  : Generate html report for test result
    
    option : Path-for-report-file
    
## Commmand to run script :

   py.test -v -s testfile --device='ANDROID DEVICE' --hub_url='hub_url/wd/hub'
            --codexFile=android test-path  --platformName='name' --platformVersion='version' --html=path-for-report-file --junitxml=junit.xml
           
   

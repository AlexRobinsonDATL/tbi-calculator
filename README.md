# TBI-calculator

Small application to calculate the TBI (from metabase) with certain customers excluded.



## Contents
* [Config](#config)
* [Dev](#Dev)
    * [Setup Enviroment](#setup-enviroment)
    * [Build Exe](#build-exe)
---
## Config
### Smartsheet
#### api_key
Used to connect to smartsheet. Found on smartsheet under personal settings

![Personal Settings](/images/smartsheet-personal-settings.png)
![Api Keys](/images/smartsheet-personal-settings2.png)

#### sheet_name
The name of the TBI exclusion sheet.

#### column_name
The name of the column containing the account codes. 

---
### Metabase
#### url
The url of metabase. Make sure not to include a trailing /

#### query_number
The card number containing the To be invoiced report. 

E.g metabase.co.uk/question/{number}

---
## Dev
### Setup Environment
* Install Python3.8 from [https://www.python.org/downloads/](https://www.python.org/downloads/)
 * Install the poetry package manager from [https://python-poetry.org](https://python-poetry.org)
* Run the setup script "setup-enviroment.bat" in /scripts
### Build exe
Run the build.bat file in /scripts
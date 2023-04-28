# Twitch login script
## Description
this project consists in a script to login on twitch with more than one account at the same time (with 2FA code) 
## Requirements
For this program you need to have python and pip installed, if you dont have you can install with this commands:
<br>
<br>
Python
```
sudo apt-get install python3
```
Pip
```
sudo apt install python3-pip
```
## Dependencies
### Selenium
in case you have pip follow this command: 
```
pip install selenium
```
in case you have pip3 follow this command: 
```
pip3 install selenium
```

### Beautifulsoup
in case you have pip follow this command:
```
pip install beautifulsoup4
```
in case you have pip3 follow this command:
```
pip3 install beautifulsoup4
```
## Usage
After installing ```python, pip and all the dependencies``` you can continue.<br>
You need to configure the accounts.txt file with this format(one account per line):<br><br>
Accounts.txt
```python
Username:Password:SecretKey
```


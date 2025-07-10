# telepush
Python module for sending to telegram bot

## What was this utility written for?
This code allows you to send data via a Telegram bot, for example, when performing an action or sending other necessary information. The telepush.py file is required for correct operation; it should be placed in the project folder along with the .env file it creates.

## What is needed to launch?
### 1) Clone repo 
```
git clone https://github.com/rbknkt/telepush.git
```
### 2) Install requirements.txt
```
pip install -r requirements.txt
```
### 3) Run telepush.py and follow the instructions

## Usage
### 1) Connect the file
```
from telepush import telepush_send
```
### 2) Use the function
```
telepush_send()
```
P.S. You can pass a number or text to the function

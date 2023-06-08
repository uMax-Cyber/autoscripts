#Telegram Autosender

Install Python: Ensure that you have Python installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

1.Install the required packages: Open a command prompt or terminal and run the following commands to install the necessary packages:
pip install -r requirements.txt

2.Obtain API credentials: You need to obtain API credentials from the Telegram website. Follow these steps:

Visit https://my.telegram.org/auth.
Log in to your Telegram account.
Under "API development tools," create a new application by providing a name, description, and website (can be any valid URL).

3.Once created, you will see the "App api_id" and "App api_hash" values. Replace '2112213' with your api_id and '222223' with your api_hash in the code.
Set your phone number: Replace '+654654654654' with your actual phone number in international format (including the country code) inside the code. (telegram-autosend.py)

4.Add contacts and sticker paths: Modify the contacts dictionary to include the desired user IDs and corresponding sticker paths. User IDs can be obtained from the Telegram API or other methods.

5.Save the Python file: Save the Python file with the modifications made.

6.Run the code: Open a command prompt or terminal, navigate to the directory where the Python file is saved, and run the following command:
python3 telegram_autosend.py

7.Keep the script running: The script will run indefinitely, checking the schedule and sending stickers every Friday at 6:00 AM. You can close the command prompt or terminal if you want to stop the script.

8. If you wanna run this script as service in startup, copy the file autosend.service to folder /etc/systemd/system and edit with nano!

Bonus: Amazing Unifi f**king script for joking with WiFi clients

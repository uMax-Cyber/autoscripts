📢 #Telegram Autosender

🔧 Install Python: Ensure that you have Python installed on your system. You can download the latest version of Python from the official website: Python Downloads

1️⃣ Install the required packages: Open a command prompt or terminal and run the following commands to install the necessary packages:

Copy code
pip install -r requirements.txt

2️⃣ Obtain API credentials: You need to obtain API credentials from the Telegram website. Follow these steps:

Visit Telegram API
Log in to your Telegram account.
Under "API development tools," create a new application by providing a name, description, and website (can be any valid URL).

3️⃣ Once created, you will see the "App api_id" and "App api_hash" values. Replace '2112213' with your api_id and '222223' with your api_hash in the code.

Set your phone number: Replace '+654654654654' with your actual phone number in international format (including the country code) inside the code. (telegram-autosend.py)

4️⃣ Add contacts and sticker paths: Modify the contacts dictionary to include the desired user IDs and corresponding sticker paths. User IDs can be obtained from the Telegram API or other methods.

5️⃣ Save the Python file: Save the Python file with the modifications made.

6️⃣ Run the code: Open a command prompt or terminal, navigate to the directory where the Python file is saved, and run the following command:

Copy code
python3 telegram_autosend.py
7️⃣ Keep the script running: The script will run indefinitely, checking the schedule and sending stickers every Friday at 6:00 AM. You can close the command prompt or terminal if you want to stop the script.

8️⃣ If you want to run this script as a service on startup, copy the file autosend.service to the folder /etc/systemd/system and edit it with nano!

💥 Bonus: Amazing Unifi f**king script for joking with WiFi clients

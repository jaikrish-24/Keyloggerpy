<h1> PyKeylogger </h1>

<h3> A Python keylogger utilizing the pynput library, designed to send captured keystroke data to a specified server. </h3>

<h2> Disclaimer : This code is intended for educational purposes only and does not endorse or encourage any illegal activities. It serves as a proof of concept and can be enhanced in various ways.</h2>

<h2>Description</h2> 

A keylogger is a software or hardware tool that records the keystrokes made on a computer or mobile device. It captures and logs the sequence of keys pressed, potentially including sensitive information such as passwords, usernames, and other text input. Keyloggers have both legitimate uses, such as in security testing or parental control, and nefarious uses, such as unauthorized data capture for malicious purposes. The project involves Two machines: the server, where a Flask app resides to receive and store keyboard data, and the client, which runs a keylogger, transmitting captured data to the server for logging and analysis.


**Features:**

- **Security Testing:** - Enhancing defenses against concealed keyloggers.

- **School/Institutions:** - Recording keystrokes and logging restricted words in a file.

- **Business Administration:** - Monitoring employee activities with their explicit consent.

- **Parental Control:**  - Tracking and monitoring your children's activities.

- **Self-analysis and Assessment:** - Conducting personal evaluation and assessment.

- **Personal Control and File Backup:** - Verifying unauthorized computer use in your absence.


<h3>Usage:</h3>

1. Run this code to clone the repo:
```bash
git clone https://github.com/Keyloggerpy/PyKeylogger.git
```

2. Run this command to install all the packages required in your virtual environment:
```bash
pip install -r requirements.txt
```

3. Run the command. This will do the basic setup of the server on Attacker machine:
```bash
python server.py
```

4. Run as a Python script on target machine:
```bash
python Target_script.py
```

5. Run as a exe file on target machine (hidden):
```bash
pip install pyinstaller
```
Move the pyinstaller to the file where Wind_script.py is located.
```bash
pyinstaller.exe --onefile --noconsole Target_script.py
```
6. After running check the directory of the server for the received keystrokes. 


<h3>Contributions:</h3>

We welcome contributions to the PyKeylogger project! If you have suggestions for enhancements, bug fixes, or new features, please don't hesitate to share them by submitting a pull request or opening an issue. Your input is valuable to the project's development.



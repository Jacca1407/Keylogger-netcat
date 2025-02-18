# Keylogger-netcat
Keylogger that sends the logs to a linux machine using socket and netcat.
The program sends logs in the format: [date hour] button clicked: x
The exe program will round without making any window pop up while the .py will.
To get the logs the linux machine (listening) shall run the command 'nc -lvp PORT' (to write the logs in a file you can add ' | tee log.txt' at the end of the command.
You can turn the .py in .exe with pyinstaller/autopytoexe (command: 'pyinstaller --noconfirm --onefile --windowed --icon "icon path"  ".py path" '

Disclamer: I do not hold any responsability for any wrong use of the app

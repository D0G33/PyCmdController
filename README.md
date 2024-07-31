<p align="center">Python Command Controller</p>

###

<p align="center">______________________________________________________________________________________________________________________________________________________</p>

###

<p align="left">A simple and powerful script for creating and controlling CMD prompts. <br><br><br>What it can do:<br><br>_ Elevate CMD Prompts<br>_ Type over read only inputs. (No more pesky password prompts)<br>_ Remember Console History (cd actually works :0)<br>_ Anything else you can do by typing into a command prompt yourself.<br><br>What it cant do:<br><br>_ Do any of this descretely<br>_ Type to hidden or minimized windows<br>_ Natively Get Outputs (no stdout access, praise temp files)</p>

###

<p align="center">______________________________________________________________________________________________________________________________________________________</p>

###

<p align="left">Unfortunatly, (or maybe not), this project uses REAL CMD prompts to allow python to use these commands.<br><br>This means that a console window must be visible for python to execute these commands.<br><br>Also, there is many PyAutoGUI inputs for allowing python to ensure window focus and to type. (Ill probably fix this to just use win32gui later.)</p>

###

<p align="center">______________________________________________________________________________________________________________________________________________________</p>

###

<p align="center">Script Requires pywin32gui, pywin32con, and pyautogui</p>
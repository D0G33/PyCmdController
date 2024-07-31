import win32con
import win32gui
import os
import pyautogui
from time import sleep
import atexit


#list all windows list
pythonPath = os.getcwd()

def enum_window_titles():
    def callback(handle, data):
        titles.append(win32gui.GetWindowText(handle))

    titles = []
    win32gui.EnumWindows(callback, None)
    return titles


class cmdObject:
    def collectHandle(self,name):
        laziness = 0
        while True:
            try:
                window_handle = win32gui.FindWindow(None, name)
                if window_handle != 0:
                    if laziness != 0: sleep(1 / (1 + (laziness / 100)))
                    return window_handle
                else:
                    laziness += 1
            except Exception as err:
                print(err)
                laziness += 1
                pass
    def __init__(self, name):
        os.system('start "' + name + '" cmd')
        self.name = name
        self.window_handle = self.collectHandle(name)
        atexit.register(self.close)

    def getRect(self):
        #Sourced Here: https://stackoverflow.com/questions/7142342/get-window-position-size-with-python
        rect = win32gui.GetWindowRect(self.window_handle)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        return x, y, w, h

    def activate(self):
        # Activate Window and Allow Keyboard Input
        win32gui.ShowWindow(self.window_handle, win32con.SW_SHOW)
        win32gui.BringWindowToTop(self.window_handle)

        # Click the window for safety
        _x, _y, _w, _h = self.getRect()
        pyautogui.click(_x + 50, _y + 50)

    def hide(self):

        win32gui.ShowWindow(self.window_handle, win32con.SW_MINIMIZE)

    def show(self):
        win32gui.ShowWindow(self.window_handle, win32con.SW_SHOW)

    def invisible(self):
        #Not Recommended for Debugging Purposes
        win32gui.ShowWindow(self.window_handle, win32con.SW_HIDE)

    def _cmd(self,cmd):
        #Intended for internal use only
        pyautogui.write(cmd + "\n", interval=0)

    def cmd(self,*cmd):
        self.activate()
        if cmd[0] != None:
            for i in cmd:
                self._cmd(i)
        else:
            _list = list(cmd)
            _list.pop(0)
            for i in _list:
                self._cmd(i)
        self.invisible()

    def close(self):
        win32gui.PostMessage(self.window_handle, win32con.WM_CLOSE, 0, 0)
    def elevate(self, user, password, domain=os.environ['COMPUTERNAME']):
        self.cmd("runas /user:"+user+" cmd", password)
        self.close()
        self.window_handle = self.collectHandle("cmd "+"(running as "+domain+"\\"+user+")")
        self.cmd("title "+self.name)
        self.invisible()

    def out(self,cmd,*args):
        #run command with output directed
        self.activate()
        os.system("mkdir C:\\Temp")
        self._cmd(cmd+" > C:\\Temp\\command_out.txt")
        for i in args:
            self._cmd(i + " >> C:\\Temp\\command_out.txt")
        self.invisible()

        output = open('C:\\Temp\\command_out.txt','r')
        raw = output.readlines()
        for i in range(len(raw)):
            raw[i] = raw[i].replace("\n",'')
        output.close()

        os.system("del C:\\Temp\\command_out.txt")
        return raw

def main():
    user,password = 'pythonAdmin', 'PythonPassword'
    testObj = cmdObject("the correct window name")
    testObj.elevate(user,password)
    testObj.invisible()
    testObj.activate()
    testObj.cmd("cd C:\\Temp")
    print(testObj.out("echo Hello",
                      "echo World"))
    testObj.show()


if __name__ == '__main__':
    main()

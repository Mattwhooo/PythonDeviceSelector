from tkinter import *
from DeviceInfo import DeviceInfo

class DeviceSelector:
    def __init__(self,parallel=False):
        #Create Window
        self.root = Tk()
        win = self.root

        #Set Window Properties
        win.iconbitmap(default='runner.ico')
        win.wm_title("Test Runner")
        win.minsize(width=500, height=500)

        #Create Listbox
        scrollbar = Scrollbar(win)
        scrollbar.pack(side=RIGHT, fill=Y)
        if parallel:
            label = Label(win, text="Please Select one or more devices to run")
            label.pack()
            self.listbox = Listbox(win, selectmode=EXTENDED)
        else:
            label = Label(win, text="Please Select one device to run")
            label.pack()
            self.listbox = Listbox(win, selectmode=SINGLE)
        self.listbox.pack(fill=BOTH, expand=1)

        #Attach Scrollbar to Listbox
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        #Generate Listbox Data
        info = DeviceInfo()
        for deviceId in info.gridDevices():
            device = info.getDevice(deviceId)
            self.listbox.insert(END, device['udid'] + ' -- ' + device['name'])
        self.frame = Frame(win)
        self.frame.pack(fill=X)

        #Create Buttons
        Button(self.frame, text="Cancel", fg="red", command=self.frame.quit, width=50).pack(side=RIGHT, fill=Y)
        Button(self.frame, text="Run Test", command=self.saveDevices, width=50).pack(side=LEFT, fill=Y)

    def getDevice(self):
        self.root.mainloop()
        self.root.destroy()
        return self.devices

    def saveDevices(self):
        devices = self.listbox.curselection()
        output=[]
        for device in devices:
            output.append(self.listbox.get(device))
        self.frame.quit()
        self.devices = output

device = DeviceSelector().getDevice()
print(device)
# TODO : Add a check if bridge is connected
# TODO : Add light selection and swap lights on click
# TODO : Add kill all lights
# TODO : Add turn all lights
# TODO : Add settings file for Bridge IP and settings menu bar




from PySide2.QtGui import *
from PySide2.QtWidgets import *
from phue import Bridge

app = QApplication([])
app.setQuitOnLastWindowClosed(False)
app.desktopSettingsAware()

bridge = Bridge("192.168.1.148")


# Create the icon
# icon = QIcon('C:\\Users\\ndrni\\OneDrive\\Desktop\\Lumierew.png')

def switch_all_lights():

    """
    Switches on/off all lights connected to Hue
    """
    print ("Switch Light Button Activated")

    lights = bridge.lights
    for light in lights:
        if light.name.endswith("lamp"):
            print (light.name)
            if light.on == True:
                print ("Found light on")
                light.on = False
            else:
                light.on = True
                light.brightness = 200
                print ("Found a dead light")


def dimmer():
    """:arg
    Dims all lights connected to Hue
    """
    lights = bridge.lights
    for light in lights:
        if light.name.endswith("lamp"):
            print (light.name)
            if light.on == True:
                print ("Dimming")
                light.brightness = 50



def connect_bridge():
    print ("Connecting to Bridge")
    bridge.connect()
    print ("Connected")






# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)
tray.setToolTip("Lumière")

# Create the menu
menu = QMenu()

action0 = QAction("Bridge Connection")
action0.setStatusTip("Testing")

action0.setCheckable(True)
action0.setChecked(True)

action0.triggered.connect(connect_bridge)
menu.addAction(action0)
menu.addSeparator()

action1 = QAction("All Lights Switch")
action1.triggered.connect(switch_all_lights)
menu.addAction(action1)

action2 = QAction("Dim All")
action2.triggered.connect(dimmer)
menu.addAction(action2)


quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec_()

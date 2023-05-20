
from __future__ import print_function
import ctypes, sys
import time
import wmi


def GetNicConfig():
    wmiService = wmi.WMI()
    NetCard = 0
    for network in wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        if network.IPAddress:
            print('{}. {}'.format(NetCard, network.IPAddress))
            NetCard += 1
    n = int(input('Select the NetCard:'))
    colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)[n]
    if len(wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)) < 1:
        print('No available network adapters found')
        return False
    else:
        global objNicConfig
        objNicConfig = colNicConfigs
        return True




def SetAutoDNS():
    returnValue = objNicConfig.SetDNSServerSearchOrder()
    if returnValue[0] == 0:
        print('Successfully set up automatic DNS acquisition')
    elif returnValue[0] == 1:
        print('Successfully set up automatic DNS acquisition')
    else:
        print('ERROR: DNS settings encountered an error')
        return False
    return True


def SetAutoIP():
    returnValue = objNicConfig.EnableDHCP()
    if returnValue[0] == 0:
        print('Successfully set automatic IP acquisition')
    elif returnValue[0] == 1:
        print('Successfully set automatic IP acquisition')
        time.sleep(5)
    else:
        print('ERROR: IP setting error')
        return False
    return True

def EnableDHCP():
    return SetAutoDNS() and SetAutoIP()


def main():
    if not GetNicConfig():
        return False
    else:
        print('Switching to dynamic IP')
        intReboot = 0
        if EnableDHCP():
            if intReboot > 0:
                print('need to restart your computer')
            else:
                print('Successfully switched to dynamic DHCP!')
        else:
            print('Please close the control panel and run with administrator privileges to try again')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    pass
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)



def ReDHCP():
    while( is_admin()):
        main()
import wmi
import activity as ac
import restore as res
import ctypes, sys


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
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

if __name__ == '__main__':
    print('Directly enter to set dynamic acquisition')
    ReDHCP = str(input('Do you want to restore DHCP(Y/N):'))
    if (ReDHCP == 'N' or ReDHCP == 'n' or ReDHCP == 'no'):
        while(is_admin()):
            print('Start modifying static address')
            ac.CIp()
    else:
        print('Start setting to automatic acquisition')
        res.ReDHCP()
import json
import wmi
import time

w = wmi.WMI()
def CIp():
    try:
        NetCard = 0
        for network in w.Win32_NetworkAdapterConfiguration(IPEnabled=True):
            if network.IPAddress:
                print('{}. {}'.format(NetCard, network.IPAddress))
                NetCard += 1
        n = int(input('Select the NetCard:'))

        #The selected NetCard
        net = w.Win32_NetworkAdapterConfiguration(IPEnabled=True)[n]

        add_24,add_32 = input('10.10.*.*:').split('.')
        add = ['10.10.{}.{}'.format(add_24,add_32)]
        mask = ['255.255.255.0']
        gateway = ['10.10.22.1']
        gateway_metric = [1]
        dns = ['10.10.1.3','223.5.5.5']
        ip_mask = net.EnableStatic(IPAddress=add, SubnetMask=mask)
        if ip_mask[0] != 0:
            print(' × {} IP/mask modification failed :('.format(add))
        else:
            print(' √ {} The IP/mask is modified successfully :)'.format(add))
        gat = net.SetGateways(DefaultIPGateway=gateway, GatewayCostMetric=gateway_metric)
        if gat[0] != 0:
            print(' × {} Gateway modification failed :('.format(gateway))
        else:
            print(' √ {} Gateway modified successfully :)'.format(gateway))
        dns_ = net.SetDNSServerSearchOrder(DNSServerSearchOrder=dns)
        if dns_[0] != 0:
            print(' × {} DNS modification failed :('.format(dns))
        else:
            print(' √ {} DNS modified successfully :)'.format(dns))
        print('\nfinish')
        print('If the modification fails, run in administrator mode')
        print('\n----------------------------------------------------------------------------------------------------------\n')

        do = input('End the run?(Y/N)')
        if(do == 'N' or do == 'n'):
            pass
        else:
            print('Bye')
            time.sleep(2)
            exit()
    except Exception as err:
        print(err)

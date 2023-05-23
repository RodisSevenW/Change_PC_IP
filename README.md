# SET_PC_IP
Modifying IP addresses in a multi intranet environment
Using the campus intranet in the laboratory and the intranet in the dormitory requires changing the address of the network card, which is very cumbersome, and can be achieved by using this script: quickly switch the writing of static IP addresses and replace the DHCP mode.
Install before use
<code>pip install wmi
  

The IP address modified in this code applies to the internal network of MKU, and if necessary, you can modify it according to your own internal network.

Note that administrator privileges are required because the NIC needs to be modified.


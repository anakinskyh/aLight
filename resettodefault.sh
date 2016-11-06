i=$(ifconfig | awk '{print $1}' | grep wl)
echo $i

sudo iwconfig $i mode managed
iwconfig

dhclient $i
ifconfig

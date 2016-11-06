i=$(ifconfig | awk '{print $1}' | grep wl)
echo $i

echo "set id [1-254]<default:1>:"
read _id

echo "set essid<default:aLight>:"
read _essid

essid=aLight
id=1

if [ ${#_id} -gt 0 ]
then
	id=$_id
fi

if [ ${#_essid} -gt 0 ]
then
	essid=$_essid
fi

if [ $# -gt 0 ]
then
	id=$1
fi

if [ $# -gt 1 ]
then
	essid=$2
fi


sudo iwconfig $i mode ad-hoc
sudo iwconfig $i essid $essid
iwconfig

sudo ifconfig $i 192.168.1.$id netmask 255.255.255.0
ifconfig

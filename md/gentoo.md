``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/ssh:192.168.0.18" rundoc-results="output"}

ip addr


```

iwconfig wlp3s0 essid HomeNearPark

iwconfig eth0 essid GentooNode

To set the network name to GentooNode:

root \#iwconfig eth0 essid GentooNode

To set a hex WEP key:

root \#iwconfig eth0 key 1234123412341234abcd

To set an ASCII WEP key, prefix the key with s::

root \#iwconfig eth0 key s:some-password

Note If the wireless network is set up with WPA or WPA2, then
wpa~supplicant~ needs to be used. For more information on configuring
wireless networking in Gentoo Linux, please read the Wireless networking
chapter in the Gentoo Handbook.

Confirm the wireless settings again by using iwconfig. Once wireless is
working,continue configuring the IP level networking options as
described in the next section (Understanding network terminology) or use
the net-setup tool as described previously. Understanding network
terminology Note If the IP address, broadcast address, netmask and
nameservers are known, then skip this subsection and continue with Using
ifconfig and route.

If all of the above fails, the network will need to be configured
manually. This is not difficult at all. However, some knowledge of
network terminology and basic concepts might be necessary. After reading
this section, users will know what a gateway is, what a netmask serves
for, how a broadcast address is formed and why systems need nameservers.

In a network, hosts are identified by their IP address (Internet
Protocol address). Such an address is perceived as a combination of four
numbers between 0 and 255. Well, at least when using IPv4 (IP version
4). In reality, such an IPv4 address consists of 32 bits (ones and
zeros). Let's view an example: CODE Example of an IPv4 address

IP Address (numbers): 192.168.0.2 IP Address (bits): 11000000 10101000
00000000 00000010 -------- -------- -------- -------- 192 168 0 2

Note The successor of IPv4, IPv6, uses 128 bits (ones and zeros). In
this section, the focus is on IPv4 addresses.

Such an IP address is unique to a host as far as all accessible networks
are concerned (i.e. every host that one wants to be able to reach must
have a unique IP address). In order to distinguish between hosts inside
and outside a network, the IP address is divided in two parts: the
network part and the host part.

The separation is written down with the netmask, a collection of ones
followed by a collection of zeros. The part of the IP that can be mapped
on the ones is the network-part, the other one is the host-part. As
usual, the netmask can be written down as an IP address. CODE Example of
network/host separation

IP address: 192 168 0 2 11000000 10101000 00000000 00000010 Netmask:
11111111 11111111 11111111 00000000 255 255 255 0
~~--------------------------~~--------+ Network Host

In other words, 192.168.0.14 is part of the example network, but
192.168.1.2 is not.

The broadcast address is an IP address with the same network-part as the
network, but with only ones as host-part. Every host on the network
listens to this IP address. It is truly meant for broadcasting packets.
CODE Broadcast address

IP address: 192 168 0 2 11000000 10101000 00000000 00000010 Broadcast:
11000000 10101000 00000000 11111111 192 168 0 255
~~--------------------------~~--------+ Network Host

To be able to surf on the Internet, each computer in the network must
know which host shares the Internet connection. This host is called the
gateway. Since it is a regular host, it has a regular IP address (for
instance 192.168.0.1).

Previously we stated that every host has its own IP address. To be able
to reach this host by a name (instead of an IP address) we need a
service that translates a name (such as dev.gentoo.org) to an IP address
(such as 64.5.62.82). Such a service is called a name service. To use
such a service, the necessary name servers need to be defined in
/etc/resolv.conf.

In some cases, the gateway also serves as a nameserver. Otherwise the
nameservers provided by the ISP need to be entered in this file.

To summarize, the following information is needed before continuing:
Network item Example The system IP address 192.168.0.2 Netmask
255.255.255.0 Broadcast 192.168.0.255 Gateway 192.168.0.1 Nameserver(s)
195.130.130.5, 195.130.130.133 Using ifconfig and route

Setting up the network consists of three steps:

Assign an IP address using ifconfig Set up routing to the gateway using
route Finish up by placing the nameserver IPs in /etc/resolv.conf

To assign an IP address, the IP address, broadcast address and netmask
are needed. Then execute the following command, substituting
\${IP~ADDR~} with the right IP address, \${BROADCAST} with the right
broadcast address and \${NETMASK} with the right netmask: root
\#ifconfig eth0 \${IP~ADDR~} broadcast \${BROADCAST} netmask \${NETMASK}
up

Set up routing using route. Substitute \${GATEWAY} with the right
gateway IP address: root \#route add default gw \${GATEWAY}

Now open /etc/resolv.conf: root \#nano -w /etc/resolv.conf

Fill in the nameserver(s) using the following as a template. Make sure
to substitute \${NAMESERVER1} and \${NAMESERVER2} with the appropriate
nameserver addresses: CODE Default template to use for /etc/resolv.conf

nameserver \${NAMESERVER1} nameserver \${NAMESERVER2}

uipcalc
=======

Universal (IPv4/IPv6) CIDR calculator

Source available at: `bitbucket.org/asenci/uipcalc/ <http://bitbucket.org/asenci/uipcalc/>`_

Please report any issues at: `bitbucket.org/asenci/uipcalc/issues/ <http://bitbucket.org/asenci/uipcalc/issues/>`_


Installing:
-----------

::

    $ pip install uipcalc


Usage:
------

::

    uipcalc [-h] address [netmask]

    Universal (IPv4/IPv6) IP address and netmask calculator

    positional arguments:
      address     IP address with optional netmask in CIDR notation
      netmask     Netmask in dotted-decimal notation

    optional arguments:
      -h, --help  show this help message and exit


Examples:
---------

::

    $ uipcalc 192.0.2.4/12
    Network:    192.0.0.0
    Netmask:    255.240.0.0
    Broadcast:  192.15.255.255

    Number of addresses:  1048576

    Net:   11000000.00000000.00000000.00000000
    Mask:  11111111.11110000.00000000.00000000
    Last:  11000000.00001111.11111111.11111111

    $ uipcalc 192.0.2.4/26
    Network:    192.0.2.0
    Netmask:    255.255.255.192
    Broadcast:  192.0.2.63

    Number of addresses:  64

    Net:   11000000.00000000.00000010.00000000
    Mask:  11111111.11111111.11111111.11000000
    Last:  11000000.00000000.00000010.00111111

    $ uipcalc 2001:DB8::/48
    Network:    2001:0db8:0000:0000:0000:0000:0000:0000
    Netmask:    ffff:ffff:ffff:0000:0000:0000:0000:0000
    Broadcast:  2001:0db8:0000:ffff:ffff:ffff:ffff:ffff

    Number of addresses:  1208925819614629174706176

    Net:   0010000000000001.0000110110111000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000
    Mask:  1111111111111111.1111111111111111.1111111111111111.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000
    Last:  0010000000000001.0000110110111000.0000000000000000.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111

    $ uipcalc 2001:DB8::/60
    Network:    2001:0db8:0000:0000:0000:0000:0000:0000
    Netmask:    ffff:ffff:ffff:fff0:0000:0000:0000:0000
    Broadcast:  2001:0db8:0000:000f:ffff:ffff:ffff:ffff

    Number of addresses:  295147905179352825856

    Net:   0010000000000001.0000110110111000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000
    Mask:  1111111111111111.1111111111111111.1111111111111111.1111111111110000.0000000000000000.0000000000000000.0000000000000000.0000000000000000
    Last:  0010000000000001.0000110110111000.0000000000000000.0000000000001111.1111111111111111.1111111111111111.1111111111111111.1111111111111111


Requirements:
-------------

- Python >= 2.6 (Python 3 not yet supported)
- argparse (for Python 2.6)
- ipaddr >= 2.1


License:
--------

Licensed under ISC license.

See `LICENSE <http://bitbucket.org/asenci/uipcalc/raw/master/LICENSE>`_ file for details.
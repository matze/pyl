# Reading system information

The file `/etc/os-release` contains information of the installed distribution.
So first let's read that into a variable

    data = open('/etc/os-release').read()

and split the ini-like format into keys and values

    info = dict(x.split('=') for x in data.split('\n') if x)

You are running version `info['VERSION']` of `info['NAME']`.

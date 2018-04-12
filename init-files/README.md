# LagoInitFile examples

This directory contains of LagoInitFiles examples, each example can be used
with the following steps:

* Create the environment

```bash
  $ lago init <filename>
```

* Start the vms

```bash
  $ lago start
```

At this point the environment is up.
The following commands can be used to interact
with the environment. The commands below was called on an environment that was created using [init_1_vm_1_net.yaml](init_1_vm_1_net.yaml), but they can be used on any environment.

* Check the status of the environment

```bash
  $ lago status

  [Prefix]:
    lago/default
    [Networks]:
        [net-01]:
            gateway: 192.168.202.1
            management: True
            status: up
    UUID: a11f1e023e4711e8836054ee75693071
    [VMs]:
        [vm-el7]:
            [NICs]:
                [eth0]:****
                    ip: 192.168.202.2
                    network: net-01
            distro: el7
            root password: 123456
            status: up

```

* Copy a file to a VM

```bash
  $ echo 'hi' > hi.txt
  $ lago lago copy-to-vm vm-el7 hi.txt /root
  @ Copy hi.txt to vm-el7:/root:
  @ Copy hi.txt to vm-el7:/root: Success (in 0:00:00)
```

* Shell to a VM

```bash
  $ lago shell vm-el7
  $ [root@vm-el7 ~] cd /root && cat hi.txt
    hi
  $ exit
```

* Stop the environment

```bash
  $ lago stop
```

* Permanently remove the environment

```bash
  $ lago destroy
  Do you really want to destroy  lago-examples/init-files/.lago/default? [Yn]
  $ Y
```

The flow above can be called directly from Python using Lago's SDK:

```python

from lago import sdk

env = sdk.init(config='<filename>',
               workdir='/tmp/lago-workdir')
```

* Checkout the full [SDK example ](https://github.com/lago-project/lago/blob/master/docs/examples/lago_sdk_one_vm_one_net.ipynb)

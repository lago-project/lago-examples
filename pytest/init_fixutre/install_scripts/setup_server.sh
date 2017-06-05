#!/bin/bash -ex
mkdir -p /var/log/myapp
echo "this will be collected!" >> /var/log/myapp/dump.log
echo "this will be collected!" >> /var/log/myapp/myapp.log

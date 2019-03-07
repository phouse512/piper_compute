#!/bin/bash

# install Ansible repository.
sudo apt -y update && apt-get -y upgrade
sudo apt -y install software-properties-common
sudo apt-add-repository ppa:ansible/ansible

sudo apt -y update
sudo apt -y install ansible


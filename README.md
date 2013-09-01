% pyvmx - a small python script to batch-edit VMWare VMX files
% Nick Ivanov
% 1 Sep. 2013

pyvmx
=====

# Small python script to batch-edit VMWare VMX files

When cloning VMWare images you have no control over several properties
of the cloned VMs, such as the VM name or the configuration of the 
virtual network adapters. This script was born to reduce the amount of
manual editing required when juggling a handful of VMXs under VMWare
Workstation. It allows you to automate editing of VMX files after clon-
ing. 

## To do

Provide similar functionality for editing /etc/vmware/networking -- 
VMWare virtual network configuration.

It might also be helpful to maintain the list of VMX configuration key-
words, as they are scarcely documented.
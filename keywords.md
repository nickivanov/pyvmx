% The list of VMWare .VMX file configuration keywords
% Nick Ivanov
% 1 Sep. 2013

<!-- Uses Markdown Extra / reStructuredText / pandoc approach
     to the definition lists -->

.encoding 
:    Encoding used in the VMX file content, e.g. "windows-1252"

annotation
:    VM image description that appears in the Workstation VM properties window. 

checkpoint.vmState
:    ?

checkpoint.vmState.readOnly
:    Boolean value

cleanShutdown
:    Boolean value.

config.version
:    Integer value (?). The VMX file version, probably should match the Workstation version.

extendedConfigFile
:    The relative path name of the file containing additional configuration parameters. 

displayName
:    The name that appears in the Workstation VM inventory window. After cloning a VM this is 
     set to "Clone of ..."

ethernet0.addressType
:    Determines how the particular virtual Ethernet adapter MAC address is
     derived. Possible values: "generated", ...

ethernet0.allow64bitVmxnet
:    Boolean value.

ethernet0.connectionType
:    Virtual network mode. Possible values: "hostonly", "bridge", "nat", ...

ethernet0.generatedAddress
:    The virtual network adapter MAC value in the format similar to "00:0C:29:1F:AC:85". I
     guess it will be present if the **ethernet0.addressType** value is "generated".

ethernet0.startConnected
:    Boolean value. Indicates whether this virtual Ethernet adapter should be enable at the
     guest startup. 

ethernet0.pvnID
:    The PVN (private virtual network) ID for this adapter, in the form "52 23 c8 b8 da ac 39 e7-bf 2e 7e 7b e2 89 af 51".

ethernet0.generatedAddressOffset
:    Integer value ?

ethernet0.pciSlotNumber
:    Integer value. The first virtual Ethernet adapter PCI slot number.

ethernet0.present
:    Boolean value to indicate if the first virtual Ethernet adapter is
     present.

ethernet0.virtualDev 
:    Virtual Ethernet adapter compatibility. Possible values: "e1000"

ethernet0.wakeOnPcktRcv
:    Boolean value. 

floppy0.present
:    Boolean value.

guestOS
:    Possible values: "suse-64", ...

gui.exitOnCLIHLT
:    Boolean value.

ide0:0.autodetect
:    Boolean value. 

ide0:0.deviceType
:    Possible values: "cdrom-image", ...

ide0:0.fileName
:    Absolute path name to the image file, e.g. .iso of a CD ROM, for the first
     IDE device

ide0:0.present
:    Boolean value. Indicates whether the first IDE device is present. 

ide0:0.startConnected
:    Boolean value. 

memsize
:    Integer value. The VM memory size, in kilobytes. (or is it kibibytes?)

nvram
:    Path name (relative or absolute) of the guest NVRAM (non-volatile RAM) image. 

policy.vm.mvmtid
:    ?

powerType.powerOff
:    Possible values: "hard", "soft"

powerType.powerOn
:    Possible values: "hard", "soft"

powerType.reset
:    Possible values: "hard", "soft"

powerType.suspend
:    Possible values: "hard", "soft"

priority.grabbed
:    Possible values: "normal", ...

priority.ungrabbed
:    Possible values: "normal", ...

replay.filename
:    Relative path to (what?)

replay.supported
:    Boolean value.

scsi0.pciSlotNumber
:    Integer value. The first virtual SCSI adapter PCI slot number.

scsi0.present
:    Boolean value to indicate if the first SCSI bus is present.

scsi0.sharedBus
:    Possible values: "none", ...

scsi0.virtualDev
:    Virtual SCSI adapter compatibility. Possible values: "lsilogic", ...

scsi0:0.deviceType
:    Possible values: "disk", ...

scsi0:0.fileName
:    File name (relative or absolute) of the virtual SCSI device image, the .vmdk file

scsi0:0.present
:    Boolean value to indicate if the first SCSI device is present.

scsi0:0.redo
:    ?

sharedFolder.maxNum
:    Integer value. What does it mean?

sharedFolder0.present
:    Boolean value. What does it mean?

sharedFolder0.enabled
:    Boolean value. Indicates whether this shared folder is enabled.

sharedFolder0.readAccess
:    Boolean value. Allows read access to the shared folder.

sharedFolder0.writeAccess
:    Boolean value. Allows write access to the shared folder.

sharedFolder0.hostPath
:    Full path to the shared folder on the host.

sharedFolder0.guestName
:    The name of the directory where the shared folder shold be mounted on the guest.

sharedFolder0.expiration
:    Determines when the shared folder should be disabled. Possible values: "never", ...

tools.remindInstall
:    Boolean value. Indicates whether the user is prompted to install VMWare
     tools when launching the guest OS.

tools.syncTime
:    Boolean ("TRUE" or "FALSE", case-insensitive). Probably reflects the VMWare tools setting
     to synchronise the guest time with the host.

unity.wasCapable
:    Boolean value

usb.pciSlotNumber
:    Integer value. The first virtual USB adapter PCI slot number.

usb.present
:    Boolean value.

uuid.action
:    Possible values: "create", ...

uuid.bios
:    UUID value in the form "56 4d 6c 24 c9 69 dd c0-cf e7 48 b9 df 1f ac 85".

uuid.location
:    UUID value in the form "56 4d 6c 24 c9 69 dd c0-cf e7 48 b9 df 1f ac 85".

virtualHW.productCompatibility
:    Possible values: "hosted", ...

virtualHW.version
:    Integer value. Reflects compatibility with previous versions of Workstation. 

vmotion.checkpointFBSize
:    Integer value?

vc.uuid
:    ?


RPi-SenseStation OS(Linux) Setup
================================

## Operating System
 - **Ubuntu Server 22.04 arm64**
   - Daily prebuilted image(20220901) for Raspberry Pi ARM64

## Reducing writes on microSD card (if you using it)
 ### F2FS
 > You can skip this section, and I strongly recommend to skip this if you are not familiar with Linux

 I just wanted to use flash-friendly file system to get most out of microSD card *(and to hope it won't mess up microSD card)*, so I followed some instructions from [WhiteHorsePlanet](http://whitehorseplanet.org/gate/topics/documentation/public/howto_ext4_to_f2fs_root_partition_raspi.html) and [addendum from Reddit](https://www.reddit.com/r/raspberry_pi/comments/f7cmm8/switched_to_f2fs_heres_some_things_to_know/) to convert root filesystem from `ext4` to `f2fs`.

 If you want to try it, you should:
   - **Complete first boot** right after flashing not modified prebuilt image
   - Make sure **you installed `f2fs-tools`** before shutdown
     ```sh
     # On RPi
     $ sudo apt install f2fs-tools
     $ sudo shutdown 0
     ```
   - Make sure **you formatted new filesystem labelled `writable`**
     ```sh
     # On another Linux host
     $ sudo mkfs.f2fs -l writable /dev/sdX
     ```
   - When you edit `fstab` file, **you should REMOVE `errors=remount-ro` MOUNT OPTION** or Ubuntu will not mount root filesystem as read/write!  
     `errors=remount-ro` mount option is not exist in F2FS, so Ubuntu will cause some errors and eventually will mount root filesystem as read-only.  
     If the mount option not exists, you can just continue.
  - It is recommended to add `noatime,nodiratime` mount option to root filesystem in `fstab`, even on ext4. This options will prevent kernel to record access time of each files/directories, so write operations will be reduced.

 ### [Log2Ram](https://github.com/azlux/log2ram)
 This will help reducing microSD card writes by mounting logs(`/var/log`) to RAM.  
 Just follow instruction in [Log2Ram README.md](https://github.com/azlux/log2ram) to install.

 If Log2Ram's systemd service fails after reboot, just manually start by command(`$ sudo systemctl start log2ram`) and reboot again.

## Packages installed
 ### via APT
  - `podman` to run/manage Home Assistant container
    - Can be replaced with `docker` or other OCI-compliant runtimes
  
## Security hardening
 ### Firewall
  - Use Ubuntu's default firewall, **UFW**
  ```sh
  # Enable UFW, this will reject all of incoming connections by default if there's no allow rules
  $ sudo ufw enable

  # Allow SSH connection only from local network, change `192.168.0.0/24` with your local network IP range
  $ sudo ufw allow proto tcp from 192.168.0.0/24 to any port 22
  ```

RPi-SenseStation Home Assistant setup
=====================================
Most of parts referenced from [official documentation](https://www.home-assistant.io/installation/raspberrypi).

## `podman` run commands
```sh
# Create directory for Home Assistant configs
$ sudo mkdir -p /data/homeassistant/config
$ sudo chown somni:somni -R /data

# Run Home Assistant container using podman
$ podman run -d \
             --rm \
             --name homeassistant \
             -e TZ=Asia/Seoul \
             -u $(id -u):$(id -g) \
             -v /data/homeassistant/config:/config:Z,U \
             --net=host \
             docker.io/homeassistant/home-assistant:latest

# Enable UFW firewall and allow Home Assistant Web UI port
$ sudo ufw enable
$ sudo ufw allow 8123/tcp

# Generate and enable Systemd service file to make Home Assistant container starts on boot automatically
$ podman generate systemd --new --name homeassistant | sudo tee /etc/systemd/user/container-homeassistant.service
$ systemctl --user enable container-homeassistant
$ sudo loginctl enable-linger somni

# Reboot is recommended
```
  - **`--rm`**: Removes container when exit. Home Assistant container doesn't do great when restart its stopped container...
  - **`-e TZ=Asia/Seoul`**: Change `Asia/Seoul` with timezone string of your home region
  - **`-v /data/homeassistant/config:/config:Z,U`**: Bind container `/config` directory with host `/data/homeassistant/config` directory
    - If you concern about `Z,U` flags, please refer [RedHat's article](https://www.redhat.com/sysadmin/debug-rootless-podman-mounted-volumes)
  - **`--net=host`**: Use host network directly
  - **`docker.io/homeassistant/home-assistant:latest`**: [Official documentation](https://www.home-assistant.io/installation/raspberrypi#platform-installation) suggests to use one from [GitHub Packages](https://github.com/home-assistant/core/pkgs/container/home-assistant), but GitHub Packages is too slow in my case so I pulled one from [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant)

## Troubleshooting
### Container does not start with Python error log `ValueError: Bad marshal data`
 - Just remove Home Assistant image and re-pull the image. The image file may be damaged by some reasons.
   ```sh
   $ podman rmi home-assistant
   $ podman pull docker.io/homeassistant/home-assistant:latest   # or just execute `podman run` command above
   ```

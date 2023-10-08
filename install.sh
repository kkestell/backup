#!/usr/bin/env bash

mkdir -p ~/.local/bin
cp backup.sh ~/.local/bin/backup.sh
chmod +x ~/.local/bin/backup.sh

mkdir -p ~/.config/systemd/user/
cp backup.service ~/.config/systemd/user/
cp backup.timer ~/.config/systemd/user/

systemctl --user daemon-reload
systemctl --user enable --now backup.timer

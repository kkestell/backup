# Backup

Install the script and Systemd timer:

```console
./install.sh
```

## Usage

Run now:

```console
systemctl --user start backup.service
```

## Troubleshooting

Logs:

```
journalctl --user -u backup.service -f
```

Status:

```
systemctl --user status backup.timer
systemctl --user status backup.service
```

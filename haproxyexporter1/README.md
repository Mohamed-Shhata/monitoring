# Ansible Role: haproxy exporter

## Description

Deploy prometheus [haproxy exporter](https://github.com/prometheus/haproxy_exporter) using ansible.

Based on [ansible node exporter](https://github.com/cloudalchemy/ansible-node-exporter).

## Requirements

- Ansible >= 2.5 (It might work on previous versions, but we cannot guarantee it)
- gnu-tar on Mac deployer host (`brew install gnu-tar`)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file.

## Example

### Playbook

Use it in a playbook as follows:
```yaml
- hosts: all
  roles:
    - lr1980.ansible-haproxy-exporter
```

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.

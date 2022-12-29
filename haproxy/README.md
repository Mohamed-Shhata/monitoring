## Ansible Collection - m4eba.haproxy

Install:

```
ansible-galaxy collection install m4eba.haproxy
```

Or add to requirements.yml

```
---
collections:
  - name: m4eba.haproxy
```

### Roles

#### haproxy

Install haproxy from the packetmanager, need to update cache first.

```
tasks:
  - ansible.builtin.import_role:
      name: m4eba.common.update_package_cache
  - ansible.builtin.import_role:
      name: m4eba.haproxy.haproxy
```

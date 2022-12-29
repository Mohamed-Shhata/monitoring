# Ansible Role mafalb.apache.httpd

## Basic Usage

```yaml
- name: install httpd with vendor config
  hosts: localhost
  roles:
  - role: mafalb.apache.httpd
```

```yaml
- name: install httpd as Software Collection
  hosts: localhost
  roles:
  - role: mafalb.apache.httpd
    httpd_scl_prefix: httpd24
```

```yaml
- name: install httpd
  hosts: localhost
  roles:
  - role: mafalb.apache.httpd
    httpd_cfgs:
    - dest: __main_config  # special name for main config
      yaml: { ... }  # config as yaml
    - src: myowntemplate.j2  # config as template
      dest: myowntemplate.conf
    - dest: test.conf
      yaml:  # config as yaml
        EnableSendfile: 'on'
      dest: test.conf
```

The above config snippet shows that there are multiple ways to specify the configuration.
If you specify src, then the template will be used.
If you specify yaml, then the provided default template will be used which translates the provided yaml dict into apache config.

It is possible to do configuration only. This can be useful to create VirtualHost configuration after apache is already configured.
Apache will not be installed nor started, but the reload handler will be notified. Note that the config is validated, so apachectl must be present.

```yaml
  - role: mafalb.apache.httpd
    do: cfg
    cfgs: [ ... ]
```

## Variables

see the [argument specs](roles/httpd/meta/argument_specs.yml)

## License

GPL-3.0-or-later

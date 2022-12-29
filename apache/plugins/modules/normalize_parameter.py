#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021 Markus Falb <markus.falb@mafalb.at>
# GNU General Public License v3.0+
# see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt

# This is a virtual module that is entirely implemented as an action plugin
# and runs on the controller

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: normalize_parameter
short_description: >
  take a list of apache httpd config files and return a slightly modified version of that list
version_added: "0.0.1"
description: take a list of config files and return a slightly modified version of that list
options:
  parameter:
    description:
      - The name of the variable that should act as the input of processing
      - This is used by mafalb.apache.httpd, I dont know if it's useful
      - outside of that.
    type: str
    required: true
author:
- Markus Falb (@mafalb)
'''

EXAMPLES = r'''
- name: create modified cfgs list
  mafalb.apache.normalize_parameter:
    parameter: "{{ 'cfgs' if cfgs is defined else 'httpd_cfgs' }}"
  when: cfgs is defined or httpd_cfgs is defined
  register: _cfgs
'''

RETURN = r'''
original_data:
  description:
    - return the unmodified list in C(original_data)
  returned: always
  type: dict
  sample:
  - dest: _main_config
  - src: bla.conf.j2
    dest: bla.conf
  - dest: bla1.conf
    yaml:
      LogFormat: '"%h gugu" justforCI'
data:
  description: return the modified list in C(data)
  returned: always
  type: dict
  sample:
  - src: 'mafalb.apache.httpd.conf.j2'
    dest: /etc/httpd/conf/httpd.conf
  - src: bla.conf.j2
    dest: bla.conf
  - src: 'mafalb.apache.httpd.conf.j2'
    dest: bla1.conf
    yaml:
      LogFormat: '"%h gugu" justforCI'
'''

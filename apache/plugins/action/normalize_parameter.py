# -*- coding: utf-8 -*-

# Copyright (c) 2021 Markus Falb <markus.falb@mafalb.at>
# GNU General Public License v3.0+
# see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleError
from ansible.parsing.yaml.objects import AnsibleMapping


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}
        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect
        result['changed'] = False
        result['failed'] = False
        result['original_data'] = task_vars[self._task.args['parameter']]
        result['data'] = []
        result['data'] = task_vars[self._task.args['parameter']]
        templates = result['data']
        if templates == []:
            return result
        for t in templates:
            if not isinstance(t, AnsibleMapping):
                raise AnsibleError("t is not an AnsibleMapping: {var}".format(var=t))
            # mangle destination
            if t['dest'] == '_main_config':
                t['dest'] = self._templar.template(task_vars['httpd_main_cfg'])
            elif not t['dest'].startswith('/'):
                if 'httpd_vhosts_d_wr' in task_vars:
                    t['dest'] = self._templar.template(task_vars['httpd_conf_d_wr'])\
                        + '/' + self._templar.template(t['dest'])
                else:
                    t['dest'] = self._templar.template(task_vars['httpd_conf_d'])\
                        + '/' + self._templar.template(t['dest'])
            # mangle src
            if 'src' not in t:
                t['src'] = self._templar.template(task_vars['httpd_default_template'])
        result['data'] = templates
        return result

#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: scion_package_info
short_description: This module returns information about the currently installed anapaya-scion package.
version_added: "1.0.0"
options:
extends_documentation_fragment:
    - anapaya.appliance.scion_package_info
author:
    - Lukas Bischofberger (@worxli)
requirements:
    - pydantic
'''

EXAMPLES = r'''
- name: Get current the anapaya scion package information
  anapaya.appliance.scion_package_info:
'''

RETURN = r'''
version:
    description: The version of the currently installed anapaya-scion package.
    type: str
    returned: always
    sample: v0.37.0
checksum:
    description: The checksum of the currently installed anapaya-scion package.
    type: str
    returned: always
    sample: bd546398fad055034850fbe83c16c4712c7280a013c040298b737da9590e4fe9
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.appliance_api_client.rest import ApiException
from ansible.module_utils.appliance_api_client.api import software_api
from ansible.module_utils.appliance_api_client import Configuration, ApiClient
from pprint import pprint

def main():
    result = dict(
        changed=False,
    )

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    # See configuration.py for a list of all supported configuration parameters.
    configuration = Configuration(
        host = "https://localhost/api/v1",
        verify_ssl = False
    )

    # Enter a context with an instance of the API client
    with ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = software_api.SoftwareApi(api_client)

        try:
            # Get the current package version
            api_response = api_instance.software_scion_installed_get()
            pprint(api_response)
            result['checksum'] = api_response.checksum
            result['version'] = api_response.version
        except ApiException as e:
            print("Exception when calling software_api: %s\n" % e)

    module.exit_json(**result)

if __name__ == '__main__':
    main()

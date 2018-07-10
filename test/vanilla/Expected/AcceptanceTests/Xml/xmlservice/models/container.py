# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Container(Model):
    """An Azure Storage container.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param properties: Required.
    :type properties: ~xmlservice.models.ContainerProperties
    :param metadata:
    :type metadata: dict[str, str]
    """

    _validation = {
        'name': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str', 'xml': {'name': 'Name'}},
        'properties': {'key': 'Properties', 'type': 'ContainerProperties', 'xml': {'name': 'Properties'}},
        'metadata': {'key': 'Metadata', 'type': '{str}', 'xml': {'name': 'Metadata'}},
    }
    _xml_map = {
    }

    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.properties = kwargs.get('properties', None)
        self.metadata = kwargs.get('metadata', None)

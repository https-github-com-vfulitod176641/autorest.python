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


class PetAPInPropertiesWithAPString(Model):
    """PetAPInPropertiesWithAPString.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, str]
    :param id:
    :type id: int
    :param name:
    :type name: str
    :ivar status:
    :vartype status: bool
    :param odatalocation:
    :type odatalocation: str
    :param additional_properties1:
    :type additional_properties1: dict[str, float]
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
        'odatalocation': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
        'odatalocation': {'key': '@odata\\.location', 'type': 'str'},
        'additional_properties1': {'key': 'additionalProperties', 'type': '{float}'},
    }

    def __init__(self, id, odatalocation, additional_properties=None, name=None, additional_properties1=None):
        super(PetAPInPropertiesWithAPString, self).__init__()
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status = None
        self.odatalocation = odatalocation
        self.additional_properties1 = additional_properties1
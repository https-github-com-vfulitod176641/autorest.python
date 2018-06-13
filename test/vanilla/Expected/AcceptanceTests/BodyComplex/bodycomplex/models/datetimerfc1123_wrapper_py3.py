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


class Datetimerfc1123Wrapper(Model):
    """Datetimerfc1123Wrapper.

    :param field:
    :type field: datetime
    :param now:
    :type now: datetime
    """

    _attribute_map = {
        'field': {'key': 'field', 'type': 'rfc-1123'},
        'now': {'key': 'now', 'type': 'rfc-1123'},
    }

    def __init__(self, *, field=None, now=None, **kwargs) -> None:
        super(Datetimerfc1123Wrapper, self).__init__(**kwargs)
        self.field = field
        self.now = now
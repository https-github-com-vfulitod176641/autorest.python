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
from msrest.exceptions import HttpOperationError


class ArrayOptionalWrapper(Model):
    """ArrayOptionalWrapper.

    :param value:
    :type value: list[str]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ArrayOptionalWrapper, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ArrayWrapper(Model):
    """ArrayWrapper.

    All required parameters must be populated in order to send to Azure.

    :param value: Required.
    :type value: list[str]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ArrayWrapper, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ClassOptionalWrapper(Model):
    """ClassOptionalWrapper.

    :param value:
    :type value: ~requiredoptional.models.Product
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'Product'},
    }

    def __init__(self, **kwargs):
        super(ClassOptionalWrapper, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ClassWrapper(Model):
    """ClassWrapper.

    All required parameters must be populated in order to send to Azure.

    :param value: Required.
    :type value: ~requiredoptional.models.Product
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'Product'},
    }

    def __init__(self, **kwargs):
        super(ClassWrapper, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class Error(Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.message = kwargs.get('message', None)


class ErrorException(HttpOperationError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorException, self).__init__(deserialize, response, 'Error', *args)


class IntOptionalWrapper(Model):
    """IntOptionalWrapper.

    :param value:
    :type value: int
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(IntOptionalWrapper, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class IntWrapper(Model):
    """IntWrapper.

    All required parameters must be populated in order to send to Azure.

    :param value: Required.
    :type value: int
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(IntWrapper, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class Product(Model):
    """Product.

    All required parameters must be populated in order to send to Azure.

    :param id: Required.
    :type id: int
    :param name:
    :type name: str
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)


class StringOptionalWrapper(Model):
    """StringOptionalWrapper.

    :param value:
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StringOptionalWrapper, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class StringWrapper(Model):
    """StringWrapper.

    All required parameters must be populated in order to send to Azure.

    :param value: Required.
    :type value: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StringWrapper, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
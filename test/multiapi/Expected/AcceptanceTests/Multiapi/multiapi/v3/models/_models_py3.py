# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Error(msrest.serialization.Model):
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

    def __init__(
        self,
        *,
        status: Optional[int] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class LanguagePagingResult(msrest.serialization.Model):
    """LanguagePagingResult.

    :param values:
    :type values: list[~multiapi.v3.models.PersonWhoSpeaksTheLanguage]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[PersonWhoSpeaksTheLanguage]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        values: Optional[List["PersonWhoSpeaksTheLanguage"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(LanguagePagingResult, self).__init__(**kwargs)
        self.values = values
        self.next_link = next_link


class ModelThree(msrest.serialization.Model):
    """Only exists in api version 3.0.0.

    :param optional_property:
    :type optional_property: str
    """

    _attribute_map = {
        'optional_property': {'key': 'optionalProperty', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        optional_property: Optional[str] = None,
        **kwargs
    ):
        super(ModelThree, self).__init__(**kwargs)
        self.optional_property = optional_property


class PagingResult(msrest.serialization.Model):
    """PagingResult.

    :param values:
    :type values: list[~multiapi.v3.models.ModelThree]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[ModelThree]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        values: Optional[List["ModelThree"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(PagingResult, self).__init__(**kwargs)
        self.values = values
        self.next_link = next_link


class PersonWhoSpeaksTheLanguage(msrest.serialization.Model):
    """PersonWhoSpeaksTheLanguage.

    :param name:
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        **kwargs
    ):
        super(PersonWhoSpeaksTheLanguage, self).__init__(**kwargs)
        self.name = name


class SourcePath(msrest.serialization.Model):
    """Uri or local path to source data.

    :param source: File source path.
    :type source: str
    """

    _validation = {
        'source': {'max_length': 2048, 'min_length': 0},
    }

    _attribute_map = {
        'source': {'key': 'source', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        source: Optional[str] = None,
        **kwargs
    ):
        super(SourcePath, self).__init__(**kwargs)
        self.source = source

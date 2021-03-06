﻿# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

import unittest
import subprocess
import sys
import isodate
import tempfile
import json
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "Header"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError

from header.aio import AutoRestSwaggerBATHeaderService
from header.models import GreyscaleColors

import pytest

class TestHeader(object):

    @pytest.mark.asyncio
    async def test_headers(self):
        client = AutoRestSwaggerBATHeaderService(base_url="http://localhost:3000")

        await client.header.param_integer("positive", 1)
        await client.header.param_integer("negative", -2)

        raw = await client.header.response_integer("positive", raw=True)
        assert 1 ==  int(raw.response.headers.get("value"))
        assert 1 ==  raw.headers.get("value")
        raw = await client.header.response_integer("negative", raw=True)
        assert -2 ==  raw.headers.get("value")

        await client.header.param_long("positive", 105)
        await client.header.param_long("negative", -2)

        raw = await client.header.response_long("positive", raw=True)
        assert 105 ==  raw.headers.get("value")
        raw = await client.header.response_long("negative", raw=True)
        assert -2 ==  raw.headers.get("value")

        await client.header.param_float("positive", 0.07)
        await client.header.param_float("negative", -3.0)

        raw = await client.header.response_float("positive", raw=True)
        assert abs(0.07 - raw.headers.get("value")) < 0.00001
        raw = await client.header.response_float("negative", raw=True)
        assert abs(-3.0 - raw.headers.get("value")) < 0.00001

        await client.header.param_double("positive", 7e120)
        await client.header.param_double("negative", -3.0)

        raw = await client.header.response_double("positive", raw=True)
        assert 7e120 ==  raw.headers.get("value")
        raw = await client.header.response_double("negative", raw=True)
        assert -3.0 ==  raw.headers.get("value")

        await client.header.param_bool("true", True)
        await client.header.param_bool("false", False)

        raw = await client.header.response_bool("true", raw=True)
        assert True ==  raw.headers.get("value")
        raw = await client.header.response_bool("false", raw=True)
        assert False ==  raw.headers.get("value")

        await client.header.param_string("valid", "The quick brown fox jumps over the lazy dog")
        await client.header.param_string("null", None)
        await client.header.param_string("empty", "")

        raw = await client.header.response_string("valid", raw=True)
        assert "The quick brown fox jumps over the lazy dog" ==  raw.headers.get("value")
        raw = await client.header.response_string("null", raw=True)
        assert None ==  json.loads(raw.headers.get("value"))
        raw = await client.header.response_string("empty", raw=True)
        assert "" ==  raw.headers.get("value")

        await client.header.param_enum("valid", GreyscaleColors.grey)
        await client.header.param_enum("valid", 'GREY')
        await client.header.param_enum("null", None)

        raw = await client.header.response_enum("valid", raw=True)
        assert GreyscaleColors.grey ==  raw.headers.get("value")

        # We receive an empty string.
        # Starting msrest 0.4.22, we consider that if a string is not in the enum, this not
        # a Deserialization issue and we return the string.
        # Here we now return empty string without failin **on purpose**
        # with pytest.raises(DeserializationError):
        raw = await client.header.response_enum("null", raw=True)
        assert "" ==  raw.headers.get("value")

        await client.header.param_date("valid", isodate.parse_date("2010-01-01"))
        await client.header.param_date("min", datetime.min)

        raw = await client.header.response_date("valid", raw=True)
        assert isodate.parse_date("2010-01-01") ==  raw.headers.get("value")
        raw = await client.header.response_date("min", raw=True)
        assert isodate.parse_date("0001-01-01") ==  raw.headers.get("value")

        await client.header.param_datetime("valid", isodate.parse_datetime("2010-01-01T12:34:56Z"))
        await client.header.param_datetime("min", datetime.min)

        raw = await client.header.response_datetime("valid", raw=True)
        assert isodate.parse_datetime("2010-01-01T12:34:56Z") ==  raw.headers.get("value")
        raw = await client.header.response_datetime("min", raw=True)
        assert isodate.parse_datetime("0001-01-01T00:00:00Z") ==  raw.headers.get("value")

        await client.header.param_datetime_rfc1123("valid", isodate.parse_datetime("2010-01-01T12:34:56Z"))
        await client.header.param_datetime_rfc1123("min", datetime.min)

        raw = await client.header.response_datetime_rfc1123("valid", raw=True)
        assert isodate.parse_datetime("2010-01-01T12:34:56Z") ==  raw.headers.get("value")
        raw = await client.header.response_datetime_rfc1123("min", raw=True)
        assert isodate.parse_datetime("0001-01-01T00:00:00Z") ==  raw.headers.get("value")

        await client.header.param_duration("valid", timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11))

        raw = await client.header.response_duration("valid", raw=True)
        assert timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11) ==  raw.headers.get("value")

        u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
        await client.header.param_byte("valid", u_bytes)

        raw = await client.header.response_byte("valid", raw=True)
        assert u_bytes ==  raw.headers.get("value")

        await client.header.param_existing_key("overwrite")

        raw = await client.header.response_existing_key(raw=True)
        assert "overwrite" ==  raw.headers.get('User-Agent')

        # This test is only valid for C#, which content-type can't be override this way
        #await client.header.param_protected_key("text/html")

        # This test has different result compare to C#, which content-type is saved in another place.
        raw = await client.header.response_protected_key(raw=True)
        assert "text/html; charset=utf-8", raw.headers.get('Content-Type')

        custom_headers = {"x-ms-client-request-id": "9C4D50EE-2D56-4CD3-8152-34347DC9F2B0"}
        raw = await client.header.custom_request_id(custom_headers=custom_headers, raw=True)
        assert raw.response.status_code ==  200

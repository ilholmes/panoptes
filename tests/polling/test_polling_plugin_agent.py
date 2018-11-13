"""
Copyright 2018, Oath Inc.
Licensed under the terms of the Apache 2.0 license. See LICENSE file in project root for terms.
"""

import collections
import glob
import json
import time
import unittest
from logging import getLogger, _loggerClass

from mock import patch, Mock, MagicMock
from mockredis import MockRedis
from redis.exceptions import TimeoutError
from zake.fake_client import FakeClient

from yahoo_panoptes.framework.configuration_manager import *
from yahoo_panoptes.framework.const import RESOURCE_MANAGER_RESOURCE_EXPIRE
from yahoo_panoptes.framework.context import *
from yahoo_panoptes.framework.resources import PanoptesResource, PanoptesResourceSet, PanoptesResourceDSL, \
    PanoptesContext, ParseException, ParseResults, PanoptesResourcesKeyValueStore, PanoptesResourceStore, \
    PanoptesResourceCache, PanoptesResourceError, PanoptesResourceCacheException, PanoptesResourceEncoder
from yahoo_panoptes.framework.utilities.helpers import ordered
from yahoo_panoptes.polling.polling_plugin_agent import PanoptesMetricsKeyValueStore, \
    PanoptesPollingPluginAgentKeyValueStore, PanoptesPollingPluginKeyValueStore, PanoptesPollingAgentContext, \
    PanoptesPollingTaskContext, PanoptesPollingPluginAgentError


class TestPollingPluginAgent(unittest.TestCase):
    def setUp(self):
        self._panoptes_polling_task_context = PanoptesPollingTaskContext()

    def test_basic_operations(self):
        pass
"""
Copyright 2018, Oath Inc.
Licensed under the terms of the Apache 2.0 license. See LICENSE file in project root for terms.
"""
import unittest

from mock import patch, MagicMock

from yahoo_panoptes.framework.utilities.consumer import PanoptesConsumer, PanoptesConsumerTypes
from yahoo_panoptes.framework.resources import PanoptesContext

from .helpers import get_test_conf_file

class TestPanoptesConsumer(unittest.TestCase):
    def setUp(self):
        self.my_dir, self.panoptes_test_conf_file = get_test_conf_file()
        self._panoptes_context = PanoptesContext(self.panoptes_test_conf_file)

    def test_basic_operations(self):
        panoptes_consumer = PanoptesConsumer(panoptes_context=self._panoptes_context,
                                             consumer_type=PanoptesConsumerTypes.METRICS,
                                             topics=[PanoptesConsumerTypes.METRICS],
                                             client_id="test",
                                             group="test_group",
                                             keys=)

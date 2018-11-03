"""
Copyright 2018, Oath Inc.
Licensed under the terms of the Apache 2.0 license. See LICENSE file in project root for terms.
"""
import unittest

from mock import patch, MagicMock

from yahoo_panoptes.framework.utilities.consumer import PanoptesConsumer, PanoptesConsumerTypes
from yahoo_panoptes.framework.resources import PanoptesContext

from .helpers import get_test_conf_file


class MockKafkaConsumer:
    def __init__(self):
        self._subscribed = []

    def subscribe(self, topics):
        for topic in topics:
            self._subscribed.append(topic)


def _callback():
    pass


class TestPanoptesConsumer(unittest.TestCase):
    def setUp(self):
        self.my_dir, self.panoptes_test_conf_file = get_test_conf_file()
        self._panoptes_context = PanoptesContext(self.panoptes_test_conf_file)

    def test_basic_operations(self):
        panoptes_consumer = PanoptesConsumer(panoptes_context=self._panoptes_context,
                                             consumer_type=PanoptesConsumerTypes.METRICS,
                                             topics=['metrics'],
                                             client_id="test",
                                             group="test_group",
                                             keys=["test_key"],
                                             poll_timeout=1,
                                             callback=_callback)

        # Test properties
        self.assertEqual(panoptes_consumer.panoptes_context, self._panoptes_context)
        self.assertEqual(panoptes_consumer.client_id, "test")
        self.assertEqual(panoptes_consumer.group, "test_group")
        # TODO seconds or milliseconds?
        self.assertEqual(panoptes_consumer.poll_timeout, 1000)
        self.assertEqual(panoptes_consumer.consumer_type, PanoptesConsumerTypes.METRICS)
        self.assertListEqual(panoptes_consumer.keys, ["test_key"])

        mock_kafka_consumer = MagicMock()

        with patch('yahoo_panoptes.framework.utilities.consumer.KafkaConsumer', mock_kafka_consumer):
            panoptes_consumer.start_consumer()

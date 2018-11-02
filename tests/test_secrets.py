import unittest

from mock import patch, MagicMock
from yahoo_panoptes.framework.utilities.secrets import PanoptesSecretsStore
from yahoo_panoptes.framework.resources import PanoptesContext
from yahoo_panoptes.framework.utilities.key_value_store import PanoptesKeyValueStore, PanoptesKeyValueStoreValidators
from yahoo_panoptes.framework.const import SECRETS_MANAGER_KEY_VALUE_NAMESPACE

from .test_framework import panoptes_mock_redis_strict_client
from .helpers import get_test_conf_file


class TestPanoptesSecretsStore(unittest.TestCase):
    @patch('redis.StrictRedis', panoptes_mock_redis_strict_client)
    def setUp(self):
        self.my_dir, self.panoptes_test_conf_file = get_test_conf_file()
        self._panoptes_context = PanoptesContext(self.panoptes_test_conf_file)

    def test_basic_operations(self):
        secrets_store = PanoptesSecretsStore(self._panoptes_context)
        self.assertEqual(secrets_store.namespace, SECRETS_MANAGER_KEY_VALUE_NAMESPACE)

        super(PanoptesSecretsStore, secrets_store).set(key="secret:test_site", value="test_secret")
        self.assertEqual(secrets_store.get_by_site("secret", "test_site"), "test_secret")

        def get_with_exceptions(key):
            if key == 

        # Test exceptions
        mock_get = MagicMock(side_effect=Exception)
        with patch('yahoo_panoptes.framework.utilities.secrets.PanoptesKeyValueStore.get',
                   mock_get):
            with self.assertRaises(Exception):
                secrets_store.get_by_site("secret", "test_site", fallback_to_default=False)
            with self.assertRaises(Exception):
                secrets_store.get_by_site("secret", "test_site")

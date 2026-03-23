import unittest
from unittest.mock import MagicMock, patch
import sys

# Mock scapy before importing the module that uses it
mock_scapy = MagicMock()
sys.modules["scapy"] = mock_scapy
sys.modules["scapy.all"] = mock_scapy.all
sys.modules["scapy.layers"] = mock_scapy.layers
sys.modules["scapy.layers.dot11"] = mock_scapy.layers.dot11
sys.modules["scapy.layers.eap"] = mock_scapy.layers.eap

import demo.handshake_detector

class TestHandshakeFilter(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args')
    @patch('demo.handshake_detector.sniff')
    def test_sniff_called_with_filter(self, mock_sniff, mock_args):
        # Setup mock arguments
        mock_args.return_value = MagicMock(interface='wlan0mon')

        # Call the main function
        demo.handshake_detector.main()

        # Verify sniff was called
        mock_sniff.assert_called()

        # Check if filter parameter is present and correct
        _, kwargs = mock_sniff.call_args
        self.assertIn('filter', kwargs, "sniff() was called without a 'filter' parameter")
        self.assertEqual(kwargs['filter'], 'ether proto 0x888e', f"Expected filter 'ether proto 0x888e', got '{kwargs.get('filter')}'")

if __name__ == '__main__':
    unittest.main()

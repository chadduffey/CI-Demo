"""
Unit Tests
"""

import sampleapp


class TestSampleApp:

    def test_addition(self):
        assert 4 == sampleapp.add(2, 2)

    def test_subtraction(self):
        assert 2 == sampleapp.subtract(4, 2)

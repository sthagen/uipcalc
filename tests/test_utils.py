import six

import pytest

import uipcalc.utils


@pytest.mark.parametrize("test_input, expected", [
    ('192.168.0.1', [
        '1', '1', '0', '0', '0', '0', '0', '0',
        '1', '0', '1', '0', '1', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '1']),
    ('192.168.1.1', [
        '1', '1', '0', '0', '0', '0', '0', '0',
        '1', '0', '1', '0', '1', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '1',
        '0', '0', '0', '0', '0', '0', '0', '1']),
    ('2001:DB8::F', [
        '0', '0', '1', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '1',
        '0', '0', '0', '0', '1', '1', '0', '1',
        '1', '0', '1', '1', '1', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '1', '1', '1', '1']),
    ('2001:DB8:ABC:DEF::1', [
        '0', '0', '1', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '1',
        '0', '0', '0', '0', '1', '1', '0', '1',
        '1', '0', '1', '1', '1', '0', '0', '0',
        '0', '0', '0', '0', '1', '0', '1', '0',
        '1', '0', '1', '1', '1', '1', '0', '0',
        '0', '0', '0', '0', '1', '1', '0', '1',
        '1', '1', '1', '0', '1', '1', '1', '1',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '1']),
])
def test_addr_to_bin(test_input, expected):
    assert uipcalc.utils.addr_to_bin(six.u(test_input)) == expected

@pytest.mark.parametrize("test_input, expected", [
    ('192.168.0.1', [
        '1', '1', '0', '0', '0', '0', '0', '0',
        '1', '0', '1', '0', '1', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '1', '1']),
    ('192.168.1.1', [
        '1', '1', '0', '0', '0', '0', '0', '0',
        '1', '0', '1', '0', '1', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '1', '1',
        '0', '0', '0', '0', '0', '0', '0', '1']),
    ('2001:DB8::F', [
        '0', '0', '1', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '1',
        '0', '0', '0', '0', '1', '1', '0', '1',
        '1', '0', '1', '1', '1', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '1', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '1', '1', '1', '1']),
    ('2001:DB8:ABC:DEF::1', [
        '0', '0', '1', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '1',
        '0', '0', '0', '0', '1', '1', '0', '1',
        '1', '0', '1', '1', '1', '0', '0', '0',
        '0', '0', '0', '0', '1', '0', '1', '0',
        '1', '0', '1', '1', '1', '1', '0', '0',
        '0', '0', '0', '0', '1', '1', '0', '1',
        '1', '1', '1', '0', '1', '1', '1', '1',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '1', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0', '0', '0', '1']),
])
def test_addr_to_bin_fail(test_input, expected):
    assert uipcalc.utils.addr_to_bin(six.u(test_input)) != expected
"""
Tests for Packet32.
"""


from irobot.packet import Packet32


def test_id():
    """Tests the packet `id`."""
    assert Packet32.id == 32


def test_size():
    """Tests the packet `size`."""
    assert Packet32.size == 1


def test_from_bytes():
    """Tests `from_bytes`."""
    data = bytes([0x00])
    packet = Packet32.from_bytes(data)
    assert packet is not None
    assert type(packet) == Packet32
    assert packet.unused_byte == 0

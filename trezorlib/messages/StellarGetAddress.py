# Automatically generated by pb2py
from .. import protobuf as p
if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None


class StellarGetAddress(p.MessageType):
    MESSAGE_WIRE_TYPE = 207
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
    }

    def __init__(
        self,
        address_n: List[int] = None
    ) -> None:
        self.address_n = address_n if address_n is not None else []

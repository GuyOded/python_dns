"""

"""


class DnsEntry(object):
    # DNS_TYPE_PTR = 0xc
    # DNS_TYPE_A = 0x1

    def __init__(self, dns_type="A", name="", ttl="", addr=""):
        """
        :type dns_type: str
        :type name: str
        :type ttl: str
        :type addr: str
        """
        self._dns_type = dns_type
        self._name = name
        self._addr = addr
        self._ttl = ttl

    def get_type(self):
        return self._dns_type

    def set_type(self, dns_type):
        self._dns_type = dns_type

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_addr(self):
        return self._addr

    def set_addr(self, addr):
        self._addr = addr

    def get_ttl(self):
        return self._ttl

    def set_ttl(self, ttl):
        self._ttl = ttl

    def compare_without_ttl(self, dns_entry):
        """
        :type dns_entry: DnsEntry
        """
        return dns_entry._name == self._name and \
            dns_entry._addr == self._addr and \
            dns_entry._dns_type == self._dns_type

    """
    implementing an __str__ slot breaks the single responsibility
    principle that should never be broken
    """

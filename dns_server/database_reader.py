import re

class DatabaseReader(object):
    def __init__(self, file_name, entry_separator="\n"):
        """
        :type entry_separator: str
        :type file_name: str
        """
        self._file_name = file_name
        self._delim= delim
        self._entry_separator = entry_separator

    def search(self, dns_entry):
        """
        :type dns_entry: DnsEntry
        :rtype: bool

        opens for reading
        """
        pass

    def add_entry(self, dns_entry):
        """
        :type dns_entry: DnsEntry
        :rtype: bool

        :return: True if the entry was added or False if it wasn't
                 in case it was found in the database

        opens for appending
        """
        pass


class DatabaseEntryParser(object):
    def __init__(self, delim, num_of_elements):
        """
        :type delim: str
        :type num_of_elements: int
        """
        self._delim = delim
        self._num_of_elements = num_of_elements

    def split_entry(self, entry):
        """
        :type entry: str
        """

        l_elements = entry.split(self._delim)

        if len(l_elements) != self._num_of_elements:
            raise ValueError("Expected {} elements in\
                              entry and not {}".format(self._num_of_elements, len(l_elements)))

        return l_elements


class DnsEntry(object):
    # DNS_TYPE_PTR = 0xc
    # DNS_TYPE_A = 0x1

    def __init__(self, dns_type=5, name="", ttl="", addr=""):
        """
        :type dns_type: int
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
        return dns_entry._name == self._name and 
               dns_entry._addr == self._addr and
               dns_entry._dns_type == self._dns_type

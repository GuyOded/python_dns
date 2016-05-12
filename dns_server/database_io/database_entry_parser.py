from database_format import *
from dns_entry import DnsEntry


class DatabaseEntryParser(object):

    @staticmethod
    def string_to_entry(entry_string):
        """
        :type entry_string: str
        :rtype: DnsEntry
        :return: dns_entry
        """
        num_of_fields = len(ENTRY_ORDER.items())

        elements = entry_string.split(DELIMITER)
        elements[-1] = elements[-1].strip()

        if len(elements) != num_of_fields:
            raise ValueError("database entry out of"
                             " format: expected {0}".format(num_of_fields))

        dns_entry = DnsEntry(dns_type=elements[ENTRY_ORDER["type"]],
                             name=elements[ENTRY_ORDER["name"]],
                             ttl=elements[ENTRY_ORDER["ttl"]],
                             addr=elements[ENTRY_ORDER["addr"]])

        return dns_entry

    @staticmethod
    def entry_to_string(dns_entry):
        """
        :type dns_entry: DnsEntry
        :return: a string version of the dns_entry
        """
        formatted = STRING_FORMAT.format(type=dns_entry.get_type(),
                                         delim=DELIMITER,
                                         name=dns_entry.get_name(),
                                         addr=dns_entry.get_addr(),
                                         ttl=dns_entry.get_ttl())
        return formatted

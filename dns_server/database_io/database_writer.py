"""
"""
import dns_entry
from database_entry_parser import DatabaseEntryParser
import os


class DatabaseWriter(object):
    def __init__(self, file_name):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        self._file_name = os.path.join(dir_name, file_name)

    def exists(self, domain_name):
        """

        :param domain_name: the domain that the caller wishes to find
        :type domain_name: str
        :return:
        :rtype: bool
        """
        try:
            database = open(self._file_name, "r")
        except IOError:
            print "Unable to open database: {}".format(self._file_name)
            raise

        lines = database.read().split()
        for line in lines:
            entry = DatabaseEntryParser.string_to_entry(line)
            if entry.get_name() == domain_name:
                return True

        database.close()

        return False

    def add_entry_to_database(self, entry):
        """
        :param entry: The entry that is wished to be added
        :type entry: dns_entry.DnsEntry
        :return: True if the entry was added False otherwise
        :rtype: bool
        """
        if self.exists(entry.get_name()):
            return False

        try:
            database = open(self._file_name, "a")
        except IOError:
            print "Unable to open database: {}".format(self._file_name)
            raise

        database.write(DatabaseEntryParser.entry_to_string(entry))

        database.close()

        return True

    def delete_by_name(self, domain_name):
        """

        deletes all occurrences of the specified name

        :type domain_name: str
        :param domain_name:
        :return: True or False
        :rtype: bool
        """
        if not self.exists(domain_name):
            return False

        try:
            database = open(self._file_name, "r")
        except IOError:
            print "Unable to open database: {}".format(self._file_name)
            raise

        lines = database.readlines()
        database.close()

        database.open("w")
        for line in lines:
            entry = DatabaseEntryParser.string_to_entry(line)
            if entry.get_name() == domain_name:
                continue

            database.write(line)

        return True

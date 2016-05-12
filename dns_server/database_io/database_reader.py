import dns_entry
from database_entry_parser import DatabaseEntryParser
import os


class DatabaseReader(object):
    def __init__(self, file_name):
        """
        :type file_name: str
        """
        dir_name = os.path.dirname(os.path.abspath(__file__))
        self._file_name = os.path.join(dir_name, file_name)

    def search(self, domain_name):
        """
        :param domain_name: the name that the caller wishes to find
        :type domain_name: str
        :rtype: bool
        opens for reading
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
                return entry

        database.close()

        return None

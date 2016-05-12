from dns_server.database_io import *


def main():
    print "testing database writer"

    test_database_writer()

    print "done"


def test_database_writer():
    """

    :return: None
    """
    db_writer = database_writer.DatabaseWriter("database.txt")
    entry = dns_entry.DnsEntry("A", "www.google.com", "1", "216.58.214.36")

    db_writer.add_entry_to_database(entry)


def test_database_reader():
    """

    :return: None
    """
    


if __name__ == "__main__":
    main()
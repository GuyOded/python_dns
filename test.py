from dns_server.database_io import *


def main():
    print "testing"

    # test_database_writer()

    test_database_reader()

    print "done"


def test_database_writer():
    """

    :return: None
    """
    db_writer = database_writer.DatabaseWriter("database.txt")
    entry = dns_entry.DnsEntry("A", "www.google.com", "1", "216.58.214.36")

    db_writer.add_entry_to_database(entry)

    assert db_writer.exists("www.google.com")


def test_database_reader():
    """

    :return: None
    """
    test_database_writer()

    db_reader = database_reader.DatabaseReader("database.txt")

    entry = db_reader.search("www.google.com")

    assert entry is not None

    assert entry.get_addr() == "216.58.214.36"

    print database_entry_parser.DatabaseEntryParser.entry_to_string(entry)


def test_delete_entry():
    db_writer = database_writer.DatabaseWriter("database.txt")

    db_writer.delete_by_name("www.google.com")


if __name__ == "__main__":
    main()
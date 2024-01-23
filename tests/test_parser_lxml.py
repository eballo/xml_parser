from src.parser.parser_lxml import LxmlParser


def read_xml(filename: str) -> str:
    with open(filename) as f:
        s = f.read()
    return s


def test_parser_lxml():
    xml_file = read_xml("fixtures/books.xml")
    # print(xml_file)
    parser = LxmlParser()
    books = parser.parse(xml_file)

    assert len(books) == 12

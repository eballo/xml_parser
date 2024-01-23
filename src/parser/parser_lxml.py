from io import StringIO, BytesIO

from lxml import etree

from src.model.book import Book


class LxmlParser(object):
    def __init__(self):
        self.parser = etree.XMLParser(remove_blank_text=True)

    def parse(self, str_xml):
        books = []
        xml_bytes = BytesIO(str_xml.encode("UTF-8"))
        context = etree.iterparse(xml_bytes, events=("start", "end"), tag="book")
        for action, element in context:
            print("%s: %s" % (action, element.tag))
            print(element.attrib)
            if action == "start":
                id = element.attrib.get("id")

                author = element.find("author").text
                title = element.find("title").text
                genre = element.find("genre").text
                price = element.find("price").text
                publish_date = element.find("publish_date").text
                description = element.find("description").text

                cities = element.findall("locations/city")
                for city in cities:
                    name = city.find("name")
                    print("name" + name.text)

                book = Book(id=id, author=author, title=title, genre=genre, price=price, publish_date=publish_date, description=description)
                books.append(book)

            if action == "end":
                element.clear()

        return books
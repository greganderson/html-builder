from tag import Tag


class Document:
    """ HTML Document """

    def __init__(self, filename: str):
        # Filename of the HTML file this will write to
        self.filename = filename

        self.html = Tag("html")
        self.head = Tag("head")
        self.body = Tag("body")

        self.html.add_child(self.head)
        self.html.add_child(self.body)
    
    def write_html_file(self) -> None:
        with open(self.filename, "w") as f:
            f.write("\n".join(self.html.listify()))


def main():
    document = Document("test.html")

    header = Tag("header")
    header.add_child(Tag("h1", contents="My Second Personal Webpage!"))
    document.body.add_child(header)

    section1 = Tag("section")
    document.body.add_child(section1)

    section1.add_child(Tag("h2", contents="About Me"))

    # Hobbies
    hobbies = Tag("ul")
    hobbies.add_child(Tag("li", contents="Teaching"))
    hobbies.add_child(Tag("li", contents="Machining"))
    hobbies.add_child(Tag("li", contents="Blacksmithing"))
    hobbies.add_child(Tag("li", contents="Piano"))
    section1.add_child(hobbies)

    footer = Tag("footer")
    document.body.add_child(footer)

    p = Tag("p", contents="I'm unreachable, sorry. Nobody can contact me.")
    p.add_attribute("style", "background-color: red;")
    footer.add_child(p)

    document.write_html_file()

if __name__ == "__main__":
    main()
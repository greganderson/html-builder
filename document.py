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

    document.write_html_file()

if __name__ == "__main__":
    main()
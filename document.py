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

    def input_loop(self) -> None:
        current_tag = self.body
        while True:
            print()
            self.print_tag_info(current_tag)
            print()

            print("What would you like to do:")
            print("1. Add a child tag")
            print("2. Add an attribute")
            print("3. Edit child tag")
            print("4. Remove child tag")
            print("5. Finish tag")
            print()

            choice = input("Enter choice: ")
            if choice == "1":
                child = self.add_child(current_tag)
                if child is not None:
                    current_tag = child
            elif choice == "5":
                break

    def print_tag_info(self, tag: Tag) -> None:
        print(f"Current tag: {tag}")
        print()
        children_string = "None"
        if len(tag.children) > 0:
            children_string = "\n".join([str(child) for child in tag.children])

        print(f"Children: {children_string}")

    def add_child(self, tag: Tag) -> Tag:
        """
        Adds a child to the tag. If contents are provided, it returns None to signify the
        child tag is complete. Otherwise it returns the tag, which will then become the new working
        tag.
        """
        print("Adding a child")
        print()
        name = input("Name: ")
        contents = input("Contents (leave blank for none): ")

        child = Tag(name, contents=contents)
        tag.add_child(child)

        return child if contents == "" else None

    
    def write_html_file(self) -> None:
        with open(self.filename, "w") as f:
            f.write("\n".join(self.html.listify()))


def main(fill_with_sample_content: bool = True):
    document = Document("test.html")

    if fill_with_sample_content:
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

    document.input_loop()

    document.write_html_file()

if __name__ == "__main__":
    main(fill_with_sample_content=False)
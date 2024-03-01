from tag import Tag

import choices


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
            for key, value in choices.CHOICES.items():
                print(f"{key}. {value.text}")
            print()

            choice = input("Enter choice: ")

            if choice not in choices.CHOICES:
                print()
                print("Invalid choice.")
                continue

            result_tag = choices.CHOICES[choice].run_choice(current_tag)

            if result_tag is None:
                # Check if they're trying to be done
                if isinstance(choices.CHOICES[choice], choices.FinishTagChoice):
                    break
            else:
                current_tag = result_tag

    def print_tag_info(self, tag: Tag) -> None:
        print(f"Current tag: {tag}")
        print()
        children_string = None
        if len(tag.children) > 0:
            children_string = "\n\t".join([str(child) for child in tag.children])

        # Print the children in a somewhat non-terrible format
        if children_string is not None:
            print(f"Children:")
            print(f"\t{children_string}")
        else:
            print(f"Children: None")

    def write_html_file(self) -> None:
        print(f"Writing HTML file to {self.filename}...")
        with open(self.filename, "w") as f:
            f.write("\n".join(self.html.listify()))
        print(f"File written.")


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
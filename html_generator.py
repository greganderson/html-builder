from abc import ABC, abstractmethod

from tag import Tag


class Choice(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def run_choice(self, tag: Tag):
        pass

class AddChildChoice(Choice):
    def __init__(self):
        super().__init__(text="Add a child tag")

    def run_choice(self, tag: Tag):
        """
        Adds a child to the tag. If contents are provided, it returns None to signify the
        child tag is complete. Otherwise it returns the tag, which will then become the new working
        tag.
        """
        print()
        print("Adding a child")
        print()
        name = input("Name: ")
        contents = input("Contents (leave blank for none): ")

        child = Tag(name, contents=contents)
        tag.add_child(child)

        return child if contents == "" else None

class AddAttributeChoice(Choice):
    def __init__(self):
        super().__init__(text="Add an attribute")

    def run_choice(self, tag: Tag) -> Tag:
        print("This option hasn't been implemented yet.")
        return tag

class EditAttributesChoice(Choice):
    def __init__(self):
        super().__init__(text="Edit attributes")

    def run_choice(self, tag: Tag) -> Tag:
        print("This option hasn't been implemented yet.")
        return tag

class EditChildTagChoice(Choice):
    def __init__(self):
        super().__init__(text="Edit child tag")

    def run_choice(self, tag: Tag) -> Tag:
        """ Prints the list of children, then asks the user to pick one """

        while True:
            print()
            for i, child in enumerate(tag.children):
                print(f"{i+1}: {child}")

            try:
                print()
                child_num = int(input("Enter child number: "))
                child = tag.children[child_num - 1]

                # Check if they're editing a tag that has contents instead of children.
                # We don't want to return the child if it's one of those.
                if child.contents != "":
                    print(f"Editing {child}:")
                    print()
                    child.contents = input("Enter new contents: ")
                    return tag
            except ValueError:
                print("Invalid choice.")

class RemoveChildTagChoice(Choice):
    def __init__(self):
        super().__init__(text="Remove child tag")

    def run_choice(self, tag: Tag) -> Tag:
        print("This option hasn't been implemented yet.")
        return tag

class FinishTagChoice(Choice):
    def __init__(self):
        super().__init__(text="Finish tag")

    def run_choice(self, tag: Tag) -> Tag:
        if tag.name == "body":
            be_done = input("Are you sure you want to be done? (y or n): ").lower()
            if be_done == "y" or be_done == "yes":
                return None
            else:
                # Do nothing
                return tag
        else:
            return tag.parent

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

        self.choices: dict[str, Choice] = {
            "1": AddChildChoice(),
            "2": AddAttributeChoice(),
            "3": EditAttributesChoice(),
            "4": EditChildTagChoice(),
            "5": RemoveChildTagChoice(),
            "6": FinishTagChoice(),
        }

    def input_loop(self) -> None:
        current_tag = self.body
        while True:
            print()
            self.print_tag_info(current_tag)
            print()

            print("What would you like to do:")
            for key, value in self.choices.items():
                print(f"{key}. {value.text}")
            print()

            choice = input("Enter choice: ")

            if choice not in self.choices:
                print()
                print("Invalid choice.")
                continue

            result_tag = self.choices[choice].run_choice(current_tag)

            if result_tag is None:
                # Check if they're trying to be done
                if isinstance(self.choices[choice], FinishTagChoice):
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
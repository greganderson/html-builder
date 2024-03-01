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


CHOICES: dict[str, Choice] = {
    "1": AddChildChoice(),
    "2": AddAttributeChoice(),
    "3": EditAttributesChoice(),
    "4": EditChildTagChoice(),
    "5": RemoveChildTagChoice(),
    "6": FinishTagChoice(),
}
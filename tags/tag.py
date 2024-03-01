class AlreadyHasContentError(Exception):
    """ Exception raised when a caller attempts to add a child when the tag already has content """
    def __init__(self, message: str):
        super().__init__(message)

class Tag:
    """ Base class for a generic tag """

    def __init__(self, name: str, contents: str = "", single_tag = False):
        # This is used when we finish a tag so we can go back to the parent (like a doubly linked list)
        # It starts as None, but when it is added with `add_child`, the parent gets set.
        self.parent: "Tag" = None

        # Name of the tag, like `h1` or `p`
        self.name = name

        self.attributes: dict[str, str] = {}
        
        # Either the tag has contents or it has children, but it cannot have both.
        self.children: list["Tag"] = []
        self.contents = contents
        self.single_tag = single_tag
    
    def add_attribute(self, key: str, value: str = "") -> None:
        self.attributes[key] = value
    
    def add_child(self, child: "Tag") -> None:
        """
        Adds a child tag, unless the tag already has contents, in which case an AlreadyHasContentError
        will be raised.
        """
        if self.contents != "":
            raise AlreadyHasContentError()
        child.parent = self
        self.children.append(child)
    
    def listify(self) -> list[str]:
        """
        Create a list of strings that represents each line of this tag, including children. Meant
        to be used with a `"\n".join(listify(tag))` call.

        TODO: listify isn't a very good name. Come up with a better one.
        """
        attribute_str = " ".join([f'{key}="{value}"' if value != "" else f'{key}' for key, value in self.attributes.items()])

        # My soul demands that this be here. It handles making sure there isn't a blank space after the tag
        # name if there aren't any attributes.
        if attribute_str != "":
            attribute_str = " " + attribute_str

        open_tag = f"<{self.name}{attribute_str}>"
        if self.single_tag:
            close_tag = ""
        else:
            close_tag = f"</{self.name}>"

        if self.contents != "":
            complete_tag = f"{open_tag}{self.contents}{close_tag}"
            return [complete_tag]
        
        # Tag has children
        complete_tag_list = []
        for child in self.children:
            complete_tag_list += child.listify()
        
        return [open_tag] + complete_tag_list + [close_tag]

    def __str__(self) -> str:
        return f"<{self.name}>"
from tag import Tag

class DoctypeHTML(Tag):
    def __init__(self, name: str = "DOCTYPE!"):
        super().__init__(name, single_tag=True)
        self.add_attribute("html")

# Testing purposes only
def main():
    tag = DoctypeHTML()
    print(tag.listify())

if __name__ == "__main__":
    main()
class SimplifiedMarkdownEditor(object):
    def __init__(self):
        self.command = ["plain", "bold", "italic", "header", "link", "inline-code",
                        "ordered-list", "unordered-list", "new-line"]

    def help(self):
        print("Available formatters:")
        for i in self.command:
            print("*" + i)

    def done(self):
        pass


if __name__ == "__main__":
    x = SimplifiedMarkdownEditor()
    print("=" * 70)
    print("Welcome to the Simplified Markdown Editor!")
    while True:
        print("=" * 70)
        formatter = input("Choose a formatter: \n").lower().strip()
        if formatter == "!help":
            x.help()
        elif formatter == "!done":
            x.done()
            break
        else:
            print("Unknown formatting type or command")

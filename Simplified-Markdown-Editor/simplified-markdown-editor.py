class SimplifiedMarkdownEditor(object):
    def __init__(self):
        self.command = ["plain", "bold", "italic", "header", "link", "inline-code",
                        "ordered-list", "unordered-list", "new-line"]
        self.edit = []

    def help(self):
        print("Available formatters:")
        for j in self.command:
            print("*" + j)

    def done(self):
        pass

    def header(self):
        while True:
            while True:
                try:
                    num = int(input("Level: "))
                    break
                except ValueError:
                    print("Please enter a number!")
            if num <= 6:
                text = input("Text: ")
                self.edit.append(num * "#" + " " + text)
                break
            else:
                print("The level should be within the range of 1 to 6.")

    def plain(self):
        self.edit.append(input("Text: "))

    def new_line(self):
        self.edit.append("")

    def link(self):
        label = input("Label: ")
        url = input("URL: ")
        self.edit.append(f"[{label}]({url})")


if __name__ == "__main__":
    x = SimplifiedMarkdownEditor()
    print("=" * 70)
    print("Welcome to the Simplified Markdown Editor!")
    while True:
        if len(x.edit) == 0:
            print("=" * 70)
            formatter = input("Choose a formatter: \n").lower().strip()
        else:
            print("=" * 70 + "\nYour text is:")
            for i in x.edit:
                print(i)
            print("=" * 70)
            formatter = input("Choose a formatter: \n").lower().strip()
        if formatter == "!help":
            x.help()
        elif formatter == "!done":
            x.done()
            break
        else:
            if formatter == "header" or formatter == "h":
                x.header()
            elif formatter == "plain" or formatter == "p":
                x.plain()
            elif formatter == "new-line" or formatter == "nl":
                x.new_line()
            elif formatter == "link" or formatter == "l":
                x.link()
            else:
                print("Unknown formatting type or command")

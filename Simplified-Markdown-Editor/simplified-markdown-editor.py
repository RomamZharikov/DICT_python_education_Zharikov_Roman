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

    @staticmethod
    def input_list():
        while True:
            try:
                num = int(input("Number of rows: "))
                if num > 0:
                    break
                else:
                    print("The number of rows should be greater than zero!")
            except ValueError:
                print("Please enter a number!")
        return [input(f"Row #{k}: ") for k in range(1, num + 1)]

    def ordered_list(self):
        append_list = self.input_list()
        for k in range(len(append_list)):
            self.edit.append(f"{k + 1}. {append_list[k]}")

    def unordered_list(self):
        append_list = self.input_list()
        for k in range(len(append_list)):
            self.edit.append(f"* {append_list[k]}")

    def main(self):
        print("=" * 70)
        print("Welcome to the Simplified Markdown Editor!")
        while True:
            if len(self.edit) == 0:
                print("=" * 70)
                formatter = input("Choose a formatter: \n").lower().strip()
            else:
                print("=" * 70 + "\nYour text is:")
                for i in self.edit:
                    print(i)
                print("=" * 70)
                formatter = input("Choose a formatter: \n").lower().strip()
            if formatter == "!help":
                self.help()
            elif formatter == "!done":
                self.done()
                break
            else:
                if formatter == "header" or formatter == "h":
                    self.header()
                elif formatter == "plain" or formatter == "p":
                    self.plain()
                elif formatter == "new-line" or formatter == "nl":
                    self.new_line()
                elif formatter == "link" or formatter == "l":
                    self.link()
                elif formatter == "ordered-list" or formatter == "ol":
                    self.ordered_list()
                elif formatter == "unordered-list" or formatter == "ul":
                    self.unordered_list()
                else:
                    print("Unknown formatting type or command")


if __name__ == "__main__":
    x = SimplifiedMarkdownEditor()
    x.main()

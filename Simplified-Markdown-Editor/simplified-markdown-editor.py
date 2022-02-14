class SimplifiedMarkdownEditor(object):
    def __init__(self, name, choice):
        self.command = ["plain", "bold (in plain)", "italic (in plain)", "header", "link", "inline-code (in plain)",
                        "ordered-list", "unordered-list", "new-line"]
        self.edit = []
        self.choice = choice
        self.name = name

    def help(self):
        print("Available formatters:")
        for j in self.command:
            print("*" + j)

    def done(self):
        if overwrite == "yes" or overwrite == "y":
            with open(self.name, "w", encoding='utf-8') as text:
                self.edit = map(lambda k: k + "\n", self.edit)
                text.writelines(self.edit)
        else:
            num = 1
            check = self.name[0:-3]
            while True:
                self.name = f"{check}({num}).md"
                try:
                    with open(self.name, "r", encoding='utf-8') as q:
                        pass
                    num += 1
                except FileNotFoundError:
                    with open(self.name, "w", encoding='utf-8') as text:
                        self.edit = map(lambda k: k + "\n", self.edit)
                        text.writelines(self.edit)
                    break

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
        text = input("Text: ")
        while True:
            append = input("\nUsed italic, bold or incline code(yes or no)? \n").strip().lower()
            if append == "yes" or append == "y":
                print(text)
                piece = input("Enter the part of the text you want to change: \n")
                action = input("What to use (italic, bold or incline code): \n").strip().lower()
                if action == "italic":
                    text = self.italic(text, piece)
                elif action == "bold":
                    text = self.bold(text, piece)
                elif action == "incline code" or action == "ic":
                    text = self.inline_code(text, piece)
                else:
                    print("Please, write italic or bold!")
            elif append == "no" or append == "n":
                break
            else:
                print("Please, write yes or no!")
        self.edit.append(text)

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

    @staticmethod
    def italic(text, piece):
        return text.replace(piece, f"*{piece}*")

    @staticmethod
    def bold(text, piece):
        return text.replace(piece, f"**{piece}**")

    @staticmethod
    def inline_code(text, piece):
        return text.replace(piece, f"`{piece}`")

    def main(self):
        print("File processed successfully!")
        while True:
            if len(self.edit) == 0:
                print("=" * 70)
                formatter = input("Choose a formatter: \n").lower().strip()
            else:
                print("=" * 70 + "\nYour text is:")
                for q in self.edit:
                    print(q)
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
    blacklist = ["~", "#", "%", "&", "*", "{", "}", "\\", ":", "<", ">", "?", "/", "+", "|", "\""]
    print("=" * 70)
    print("Welcome to the Simplified Markdown Editor!")
    while True:
        name_file = input("Enter the name of the future file: \n")
        check_name = 0
        for i in name_file:
            if i in blacklist:
                break
            else:
                check_name += 1
        if check_name == len(name_file):
            break
        else:
            print("Please, don't use symbols in the file name!")
    if len(name_file) == 0:
        name_file = "output.md"
    else:
        name_file += ".md"
    try:
        with open(name_file, "r", encoding='utf-8') as i:
            pass
        while True:
            overwrite = input("Do you want to overwrite an existing file? \n").lower().strip()
            if overwrite == "yes" or overwrite == "no" or overwrite == "y" or overwrite == "n":
                break
            else:
                print("Please, write yes or no.")
    except FileNotFoundError:
        overwrite = "yes"
    x = SimplifiedMarkdownEditor(name_file, overwrite)
    x.main()

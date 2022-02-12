"""
Tables color (different in dark bg)
Font size
Image size
line height less under heading
line height more normal
Inline code, background, border-radius

HTML:
Lines come under h1, h2
strikethrough
"""


class ModifyCSS:
    def __init__(self, css_file: str) -> None:
        self.file = css_file
        self.css = self.read_css()

    def read_css(self) -> list[str]:
        """Read the css file and return it's list."""
        with open(self.file) as file:
            css = file.read().splitlines()
        return css

    def update_css_file(self) -> None:
        """Update the CSS file with modified list."""
        with open(self.file, 'w') as file:
            file.write('\n'.join(self.css))

    def font_size(self) -> None:
        pass

    def _code_style(self) -> None:
        """Change code style in CSS."""
        pre_style = self.css[0][:-1]
        pre_style += "padding: 10px; }"
        self.css[0] = pre_style
        ...

    def _blockquote_style(self) -> None:
        """Add blockquote style in CSS."""
        blockquote_style = "blockquote { border-left: 5px solid grey; padding-left: 10px;}"
        self.css.append(blockquote_style)

    def show_css(self) -> None:
        """Show the css list preview."""
        print(self.css[:2], self.css[-2:], sep="\n")
        # c = "😀"
        # print(c)

    def apply_all_styles(self) -> None:
        """Run all the functions, workes as main function for class."""


"""
Make separate dark background file:
modifies body background, text color, anchor tag color
body { background-color: rgb(46, 46, 46); color: #FFF; }

a {color: lightskyblue;}
"""

if __name__ == "__main__":
    mycss = ModifyCSS("./css_files/one-dark.css")
    # mycss.show_css()
    # mycss.code_padding()
    # mycss.show_css()
    # mycss.block_quote()
    # mycss.show_css()
    # mycss.update_css_file()

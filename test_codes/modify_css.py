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

    def _body_style(self) -> None:
        """Change Body background color, text color, font-family."""

        body_line = 'body { background-color: #FFF; color: #0d1117; font-family: "Segoe UI", sans-serif; }'
        body_ind = self.selector_found("body")

        if body_ind == -1:
            self.css.insert(0, body_line)
            return
        
        if self.css[body_ind] != body_line:
            self.css[body_ind] = body_line

    def _anchor_style(self) -> None:
        """Change link color"""

        anchor_line = "a { color: #58A6FF; }"
        anchor_ind = self.selector_found("a {")

        if anchor_ind == -1:
            self.css.append(anchor_line)
            return
        
        if self.css[anchor_ind] != anchor_line:
            self.css[anchor_ind] = anchor_line
    

    def _font_size(self) -> None:

        font_lines = [
            "* { font-size: 16px; }",   # all
            "h1 { font-size: 28px; }",  # h1
            "h2 { font-size: 26px; }",  # h2
            "h3 { font-size: 24px; }",  # h3
            "h4 { font-size: 22px; }",  # h4
            "h5 { font-size: 20px; }",  # h5
            "h6 { font-size: 18px; }",  # h6
        ]

        for font in font_lines:
            findex = self.selector_found(font.split()[0])
            if findex == -1:
                self.css.append(font)
            elif self.css[findex] != font:
                self.css[findex] = font

    def _code_style(self) -> None:
        """Change code style"""

        codehilite_line = "width: max-content; padding: 5px 50px 5px 10px;  border-radius: 5px; margin: 10px 0; }"
        code_index = self.selector_found(".codehilite {")

        if code_index == -1:
            self.css.append(codehilite_line)
            return

        if codehilite_line not in self.css[code_index]:
            self.css[code_index] = self.css[code_index][:-1] + codehilite_line


    def _blockquote_style(self) -> None:
        """Add blockquote style"""

        blockquote_style = "blockquote { border-left: 5px solid grey; padding-left: 10px; }"
        bq_index = self.selector_found("blockquote")
        if bq_index == -1:
            self.css.append(blockquote_style)
            return
        
        if self.css[bq_index] != blockquote_style:
            self.css[bq_index] = blockquote_style
            

    def selector_found(self, selector: str) -> int:
        """If selector present in css, return it's index."""
        
        for line in self.css:
            if line.startswith(selector):
                return self.css.index(line)
        return -1

    def show_css(self) -> None:
        """Show the css list preview."""
        print(self.css[:2], self.css[-2:], sep="\n")

    def apply_styles(self) -> None:
        """Run all the functions, workes as main function for class."""
        self._body_style()
        self._anchor_style()
        self._code_style()
        self._font_size()
        self._blockquote_style()


"""
Make separate dark background file:
modifies body background, text color, anchor tag color
body { background-color: rgb(46, 46, 46); color: #FFF; }

a {color: lightskyblue;}
"""

if __name__ == "__main__":
    mycss = ModifyCSS("./css_files/one-dark.css")
    mycss.apply_styles()
    mycss.update_css_file()

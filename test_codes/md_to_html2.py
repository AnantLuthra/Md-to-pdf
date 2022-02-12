import markdown
import os


EXTENSIONS = [
    "tables",
    "attr_list",
    "def_list",
    "fenced_code",
    "codehilite",
]

THEMES = [
    "default",
    "emacs",
    "friendly",
    "friendly_grayscale",
    "colorful",
    "autumn",
    "murphy",
    "manni",
    "material",
    "monokai",
    "perldoc",
    "pastie",
    "borland",
    "trac",
    "native",
    "fruity",
    "bw",
    "vim",
    "vs",
    "tango",
    "rrt",
    "xcode",
    "igor",
    "paraiso-light",
    "paraiso-dark",
    "lovelace",
    "algol",
    "algol_nu",
    "arduino",
    "gruvbox-light",
    "dracula",
    "one-dark",
    "lilypond"
]


def covnert_md_to_html(filename, theme="monokai"):
    global EXTENSIONS
    print("Reading markdown")
    with open(filename) as mdfile:
        html = markdown.markdown(
            mdfile.read(),
            extensions=EXTENSIONS
        )

    print("Linking css")
    # linking css file of theme with html
    html = link_css_to_html(html, theme=theme)
    print("Writing to html file")

    """SHOULD UPDATE CSS TOO"""

    with open("./html2.html", "w") as htmlfile:
        htmlfile.write(html)

def link_css_to_html(html, *, theme):
    """Link css file in HTML"""
    css_link = f'<link rel="stylesheet" href="./css_files/{theme}.css">\n'
    return css_link + html


def generate_css(theme):
    """Generate CSS file for code highlighting of provided theme"""
    print(f"Generating theme: {theme}")
    cmd = f"pygmentize -S {theme} -f html -a .codehilite > ./css_files/{theme}.css"
    os.system(cmd)
    print("Theme Generated\n")



if __name__ == "__main__":
    # for theme in THEMES:
    #     generate_css(theme)

    file = "./markdown_sample.md"
    covnert_md_to_html(file)
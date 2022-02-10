from distutils import extension
import markdown

# from markdown.extensions.codehilite import CodeHiliteExtension, CodeHilite

with open("./markdown_sample.md") as mdfile:
    # x = CodeHilite(mdfile)
    # print(x)
    html = markdown.markdown(mdfile.read(), extensions=["tables"])

with open("./html2.html", "w") as htmlfile:
    htmlfile.write(html)
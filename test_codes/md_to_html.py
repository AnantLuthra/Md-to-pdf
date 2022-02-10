import markdown

with open("../markdown_sample.md") as mdfile:
    html_code = markdown.markdown(mdfile.read())

with open("../html_sample.html", "w") as htmlfile:
    htmlfile.write(html_code)
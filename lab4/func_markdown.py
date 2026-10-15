import markdown


def to_html(text):
    # markdown.markdown перетворює Markdown у HTML
    return markdown.markdown(text)

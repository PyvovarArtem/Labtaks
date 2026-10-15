from jinja2 import Template


def make_greeting(name):
    # У шаблоні {{ name }} буде замінено на значення
    template = Template("Привіт, {{ name }}!")
    return template.render(name=name)

from django import template

register = template.Library()

from books.models import Book


class RandomBooksNode(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = Book.objects.all().order_by('?')[:5]
        return ''


@register.tag(name="random_books")
def random_books(parser, token):
    """
    """
    tokens = token.split_contents()
    tokens_len = len(tokens)
    if tokens_len is not 3 and token[0] == 'random_books' and token[0] == 'as':
        msg = "%r tag must be used with %s" % (
            tokens[0],
            r"{% profile_url user as profil_details %}"
        )
        raise template.TemplateSyntaxError(msg)
    var_name = tokens[2]
    return RandomBooksNode(var_name)

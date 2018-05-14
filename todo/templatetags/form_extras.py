from django import template

register = template.Library()

@register.filter(name='addClassOnError')
def addClassOnError(field, css):
    newClass = field.field.widget.attrs.get('class', '')
    if field.errors:
        newClass = (newClass + ' ' + css).strip()
    return field.as_widget(attrs={ 'class': newClass })
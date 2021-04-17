from django import template

register = template.Library()


@register.filter
def addrowtable(open, closed):
    table = ""
    while open != {} or closed != {}:
        if open != {} and closed != {}:
            key, value = closed.popitem()
            table += "<td>{}</td><td>{}</td>".format(value["url"],
                                                     value["comment"])
            key, value = open.popitem()
            table += "<td>{}</td><td>{}</td>".format(value["url"],
                                                     value["comment"])
            table += "</tr>"
            if open != {} or closed != {}:
                table += "<tr><td></td><td></td><td></td><td></td>"
        elif closed != {}:
            key, value = closed.popitem()
            table += "<td>{}</td><td>{}</td><td></td><td></td></tr>".format(
                value["url"],
                value["comment"])
            if closed != {}:
                table += "<tr><td></td><td></td><td></td><td></td>"
        else:
            key, value = open.popitem()
            table += "<td>{}</td><td>{}</td>".format(value["url"],
                                                     value["comment"])
            table += "<td></td><td</td></tr>"
            if open != {}:
                table += "<tr><td></td><td></td><td>" \
                         "</td><td></td><td></td><td></td>"
    return table

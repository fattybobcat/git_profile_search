from django import template

register = template.Library()


@register.filter
def addrowtable(open, closed):
    table = ""
    while open != {} or closed != {}:
        if open != {} and closed != {}:
            key, value = closed.popitem()
            table += ("<td><a href='{0}' target='_blank''>{0}"
                      "</a></td><td>{1}</td>").format(value["url"],
                                                      value["comment"])
            key, value = open.popitem()
            table += ("<td><a href='{0}' target='_blank'>{0}"
                      "</a></td><td>{1}</td>").format(value["url"],
                                                      value["comment"])
            table += "</tr>"
            if open != {} or closed != {}:
                table += "<tr><td></td><td></td><td></td><td></td>"
        elif closed != {}:
            key, value = closed.popitem()
            table += ("<td><a href='{0}'target='_blank'>{0}"
                      "</a></td><td>{1}</td>").format(value["url"],
                                                      value["comment"])
            table += "<td></td><td></td></tr>"
            if closed != {}:
                table += "<tr><td></td><td></td><td></td><td></td>"
        else:
            key, value = open.popitem()
            table += ("<td><a href='{0}'target='_blank'>{0}"
                      "</a></td><td>{1}</td>").format(value["url"],
                                                      value["comment"])
            table += "<td></td><td</td></tr>"
            if open != {}:
                table += "<tr><td></td><td></td><td>" \
                         "</td><td></td><td></td><td></td>"
    return table


@register.filter
def page_re(link):
    if link.split("=")[-1].isdigit():
        return int(link.split("=")[-1])
    else:
        return link.split("=")[-1]


@register.filter
def page_build(page, user_name):
    paginator_html = "<ul class='pagination justify-content-center'>"
    if "prev" in page:
        paginator_html += ('<li class="page-item"><a class="page-link" href="'
                           '?q={}?page={}">Previous</a></li>').format(
            user_name,
            page_re(page["prev"])
        )
    else:
        paginator_html += ('<li class="page-item disabled">'
                           '<a class="page-link" >Previous</a></li>')
    if "first" in page:
        paginator_html += ('<li class="page-item"><a class="page-link" '
                           'href="?q={}?page=1">1</a></li>').format(user_name)
    if "next" in page:
        paginator_html += ('<li class="page-item active"><a class="page-link"'
                           ' href="?q={0}?page={1}">{1}</a></li>').format(
            user_name,
            page_re(page["next"])-1,
        )
        if page_re(page["last"]) != page_re(page["next"]):
            paginator_html += ('<li class="page-item"><a class="page-link" '
                               'href="?q={0}?page={1}">{1}</a></li>').format(
                user_name,
                page_re(page["next"]),
            )
    elif "prev" in page:
        paginator_html += ('<li class="page-item"><a class="page-link" href="'
                           '?q={0}?page={1}">{1}</a></li>').format(
            user_name,
            page_re(page["prev"]),
        )
        paginator_html += ('<li class="page-item active"><a class="page-link"'
                           ' href="?q={0}?page={1}">{1}</a></li>').format(
            user_name,
            page_re(page["prev"])+1,
        )
    if "last" in page:
        paginator_html += ('<li class="page-item"><a class="page-link" '
                           'href="?q={0}?page={1}">{1}</a></li>').format(
            user_name,
            page_re(page["last"]),
        )
    if "next" in page:
        paginator_html += ('<li class="page-item"><a class="page-link" href="?'
                           'q={}?page={}">Next</a></li>').format(
            user_name,
            page_re(page["next"]))
    else:
        paginator_html += ('<li class="page-item disabled"><a class="page-'
                           'link">Next</a></li>')
    paginator_html += "</ul>"
    return paginator_html


@register.filter
def last_pr(page):
    s = ""
    if page.split("=")[-1].isdigit():
        s = (str((int(page.split("=")[-1]) - 1) * 100) + " - " +
             str(int(page.split("=")[-1]) * 100 - 1))
    return s

def row (l):
    buffer = "<tr>"
    for entry in l:
        buffer += "<td>%s</td>" % entry
    buffer += "</tr>"

    return buffer

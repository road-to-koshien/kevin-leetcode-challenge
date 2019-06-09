import webbrowser

origin = 'http://www.abcxyz.com/document'
for i in range(1, 99999):
    weblink = origin + '{0:05}'.format(i) + '.pdf'
    webbrowser.open(weblink)

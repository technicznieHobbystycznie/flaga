import wikipedia as wiki
wiki.set_lang('pl')


def character( name):
    content = wiki.summary(name, sentences=6)
#    img = wiki.page(page[0],images[0])
    return content




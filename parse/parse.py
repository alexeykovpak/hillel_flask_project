def parse(query):

    # Searches name and color values in the input string and returns a dictionary with those values or an empty dictionary

    from re import search

    result = dict()

    name_substring = search(r'name=.+', query)
    if name_substring:
        name = name_substring.group(0)[5:]
        if name[-1] == '&':
            name = name[:-1]
        if 'color=' in name:
            name = search(r'.+(?=&)', name).group(0)
        result['name'] = name

    color_substring = search(r'color=.+$', query)
    if color_substring:
        color = color_substring.group(0)[6:]
        if color[-1] == '&':
            color = color[:-1]
        result['color'] = color

    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

# SSH key added

def parse_cookie(query):
    # Returns a dictionary with keys 'name' and 'age' in the case if the input string contains such values, or an empty dictionary otherwise

    from re import search

    result = dict()
    name_substring = search(r'name=.+?;', query)
    if name_substring:
        name = name_substring.group(0)[5:-1]
        result['name'] = name
    age_substring = search(r'age=\d+;', query)
    if age_substring:
        age = age_substring.group(0)[4:-1]
        result['age'] = age
    return result


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

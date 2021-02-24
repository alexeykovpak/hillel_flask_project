from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/requirements/')
def re_py_pa():
    # Returns the list of intalled Python3 packages from 'requirements.txt' file

    with open('requirements.txt') as file:
        lst = file.read()
        data = [line for line in lst.split('\n')]

    return render_template(
       'template.html',
        **{
            'data': data,
            'query': request.values,
        }
    )


@app.route('/generate-users/')
def gen_usrs():
    # Generates random first names and e-mail addresses in the quantity that equals ti 'user_count' parameter

    from faker import Faker

    fake = Faker()
    data = []
    user_count = int(request.args.get('user_count', '100'))
    names = [fake.unique.first_name() for _ in range(user_count)]
    for _ in range(user_count):
        text = fake.text().split(' ')[0]
        data.append(str(names[_]) + ' ' + str.lower(text) + '@mail.com')

    return render_template(
        'template1.html',
        **{
            'query': request.values,
            'data': data,
            'user_count': user_count,
        }
    )


if __name__ == '__main__':
    app.run()

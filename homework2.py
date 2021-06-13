
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
    # Generates random first names and e-mail addresses in the quantity that equals to 'user_count' parameter


    from faker import Faker

    fake = Faker()
    user_count = int(request.args.get('user_count', '100'))
    data = ['{} {}'.format(fake.unique.first_name(), fake.email()) for _ in range(user_count)]
    # I use Python 3.5 so I cannot use f-strings

    return render_template(
        'template1.html',
        **{
            'query': request.values,
            'data': data,
            'user_count': user_count,
        }
    )


@app.route('/space/')
def astros():
    # Shows the number of astronauts that are currently in space

    import requests

    req = requests.get('http://api.open-notify.org/astros.json')
    if req.status_code == 200:
        number = req.json()['number']
        return render_template(
            'template2.html',
            **{
                'query': request.values,
                'number': number,
            }
        )
    else:
        return render_template(
            'template3.html',
	    **{
		'query': request.values,
	    }
        )


if __name__ == '__main__':
    app.run()


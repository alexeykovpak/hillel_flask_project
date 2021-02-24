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


if __name__ == '__main__':
    app.run()

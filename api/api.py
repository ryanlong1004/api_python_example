# api.py


from flask import render_template  # Remove: import Flask

import connexion


app = connexion.App(__name__, specification_dir="./")

app.add_api("swagger.yml", resolver_error=501)


@app.route("/")
def home():

    return render_template("home.html")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8888, debug=True)

from flask import Flask
import check_Eid

website = Flask(__name__)

@website.route("/")
def home():
    return f"""<h1 style='text-align: center;
    margin: 200px auto;
    font-size: 150px'>{check_Eid.check_Eid()}</h1>"""


# run the app
if __name__ == "__main__":
    website.run(debug=True, port=3000)
    
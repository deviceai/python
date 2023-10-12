from flask import Flask, render_template

app = Flask(__name__)

def factors(num):
    return [x for x in range(1, num+1) if num%x ==0]

@app.route('/')
def home():
  return '<a href="/factors_raw/100"> click here for an example</a>'
@app.route('/factors_raw/<int:n>')
def factors_display_raw_html(n):
    return render_template(
        "factors.html",
        number = n,
        factors = factors(n)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
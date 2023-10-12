from flask import Flask
app = Flask(__name__)

def factors(num):
    return [x for x in range(1, num+1) if num%x ==0]

@app.route('/')
def home():
  return '<a href="/factors_raw/100"> click here for an example</a>'
@app.route('/factors_raw/<int:n>')
def factors_display_raw_html(n):
    factors_list = factors(int(n))
    html = "<h1> The factors of " +str(n)+ " are</h1>" + "\n" + "<ul>"

    for f in factors_list:
        html += "<li>" +str(f)+"</li>" + "\n"
    html += "</ul> </body>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0')
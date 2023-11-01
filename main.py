from flask import Flask, render_template, request
import marketing_assistant_gpt as magpt
import marketing_assistant_lm as malm
import pprint

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')


@app.route("/index.html")
def results():
    return render_template('index.html')

@app.route('/index.html', methods=['POST'])
def run_post():
    query_s = request.form['query_string']
    print(f'query={query_s}')
    gpt_data = magpt.marketing_text(query_s)
    pprint.pprint(gpt_data)
    gpt_blog = gpt_data['blog']
    gpt_yt_script = gpt_data['yt_script']
    gpt_yt_visuals= gpt_data['yt_visuals']

    lm_data = malm.marketing_text(query_s)
    pprint.pprint(lm_data)
    lm_blog = lm_data['blog']
    lm_yt_script = lm_data['yt_script']
    lm_yt_visuals= lm_data['yt_visuals']
    return render_template('index.html',
                           gpt_blog=gpt_blog,
                           gpt_yt_scripts = gpt_yt_script,
                           gpt_yt_visuals = gpt_yt_visuals,
                           lm_blog = lm_blog,
                           lm_yt_scripts = lm_yt_script,
                           lm_yt_visuals = lm_yt_visuals

    )

if __name__ == "__main__":
    app.run(debug=True)
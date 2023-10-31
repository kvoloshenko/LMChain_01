from flask import Flask, render_template, request
import marketing_assistant_01 as ma

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/form01.html")
def form():
    return render_template('form01.html')

@app.route("/form02.html")
def results():
    return render_template('form02.html')

@app.route("/contacts.html")
def contacts():
    developer_name = 'AI Experience Exchange'
    return render_template('contacts.html', name=developer_name, creation_date='https://t.me/AiExp01')

@app.route('/form02.html', methods=['POST'])
def run_post():
    # Как получть данные формы
    query_s = request.form['query_string']
    print(type(query_s),f'query={query_s}')

    # app_data = ma.marketing_text(query_s)
    blog = '''
    You're an amazing director, generate the scene by scene
    Description for the Youtube video based on the following script: [Opening shot: A close-up of a steaming cup of coffee]

Narrator: Всем привет, любители кофе и заботы о планете! У нас есть отличная новость для вас!

[Cut to a shot of a coffee cup made from biodegradable material]

Narrator: Представляем вам инновационную экологически чистую кофейную чашку!

[Cut to a shot of the cup being held]

Narrator: Эта чашка изготовлена из специального биоразлагаемого материала, который не только сохраняет температуру вашего любимого напитка, но и не наносит вреда окружающей среде.

[Cut to a shot of plastic cups and disposable coffee cups being thrown away]

Narrator: Забудьте о пластиковых стаканчиках и одноразовых чашках! Теперь вы можете наслаждаться своим кофе, зная, что вы делаете что-то хорошее для нашей планеты.

[Cut to a shot of the cup being washed]

Narrator: Эта чашка легко моется и многократно используется, что делает ее идеальным выбором для дома, офиса или даже в путешествиях.

[Cut to a shot of someone enjoying a cup of coffee]

Narrator: Подарите себе и своим близким возможность наслаждаться вкусом кофе, не нанося вреда природе.

[Cut to a shot of the cup being ordered online]

Narrator: Закажите свою инновационную экологически чистую кофейную чашку прямо сейчас и станьте частью движения в защиту окружающей среды!

[Closing shot: A close-up of the cup with the text "Для заказа и получения дополнительной информации, пожалуйста, напишите нам в личные сообщения."]

Narrator: Вместе мы можем сделать нашу планету чище и зеленее! Закажите свою чашку уже сегодня!

[End screen with hashtags: #экология #чистаяпланета #кофе #инновации]
    Here is additional blog content if additional context is needed: 🌿🌍 Новинка для настоящих ценителей кофе и заботы о планете! 🌍🌿

🔬 Представляем вам инновационную экологически чистую кофейную чашку! 🔬

🌱 Эта чашка изготовлена из специального биоразлагаемого материала, который не только сохраняет температуру вашего любимого напитка, но и не наносит вреда окружающей среде. 🌱

🌿 Забудьте о пластиковых стаканчиках и одноразовых чашках! Теперь вы можете наслаждаться своим кофе, зная, что вы делаете что-то хорошее для нашей планеты. 🌿

🌍 Эта чашка легко моется и многократно используется, что делает ее идеальным выбором для дома, офиса или даже в путешествиях. 🌍

🌱 Подарите себе и своим близким возможность наслаждаться вкусом кофе, не нанося вреда природе. 🌱

🌿 Закажите свою инновационную экологически чистую кофейную чашку прямо сейчас и станьте частью движения в защиту окружающей среды! 🌿

📲 Для заказа и получения дополнительной информации, пожалуйста, напишите нам в личные сообщения. 📲

#экология #чистаяпланета #кофе #инновации. Add line breaks. 
    Give the result in Russian
    '''
    yt_script = blog
    yt_visuals = blog
    # blog = app_data['blog']
    # yt_script = app_data['yt_script']
    # yt_visuals= app_data['yt_visuals']

    return render_template('form02.html', blog=blog, yt_scripts = yt_script, yt_visuals = yt_visuals)

if __name__ == "__main__":
    app.run(debug=True)
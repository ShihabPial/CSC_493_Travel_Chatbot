from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from logicadapter import MyLogicAdapter
from flask import Flask, render_template, request

app =Flask(__name__)

bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'logicadapter.MyLogicAdapter',
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation'
        ],
    database_uri='sqlite:///database.sqlite3'
)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    'chatterbot.corpus.english'
 )

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()





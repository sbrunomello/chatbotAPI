import os
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# bot = ChatBot("Bot brabo", storage_adapter="chatterbot.storage.SQLStorageAdapter")

# trainer = ChatterBotCorpusTrainer(bot)

# trainer.train('chatterbot.corpus.portuguese')
# trainer.train('chatterbot.corpus.portuguese.greetings')
# trainer.train('chatterbot.corpus.portuguese.conversations')
# trainer = ListTrainer(bot)
# trainer.train("chatterbot.corpus.Portuguese")
# trainer.train("chatterbot.corpus.Portuguese.greetings_pt-BR")
# trainer.train("chatterbot.corpus.Portuguese.conversations_pt-BR")

# Treino baseado no corpus em português
# bot.train("chatterbot.corpus.Portuguese")

@app.route("/")
def home():
    return render_template("home.html")

#@app.route("/get")
#def get_bot_response():
#    userText = request.args.get('msg')
#    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)

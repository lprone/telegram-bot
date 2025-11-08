from telegram import Update
from telegram.ext import ContextTypes

from src.common.env import groq_key, llm_model
from src.llm.groq_wrapper import GroqLLM

groq = GroqLLM(groq_key, llm_model)


async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await update.message.reply_text(groq.chat(update.message.text))

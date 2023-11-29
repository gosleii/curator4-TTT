import telebot
bot = telebot.TeleBot("6642328360:AAHJ0TQrmIlpL-ARub584JyTZV4v2Koyfco")

@bot.message_handler(commands=["peremen"])
def main(message):
    bot.send_message(message.chat.id, "Переменная - это именованная область памяти компьютера для хранения данных, изменяющихся при исполнении программы.")

@bot.message_handler(commands=["bait"])
def main(message):
    bot.send_message(message.chat.id, "Байт – 1. восьмиразрядное двоичное число; 2. элемент памяти, позволяющий хранить восьмиразрядное двоичное число.")

@bot.message_handler(commands=["sintaks"])
def main(message):
    bot.send_message(message.chat.id, "Синтаксис – совокупность правил, с помощью которых строятся правильные предложения.")

@bot.message_handler(commands=["registr"])
def main(message):
    bot.send_message(message.chat.id, "Регистры – внутренняя сверхбыстрая память процессора.")


@bot.message_handler(commands=["protokol"])
def main(message):
    bot.send_message(message.chat.id, "Протокол – совокупность технических условий, которые должны быть обеспечены разработчиками для успешного согласования работы устройств или программ.")

@bot.message_handler(commands=["kodir"])
def main(message):
    bot.send_message(message.chat.id, "Кодирование – представление данных одного типа через данные другого типа.")

@bot.message_handler(commands=["info"])
def main(message):
    bot.send_message(message.chat.id, "*Данный бот поможет вам в легком запоминание и усвоение терминов по информатике. Жлеаю удачи, у вас всё получится!!!*", parse_mode="Markdown")

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "Приятный [бонус](https://sun9-49.userapi.com/impg/eLRwXWSJne4tygIPnLRAnt9rCKNeL86D8qY95g/KOWl2nx6dWo.jpg?size=707x634&quality=95&sign=f2346ead8639a096781d4ec151c064d8&c_uniq_tag=oAwlpxUFZfb_g8GqFEa_IiV7HTYX8l5oMQVhpJvxk4Q&type=album)", parse_mode="Markdown")

bot.infinity_polling()
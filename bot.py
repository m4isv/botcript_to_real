import requests
import telebot
import lib
import h

bot = telebot.TeleBot("5019169340:AAE2LcRyAH5J_57EWDJQEokRRtcantzAIIo")


@bot.message_handler(commands=['cripto', 'help'])
def send_welcome(message):
	# Exemplo de uso
    bitcoin_amount = 0.00028360 #sua quantidade de bitcoin aqui
    real_amount = lib.bitcoin_to_real(bitcoin_amount)
     
    # Exempplo de uso 
    dogecoin_amount = 52.00998989 #sua quantidade dogecoin aqui
    quantidadedoge = lib.dogecoin_to_real(dogecoin_amount)

    data_atual = h.DATA_HORA() # pegar  data e hora atual
    
    if real_amount is not None:
        bot.reply_to(message, f"agora: {data_atual}\n\nSeus BTC: [ {bitcoin_amount} ]  VALE  {real_amount:.2f} R$.\n\nSeus DOGE [ 52.00998989 ] VALE {quantidadedoge:.2f} R$")

    else:
       bot.reply_to(message, "Erro na consulta.")



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Digite um comando valido")

# bot no oop infinito
bot.infinity_polling()


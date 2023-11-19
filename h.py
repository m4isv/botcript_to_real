#!/usr/bin/env python
# -*- coding: utf-8

from datetime import datetime
from pytz import timezone

def DATA_HORA():
   data_e_hora_atuais = datetime.now()
   fuso_horario = timezone("America/Sao_Paulo")
   data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
   data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")
   return data_e_hora_sao_paulo_em_texto

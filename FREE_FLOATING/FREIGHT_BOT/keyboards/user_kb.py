from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# start buttons
b1 = KeyboardButton('/Voyage_calculator')
b2 = KeyboardButton('/vessels_list')
b3 = KeyboardButton('/EUR_USD_exchange')
b4 = KeyboardButton('/Intake_calculator')

kb_user = ReplyKeyboardMarkup(resize_keyboard=True)
kb_user.add(b1).add(b2).add(b3).add(b4)

# vessels buttons
v1 = KeyboardButton('nordborg')
v2 = KeyboardButton('ostborg')
v3 = KeyboardButton('sydborg')
v4 = KeyboardButton('westborg')
v5 = KeyboardButton('bergfjord')
v6 = KeyboardButton('tucana')
v7 = KeyboardButton('aerandir')
v8 = KeyboardButton('avalon')
v9 = KeyboardButton('ankie')
v10 = KeyboardButton('emma')
v11 = KeyboardButton('jolyn')
v12 = KeyboardButton('leonie')
v13 = KeyboardButton('heyn')
v14 = KeyboardButton('mila')
v15 = KeyboardButton('ruyter')
v16 = KeyboardButton('sprinter')
v17 = KeyboardButton('speyk')
v18 = KeyboardButton('andrea')
v19 = KeyboardButton('carolina')
v20 = KeyboardButton('noorderliht')
v21 = KeyboardButton('egon_w')
v22 = KeyboardButton('marietje_hester')
v23 = KeyboardButton('merel_v')
v24 = KeyboardButton('susanne')
v25 = KeyboardButton('panta_rhei')
v26 = KeyboardButton('kelt')
v27 = KeyboardButton('cristina')
v28 = KeyboardButton('adamas')
v29 = KeyboardButton('alana_evita')
v30 = KeyboardButton('cito')
v31 = KeyboardButton('helenic')
v32 = KeyboardButton('hekla')
v33 = KeyboardButton('hestia')
v34 = KeyboardButton('hydra')
v35 = KeyboardButton('jade')
v36 = KeyboardButton('priscilla')
v37 = KeyboardButton('zeeland')

kb_vessels = ReplyKeyboardMarkup(resize_keyboard=True)
kb_vessels.add(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10,
               v11, v12, v13, v14, v15, v16, v17, v18,
               v19, v20, v21, v22, v23, v24, v25, v26,
               v27, v28, v29, v30, v31, v32, v33, v34,
               v35, v36, v37)


# load ports buttons
lp1 = KeyboardButton('Kaliningrad')
lp2 = KeyboardButton('Klaipeda')

kb_load_ports = ReplyKeyboardMarkup(resize_keyboard=True)
kb_load_ports.add(lp1).add(lp2)


# dis ports buttons
dp1 = KeyboardButton('St. Malo')
dp2 = KeyboardButton('Le Legue')
dp3 = KeyboardButton('Rotterdam')
dp4 = KeyboardButton('Brake')
dp5 = KeyboardButton('Bremen')
dp6 = KeyboardButton('WC UK')
dp7 = KeyboardButton('EC Ireland')
dp8 = KeyboardButton('Montrose')
dp9 = KeyboardButton('New Holland')
dp10 = KeyboardButton('Plymouth')
dp11 = KeyboardButton('Teignmouth')
dp12 = KeyboardButton('Brest')
dp13 = KeyboardButton('Brugge')

kb_dis_ports = ReplyKeyboardMarkup(resize_keyboard=True)
kb_dis_ports.add(dp1, dp2, dp3, dp4, dp5, dp6, dp7, dp8, dp9, dp10, dp11, dp12, dp13)


# dis ports buttons
m1 = KeyboardButton('January')
m2 = KeyboardButton('February')
m3 = KeyboardButton('March')
m4 = KeyboardButton('April')
m5 = KeyboardButton('May')
m6 = KeyboardButton('June')
m7 = KeyboardButton('July')
m8 = KeyboardButton('August')
m9 = KeyboardButton('September')
m10 = KeyboardButton('November')
m11 = KeyboardButton('October')
m12 = KeyboardButton('December')

kb_months = ReplyKeyboardMarkup(resize_keyboard=True)
kb_months.add(m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


# start buttons
b1 = KeyboardButton('/Voyage_calculator')
b2 = KeyboardButton('/vessels_list')
b3 = KeyboardButton('EUR-USD rate of exchange')
b4 = KeyboardButton('Intake calculator')

kb_user = ReplyKeyboardMarkup()
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

kb_vessels = ReplyKeyboardMarkup()
kb_vessels.add(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10,
               v11, v12, v13, v14, v15, v16, v17, v18,
               v19, v20, v21, v22, v23, v24, v25, v26,
               v27, v28, v29, v30, v31, v32, v33, v34,
               v35, v36, v37)

# load ports buttons
lp1 = KeyboardButton('Kaliningrad')
lp2 = KeyboardButton('Klaipeda')

kb_load_ports = ReplyKeyboardMarkup()
kb_user.add(lp1).add(lp2)




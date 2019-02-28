slovar = {
'Привет' : 'Здрасьте',
'Как дела' : 'ЗБС',
'Что делаешь' : "Танцую с бубном",
"Зачем" : "чтобы погода наладилась"

}

a = input ()
while True:
    for score in slovar:
        if a == (score):
            print (slovar [score])
            break
    if a != (score):
        print ('Остановись')
        break




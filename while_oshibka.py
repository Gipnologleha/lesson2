slovar = {
'Привет' : 'Здрасьте',
'Как дела' : 'ЗБС',
'Что делаешь' : "Танцую с бубном",
"Зачем" : "чтобы погода наладилась"

}


try:
    a = input ()
    while True:
            if a in slovar:
                print (slovar [a])
                break
            elif a not in slovar:
                print ('СТОП')
except KeyboardInterrupt:
    print("надо пересмотреть ввод")
        
     


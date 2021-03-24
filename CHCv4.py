import os
def build(x):
    quest=int(input('привязать css расширение?\n1 да\n2 нет'))
    if(quest==2):
        rt=open(str(x)+'.html','w')
        rt.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8"/>\n<title>'+str(x)+'</title>\n<body>')
        rt.close()
    elif(quest==1):
        rt=open(str(x)+'.html','w')
        qaz=input('вводи название ячейки')
        fhk=open('C:/ячейки памяти/'+qaz+'.txt','r')
        ddv=(fhk.read())
        rt.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8"/>\n<link rel="stylesheet" type="'+fhk+'"/>\n<title>'+str(x)+'</title>\n<body>')
        rt.close()
def append(x):
    rty=open(str(x),'a')
    while(1==1):
        cv=input('подкоманда:')
        def img():
            w=input('1 в ручную\n2 с помощью ячеек памяти')
            if(w==1):
                x=input('вводи источник')
                rty.write('<img scr="'+str(x)+'"/><br/>\n')
            else:
                qaz=input('вводи название ячейки')
                fhk=open('C:/ячейки памяти/'+qaz+'.txt','r')
                x=(fhk.read())
                rty.write('<img scr="'+str(x)+'"/><br/>\n')
                
        def img2():
            w=input('1 в ручную\n2 с помощью ячеек памяти')
            if(w==1):
                x=input('вводи источник')
                y=int(input('вводи ширину'))
                rty.write('<img scr="'+str(x)+'" width="'+str(y)+'px"/><br/>\n')
            else:
                qaz=input('вводи название ячейки')
                y=int(input('вводи ширину'))
                fhk=open('C:/ячейки памяти/'+qaz+'.txt','r')
                x=(fhk.read())
                rty.write('<img scr="'+str(x)+'" width="'+str(y)+'px"/><br/>\n')
                
        def img3():
            w=input('1 в ручную\n2 с помощью ячеек памяти')
            if(w==1):
                x=input('вводи источник')
                y=int(input('вводи ширину'))
                q=int(input('вводи длину'))
                rty.write('<img scr="'+str(x)+'" width="'+str(y)+'px" height="'+str(q)+'"/><br/>\n')
            else:
                qaz=input('вводи название ячейки')
                y=int(input('вводи ширину'))
                q=int(input('вводи длину'))
                fhk=open('C:/ячейки памяти/'+qaz+'.txt','r')
                x=(fhk.read())
                rty.write('<img scr="'+str(x)+'" width="'+str(y)+'px" height="'+str(q)+'"/><br/>\n')
                        
        def audio():
            qaz=input('вводи название ячейки')
            j=input('вводи режим')
            fhk=open('C:/ячейки памяти/'+qaz+'.txt','r')
            x=(fhk.read())
            if(j=='a'):
                rty.write('<audio src="'+str(x)+'" controls autoplay></audio><br/>\n')
            elif(j=='l'):
                rty.write('<audio src="'+str(x)+'" controls loop></audio><br/>\n')
            elif(j=='a,l')or(j=='a, l'):
                rty.write('<audio src="'+str(x)+'" controls loop autoplay></audio><br/>\n')
            elif(j=='0'):
                rty.write('<audio src="'+str(x)+'" controls></audio><br/>\n')
            
        def div():
            x=input('введи текст')
            rty.write('<div>'+x+'</div><br/>\n')
        def video():
            qaz=input('вводи название ячейки')
            fhk=open('C:/ячейки памяти/'+qaz+'.txt','r')
            x=(fhk.read())
            rty.write('<video src="'+x+'" controls></video><br/>\n')
            
        def video2():
            qaz=input('вводи название ячейки')
            fhk=open('C:/ячейки памяти/'+qaz+'.txt','r')
            x=(fhk.read())
            y=input('вводи ширину')
            rty.write('<video src="'+str(x)+'" width="'+str(y)+'" controls></video><br/>\n')
            
        def video3():
            qaz=input('вводи название ячейки')
            fhk=open('C:/ячейки памяти/'+qaz+'.txt','r')
            x=(fhk.read())
            y=input('вводи ширину')
            q=int(input('вводи длину'))
            rty.write('<video src="'+str(x)+'" width="'+str(y)+'"height="'+str(q)+'" controls></video><br/>\n')
            
        def gline():
            rty.write('<hr/>')
        def broke():
            rty.write('<br/>')
        def end():
            rty.write('\n</body>\n</html>')
            rty.close()
        def a():
            x=input('название ссылки')
            qaz=input('вводи название ячейки,которая определит содержание ссылки')
            fhk=open('C:/ячейки памяти/'+qaz+'.txt','r')
            y=(fhk.read())
            rty.write('<a href="'+y+'">'+x+'</a>')
            
        def button():
            x=input('название кнопки')
            y=input('атрибут кнопки')
            if(y=='a'):
                qaz=input('вводи название ячейки,которая определит содержание ссылки')
                fhk=open('C:/ячейки памяти/'+qaz+'.txt','r')
                q=(fhk.read())
                rty.write('<a href="'+q+'"><button>'+x+'</button></a>')
            elif(y=='ad'):
                qaz=input('вводи название ячейки,которая определит содержание ссылки или путь к файлу')
                fhk=open('C:/ячейки памяти/'+qaz+'.txt','r')
                q=(fhk.read())
                rty.write('<a href="'+q+'" download><button>'+x+'</button></a>')
            elif(y=='0'):
                rty.write('<button>'+x+'</button>')
        def start():
            os.startfile(d)
        def inpat():
            rty.write('<input>'+x+'</input>')
        def textarea():
            rty.write('<textarea width="'+x+'" height="'+y+'"></textarea>')
        if(cv=='img'):
            img()
        elif(cv=='img2'):
            img2()
        elif(cv=='img3'):
            img3()
        elif(cv=='звук')or(cv=='audio'):
            audio()
        elif(cv=='текст')or(cv=='div'):
            div()
        elif(cv=='видео')or(cv=='video'):
            video()
        elif(cv=='видео2')or(cv=='video2'):
            video2()
        elif(cv=='глиния')or(cv=='gline'):
            gline()
        elif(cv=='broke'):
            broke()
        elif(cv=='конец')or(cv=='end'):
            end()
            break
        elif(cv=='видео3')or(cv=='video3'):
            video3()
        elif(cv=='a')or(cv=='ссылка'):
            a()
        elif(cv=='кнопка')or(cv=='button'):
            button()
        elif(cv=='start')or(cv=='запуск'):
            start()
        elif(cv=='ввод'):
            inpat()
        elif(cv=='поле ввода'):
            textarea()
def yap():
    g=os.path.exists(r'C:/ячейки памяти')
    if(g==True):
        pass
    else:
        os.mkdir(r'C:/ячейки памяти')
    cvb=input('укажи название ячейки памяти')
    uhd=os.path.exists('C:/ячейки памяти/'+cvb+'.txt')
    if(uhd==False):
        try:
            qwertyuiop=open('C:/ячейки памяти/'+cvb+'.txt','w')
        except:
            print('не удалось')
    else:
        print('такая ячейка уже существует')        
while(1==1):
    cvd=input('команда?')
    if(cvd=='создать'):
        x=input('путь к созданию файла')
        build(x)
    elif(cvd=='редактировать'):
        d=input('путь к файлу')
        append(d)
    elif(cvd=='yap')or(cvd=='ячейка памяти'):
        yap()
    else:
        break

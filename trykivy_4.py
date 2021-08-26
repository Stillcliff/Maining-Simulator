# обработка события "нажали на кнопку"

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from random import randint
#from kivy.uix.screenmanager import ScreenManager, Screen
#al = AnchorLayout()
class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        al = AnchorLayout()
        bl = BoxLayout(orientation = "vertical", size_hint=[.93, .28])
        
        s = Button(text = "Начать игру",
                    font_size = 12,
                    background_color = [0,0,.777,1],
                    background_normal = "")

        s.on_press = self.next

        bl.add_widget(s)

        s1 = Button(text = "Статистика",
                    font_size = 12,
                    background_color = [0,0,.777,1],
                    background_normal = "")

        s1.on_press = self.next_stat

        bl.add_widget(s1)

        s2 = Button(text = "Выход",
                    font_size = 12,
                    background_color = [.777,0,0,1],
                    background_normal = "")

        s2.on_press = exit

        bl.add_widget(s2)



        
        #bl.add_widget( Button(text = "Статистика",
                        #font_size = 12,
                        #on_press = self.next,
                        #background_color = [1,0,0,1],
                        #background_normal = "") )

        #bl.add_widget( Button(text = "Выход",
                        #font_size = 12,
                        #on_press = self.next,
                        #background_color = [1,0,0,1],
                        #background_normal = "") )
        

        
        #btn = Button(text="Переключиться на другой экран")
        
        al.add_widget(bl)
        self.add_widget(al)

    def next(self):
        self.manager.transition.direction = 'down' 
        self.manager.current = 'game'

    def next_stat(self):
        self.manager.transition.direction = 'up' 
        self.manager.current = 'second'
    
    #def btn_press(self, instance):
        #print("Тест. Кнопка нажата")
        #instance.text = "Тест пройден"
        #instance.background_color = [.29,.88,.86,1]

Clicks = 0
Maining = 0
PerClicks = 1
class SecondScr(Screen):
    def __init__(self, name='second'):
        global Clicks, Maining
        super().__init__(name=name)

        al = AnchorLayout()
        bl = BoxLayout(orientation = "vertical", size_hint=[.93, .28])
        
        self.txt1 = Label(text = "Всего кликов:" + str(Clicks))

        self.txt1.color = [0,0,1,1]
        
            
        bl.add_widget(self.txt1)

        self.txt2 = Label(text = "Заработано за всё время:" + str(Maining))

        self.txt2.color = [0,.777,0,1]
        
            
        bl.add_widget(self.txt2)

        self.total_buy = Label(text = "Куплено улучшений" + str(PerClicks -1))

        bl.add_widget(self.total_buy)
        s_1 = Button(text = "Назад",
                    font_size = 12,
                    background_color = [.777,0,0,1],
                    background_normal = "")

        s_1.on_press = self.next

        bl.add_widget(s_1)
        
        #btn1.on_press = self.next
        #self.add_widget(btn1)
        al.add_widget(bl)
        self.add_widget(al)
        
    def next(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'first'
 


class GameScr(Screen):
    def __init__(self, name='game'):
        global Maining, Clicks
        super().__init__(name=name)

        al = AnchorLayout()
        bl = BoxLayout(orientation = "vertical", size_hint=[.93, .28])
        
        self.txt1 = Label(text = "Заработано:" + str(Maining))
        
            
        bl.add_widget(self.txt1)

        
        s__1 = Button(text = "Майнить",
                    font_size = 12,
                    background_color = [0,.777,0,1],
                    background_normal = "")

        s__1.on_press = self.r

        bl.add_widget(s__1)



        s__2 = Button(text = "Вернуться в главное меню",
                    font_size = 12,
                    background_color = [.777,0,0,1],
                    background_normal = "")

        s__2.on_press = self.next
        buy_button = Button(text = "Купить ускоритель",
                    font_size = 15,
                    background_color = [.941,0.239,0.8,1],
                    background_normal = "")
        buy_button.on_press = self.buy
        bl.add_widget(buy_button)
        bl.add_widget(s__2)
        

        #btn1.on_press = self.next
        #self.add_widget(btn1)
        al.add_widget(bl)
        self.add_widget(al)

    def r(self):
        global Maining, Clicks , PerClicks
        Maining += PerClicks 
        Clicks += 1
        self.txt1.text =  "Заработано:" + str(Maining)
        app.scr2.txt1.text =  "Всего кликов:" + str(Clicks)
        app.scr2.txt2.text =  "Заработано за всё время:" + str(Maining)

    def next(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'first'
    
    def buy(self):
        global PerClicks , Maining
        if Maining >= 15 :
            PerClicks += 1
            Maining -= 15
            app.scr2.total_buy.text =  "Куплено улучшений:" + str(PerClicks)
            self.txt1.text =  "Cписано 15, Осталось:" + str(Maining)
        else :
            self.txt1.text =  "Cначала накопи 15:"
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        self.scr2 = SecondScr()
        sm.add_widget(self.scr2)
        sm.add_widget(GameScr())


        #al = AnchorLayout()
        #bl = BoxLayout(orientation = "vertical", size_hint=[.93, .28])
    
        #bl.add_widget( Button(text = "Тест",
                        #font_size = 12,
                        #on_press = self.btn_press,
                        #background_color = [1,0,0,1],
                        #background_normal = "") )
        
        #bl.add_widget( Button(text = "Тест1",
                        #font_size = 12,
                        #on_press = self.btn_press,
                        #background_color = [1,0,0,1],
                        #background_normal = "") )

        #bl.add_widget( Button(text = "Тест2",
                        #font_size = 12,
                        #on_press = self.btn_press,
                        #background_color = [1,0,0,1],
                        #background_normal = "") )
        

        #al.add_widget(bl)
        
        return sm

    #def btn_press(self, instance):
        #print("Тест. Кнопка нажата")
        #instance.text = "Тест пройден"
        #instance.background_color = [.29,.88,.86,1]



        

        

app = MyApp()
app.run() # программа отслеживает нажатие на кнопку и печатает соотв. текст.
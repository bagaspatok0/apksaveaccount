from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineListItem

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

import sqlite3, webbrowser, os

# Window.size = 360, 600

class UI(ScreenManager):
    pass

class PatokAccount(MDApp):
    def build(self, **kwargs):
        super().__init__(**kwargs)
        
        Builder.load_file('app.kv')
        
        return UI()

    def help_user(self):
        self.btn = MDFlatButton (
            text='Close',
            on_press=self.closebtn
        )
        
        self.dialog = MDDialog (
            title='Helpme',
            text='This is an application for storing account  data',
            buttons = [self.btn]
        )
        
        self.dialog.open()
    def closebtn(self, obj):
        self.dialog.dismiss()
    
    def submit(self):
        con = sqlite3.connect('databaseaccount.db')
        cur = con.cursor()
        
        if self.root.ids.user_input.text != '' and self.root.ids.email_input.text != '' and self.root.ids.password_input.text != '':
            
            cur.execute('create table if not exists data (user, email, password) ')
            cur.execute('insert into data values (?, ?, ?) ', (self.root.ids.user_input.text, self.root.ids.email_input.text, self.root.ids.password_input.text))

            self.root.ids.texttitle.text = f'{self.root.ids.user_input.text} added'
        
        else:
            self.root.ids.texttitle.text = 'PATOK ACCOUNT'
        
        con.commit()
        con.close()
        
    def export_database(self):
        
        try:
            con = sqlite3.connect('databaseaccount.db')
            cur = con.cursor()
            
            cur.execute('select * from data')
            records = cur.fetchall()
            
            word = ''
            for record in records:
                word = f'{word}\n{record}'
                self.root.ids.listdatabase.text = f'{word}'
        except:
            self.root.ids.listdatabase.text = 'DATABASE EMPTY'
        
        con.commit()
        con.close()
        
            
    # FOLLOW MY SOCIAL MEDIA OK --
    
    def instagram(instance):
        webbrowser.open('https://instagram.com/bagas_patok')
    def facebook(instance):
        webbrowser.open('https://www.facebook.com/bagas0876')
    def twitter(instance):
        webbrowser.open('https://twitter.com/CssBagas')
    def github(instance):
        webbrowser.open('https://github.com/bagaspatok0/')
    def mywebsite(instance):
        webbrowser.open('https://patok.vercel.app')
    
    def deletedatabase(self):
        os.remove('databaseaccount.db')

if __name__ == '__main__':
    PatokAccount().run()

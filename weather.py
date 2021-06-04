from tkinter import *
import requests
import time

#weather_retrieval
def weatherdata(w):
    city=textfield.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=79bcd6daed46efe35e88298e48c8458f"
    json1 = requests.get(api).json()
    temp1=int(json1['main']['temp_min'] - 273.15)
    desc1=json1['weather'][0]['description']
    min_temp1 = int(json1['main']['temp_min'] - 273.15)
    max_temp1 = int(json1['main']['temp_max'] - 273.15)
    pressure1 = json1['main']['pressure']
    humidity1 = json1['main']['humidity']
    wind1 = json1['wind']['speed']


    info1 = "Today:"+'\n'+desc1.upper()+'\n'+'TEMP:'+str(temp1)+"'C"+'\n'+'MAX_TEMP:'+str(max_temp1)+'\n'+"MINTEMP:"+str(min_temp1)+'\n'+'PRESSURE:'+str(pressure1)+'\n'+'HUMIDITY:'+str(humidity1)+'\n'+"WIND:"+str(wind1)
    buttonframe=Frame(window)
    buttonframe.pack(side=TOP)
    btn1=Button(buttonframe,text=str(info1),font=font2,width=30,height=20,relief='ridge',activebackground='yellow')
    btn1.grid(row=0,column=0)



font=('Arial',20)
font2=('Arial',10)
#window
window=Tk()
window.title("My Weather App")
window.geometry('500x500')

#heading
heading=Label(window,text="SIMPLE-WEATHER-APP",font=font)
heading.pack(side=TOP)

#textfield
textfield=Entry(window,font=font)
textfield.pack(side=TOP,pady=20)
textfield.bind('<Return>', weatherdata)


window.mainloop()
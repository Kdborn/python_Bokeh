from bokeh.plotting import figure
from bokeh.io import output_file,show
from openpyxl import load_workbook
import datetime
import pandas

date_list=[]
temperature_list=[]
pressure_list=[]

#read wherater data
wb = load_workbook(filename="verlegenhuken.xlsx", read_only=True)
ws = wb['Ark1']
df = pandas.DataFrame(ws.values)

for Year,Month,Day,Hour, Temperature, Pressure in zip(df[0][1:],df[1][1:],df[2][1:],df[3][1:],df[4][1:],df[5][1:]):
    date_list.append(datetime.datetime(int(Year),int(Month),int(Day),hour=int(Hour)))
    temperature_list.append(Temperature/10.0)
    pressure_list.append(Pressure/10.0)


#plot Temperature / Pressure Plot
def show_wheater_temperature_pressure():
    f = figure(tools='pan')
    f.title.text = "Temperature and Air Pressure"
    f.title.text_color="Gray"
    #f.title.text_font="times"
    f.title.text_font_style="bold"
    f.xaxis.minor_tick_line_color=None
    f.yaxis.minor_tick_line_color=None
    f.xaxis.axis_label="Temperature (°C)"
    f.yaxis.axis_label="Pressure (hPa)"
    f.axis.axis_label_text_font_style ="bold italic"
    output_file("weather_data.html")
    f.circle(temperature_list,pressure_list,size=1,color='blue')
    show(f)
    return

def show_weather_temperature_time():

    f = figure(x_axis_type = "datetime")
    f.title.text = "Temperature over Time"
    f.title.text_color = "Gray"
    # f.title.text_font="times"
    f.title.text_font_style = "bold"
    f.xaxis.minor_tick_line_color = None
    f.yaxis.minor_tick_line_color = None
    f.yaxis.axis_label = "Temperature (°C)"
    f.xaxis.axis_label = "Time"
    f.axis.axis_label_text_font_style = "bold italic"
    output_file("weather_time.html")
    f.circle(date_list, pressure_list, size=1,color='red')
    show(f)

show_weather_temperature_time()
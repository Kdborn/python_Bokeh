from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

#read bachelors.csv
df=pandas.read_csv("bachelors.csv",delimiter=',')
year=df["Year"]
line_1=df["Engineering"]

f = figure(width=400,height=400,logo=None,tools='pan')

f.title.text="Bachelor precent Women Engineering"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Year"
f.yaxis.axis_label="Percent %"

#output File
output_file("bachelors.html")

f.line(x=year,y=line_1)

show(f)

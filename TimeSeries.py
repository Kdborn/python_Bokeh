from bokeh.plotting import figure, output_file,show
import pandas

df = pandas.read_csv("adbe.csv",delimiter=",",parse_dates=["Date"])

f = figure(title="Timeseries",x_axis_type='datetime',sizing_mode='stretch_both')
output_file("timeseries.html")

f.line(df["Date"],df["Close"])

show(f)

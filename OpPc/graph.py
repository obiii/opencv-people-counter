# --- matplotlib ---
import matplotlib
matplotlib.use('TkAgg') # choose backend

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.pyplot import Figure

# --- other ---
import Tkinter as tk
import pandas as pd

# --- GUI ---

root = tk.Tk()

# top frame for canvas and toolbar - which need `pack()` layout manager
top = tk.Frame(root)
top.pack()

# bottom frame for other widgets - which may use other layout manager
bottom = tk.Frame(root)
bottom.pack()

# --- canvas and toolbar in top ---

# create figure
fig = matplotlib.pyplot.Figure()

# create matplotlib canvas using `fig` and assign to widget `top`
canvas = FigureCanvasTkAgg(fig, top)

# get canvas as tkinter widget and put in widget `top`
canvas.get_tk_widget().pack()

# create toolbar
toolbar = NavigationToolbar2TkAgg(canvas, top)
toolbar.update()
canvas._tkcanvas.pack()

# --- plot ---

data = {
    'Gender':['F', 'M', 'F','M'],
    'Sales': [1, 2, 3, 4],
}

df = pd.DataFrame(data)

x = 'Gender'
y = 'Sales'

new_df = df[[x, y]].groupby(x).sum()

# create first place for plot
ax = fig.add_subplot(111)

# draw on this plot
new_df.plot(kind='bar', legend=False, ax=ax)


# --- other widgets in bottom ---

b = tk.Button(bottom, text='Exit', command=root.destroy)
b.pack()

# --- start ----

root.mainloop()

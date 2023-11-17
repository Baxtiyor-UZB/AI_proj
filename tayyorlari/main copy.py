from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import numpy as np

taskilotlar=("O'zbekiston Respublikasi Fanlar akademiyasi",
             "O'zbekiston milliy universiteti",
             "Samarqand Davlat Universiteti",
             "Toshkent Davlat Iqtisodiyot universiteti",
             "Toshkent axborot texnologiyalari universiteti",
             "Toshkent irrigatsiya va qishloq xo'jaligini mexanizatsiyalash muhandislari instituti",
             "Islom Karimov nomidagi Toshkent Davlat texnika universiteti",
             "Buxoro Davlat Universiteti",
             "O'zbekiston Davlat Jahon tillari universiteti",
             "Toshkent temir yo'l transporti muhandislari instituti")
data=[[6,11,9,16,34,26,35],
        [7,7,22,33,61,65,70],
        [2,4,9,26,32,33,37],
        [1,3,2,7,23,45,58],
        [10,9,96,106,166,98,71],
        [1,1,15,56,64,30,78],
        [1,2,28,74,91,41,65],
        [1,4,24,48,24,47,67],
        [2,1,6,17,34,34,17],
        [5,10,35,27,54,34,23]]

palette = list(reversed(sns.color_palette("Spectral", 10).as_hex()))
labels = taskilotlar

fig = plt.figure(figsize=(7,5))
axes = fig.add_subplot(1,1,1)
axes.set_xlim(0, 12000)

def animate(i):
    y1=((data[0][i]))
    y2=((data[1][i]))
    y3=((data[2][i]))
    y4=((data[3][i]))
    y5=((data[4][i]))
    y6=((data[5][i]))
    y7=((data[6][i]))
    y8=((data[7][i]))
    y9=((data[8][i]))
    y10=((data[9][i]))

    plt.barh(range(9), sorted([y1,y2,y3,y4,y5,y6,y7,y8,y9]), color=palette)
    
    tickdic = {"O'zbekiston Respublikasi Fanlar akademiyasi":y1,
             "O'zbekiston milliy universiteti":y2,
             "Samarqand Davlat Universiteti":y3,
             "Toshkent Davlat Iqtisodiyot universiteti":y4,
             "Toshkent axborot texnologiyalari universiteti":y5,
             "Toshkent irrigatsiya va qishloq xo'jaligini mexanizatsiyalash muhandislari instituti":y6,
             "Islom Karimov nomidagi Toshkent Davlat texnika universiteti":y7,
             "Buxoro Davlat Universiteti":y8,
             "O'zbekiston Davlat Jahon tillari universiteti":y9,
             "Toshkent temir yo'l transporti muhandislari instituti":y10}

    sorted_tickdic = sorted(tickdic.items(), key=lambda x: x[0])

    tcks = [i[0] for i in sorted_tickdic]
    
    plt.title("CO2 Emissions, Year: {} ".format(i+1850), color=("blue"))
    plt.yticks(np.arange(10), tcks)
ani = FuncAnimation(fig, animate, interval=1)
import plotly.graph_objects as go

taskilotlar=["O'zbekiston Respublikasi Fanlar akademiyasi",
             "O'zbekiston milliy universiteti",
             "Samarqand Davlat Universiteti",
             "Toshkent Davlat Iqtisodiyot universiteti",
             "Toshkent axborot texnologiyalari universiteti",
             "Toshkent irrigatsiya va qishloq xo'jaligini mexanizatsiyalash muhandislari instituti",
             "Islom Karimov nomidagi Toshkent Davlat texnika universiteti"
             "Buxoro Davlat Universiteti",
             "O'zbekiston Davlat Jahon tillari universiteti",
             "Toshkent temir yo'l transporti muhandislari instituti"]
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


fig = go.Figure(go.Bar(
            x=data,
            y=taskilotlar,
            orientation='h'))

fig.show()
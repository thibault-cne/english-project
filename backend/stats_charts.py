import matplotlib.pyplot as plt


def stat_chart():
    for i in range (101):
        data = [i, 100-i]
        colors = ["#696969", "#3AA9FF"]
        plt.pie(data, colors=colors, startangle=90)
        circle=plt.Circle( (0,0), 0.7, color='white')
        plt.text(0, 0, str(100-i)+"%", ha='center', va='center', fontsize=42, color='#3AA9FF')
        p=plt.gcf()
        p.gca().add_artist(circle)
        plt.savefig("./src/static/" + str(100-i) + "pourcent.png", transparent=True)
        plt.close()


stat_chart()
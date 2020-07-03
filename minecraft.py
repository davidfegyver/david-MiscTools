from mcstatus import MinecraftServer
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import time
xar = []
yar = []

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ip = input(" Server IP:  ")
interval = int(input("Interval: "))*1000
server = MinecraftServer.lookup(ip)

def animate(i):

	status = server.status()

	if status.players.online != 0:
		print(str(status.players.online) + " Online Players")
		xar.append(datetime.now())
		yar.append(status.players.online)
		ax1.plot(xar,yar)

	
ani = animation.FuncAnimation(fig, animate, interval=interval)
plt.show()


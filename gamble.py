from gamblesim import *
from matplotlib import pyplot as plt

fig = plt.figure(figsize = (12, 8))

ax1 = fig.add_subplot(331)
plt.title("SET 10")
market = SET(10, 100, 1000, 100)
for bidder in market:
    plt.plot(bidder, color="b")

ax2 = fig.add_subplot(332)
plt.title("SET 20")
market = SET(20, 100, 1000, 100)
for bidder in market:
    plt.plot(bidder, color="b")

ax3 = fig.add_subplot(333)
plt.title("SET 30")
market = SET(30, 100, 1000, 100)
for bidder in market:
    plt.plot(bidder, color="b")

ax4 = fig.add_subplot(334)
plt.title("SET 40")
market = SET(40, 100, 1000, 100)
for bidder in market:
    plt.plot(bidder, color="b")

ax5 = fig.add_subplot(335)
plt.title("SET 50")
market = SET(50, 100, 1000, 100)
for bidder in market:
    plt.plot(bidder, color="b")

ax6 = fig.add_subplot(336)
plt.title("SET 60")
market = SET(60, 100, 1000, 100)
for bidder in market:
    plt.plot(bidder, color="b")

ax7 = fig.add_subplot(337)
plt.title("SET 70")
market = SET(70, 100, 1000, 100)
for bidder in market:
    plt.plot(bidder, color="b")

ax8 = fig.add_subplot(338)
plt.title("SET 80")
market = SET(80, 100, 1000, 100)
for bidder in market:
    plt.plot(bidder, color="b")

ax9 = fig.add_subplot(339)
plt.title("SET 90")
market = SET(90, 100, 1000, 100)
for bidder in market:
    plt.plot(bidder, color="b")

plt.show()

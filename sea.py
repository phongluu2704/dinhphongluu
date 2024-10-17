# # # import matplotlib.pyplot as plt
# # # import matplotlib.gridspec as gridspec

# # # # Tạo figure
# # # fig = plt.figure()

# # # # Sử dụng GridSpec để chia lưới biểu đồ
# # # gs = gridspec.GridSpec(2, 3, height_ratios=[1, 2])

# # # # Tạo các subplot
# # # ax1 = plt.subplot(gs[0, 0])
# # # ax2 = plt.subplot(gs[0, 1])
# # # ax3 = plt.subplot(gs[0, 2])
# # # ax4 = plt.subplot(gs[1, :])

# # # # Hiển thị biểu đồ
# # # plt.tight_layout()
# # # plt.show()

# import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec

# # Tạo figure
# fig = plt.figure(figsize=(10, 8))

# # Chia lưới 3x3
# gs = gridspec.GridSpec(4, 2, figure=fig)

# # Thêm subplots theo cấu trúc yêu cầu
# ax0 = fig.add_subplot(gs[0, 0])
# ax1 = fig.add_subplot(gs[0, 1])  # Hình nhỏ 1
# ax2 = fig.add_subplot(gs[1, 0])  # Hình nhỏ 2
# ax3 = fig.add_subplot(gs[2, 0])  # Hình nhỏ 3
# ax4 = fig.add_subplot(gs[1:3,1])  
# ax5 = fig.add_subplot(gs[3, :])  
# # ax6 = fig.add_subplot(gs[1, 2])  
# # ax7 = fig.add_subplot(gs[2, 1:3])  

# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Create figure
fig = plt.figure(figsize=(10, 8))

# Define a 3x2 grid
gs = gridspec.GridSpec(3, 2, figure=fig)

# Add subplots according to the specified structure
ax0 = fig.add_subplot(gs[0, :])  # Full width subplot on top
ax1 = fig.add_subplot(gs[1:3, 0])  # Left subplot spanning rows 1 and 2
ax2 = fig.add_subplot(gs[1, 1])  # Right subplot in the second row
ax3 = fig.add_subplot(gs[2, 1])  # Right subplot in the third row

# Set titles for clarity
ax0.set_title('Full Width Subplot')
ax1.set_title('Combined Subplot 1 & 3')
ax2.set_title('Subplot 2')
ax3.set_title('Subplot 4')

# Adjust layout
plt.tight_layout()
plt.show()


# import matplotlib.pyplot as plt
# from matplotlib.gridspec import GridSpec
# fig = plt.figure()
# gs = GridSpec(1, 1,
#  bottom=0.2,
#  left=0.15,
#  top=0.8)
# ax = fig.add_subplot(gs[0,0])
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt


# x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
# y1 = np.sin(x)
# y2 = 3 * np.sin(x)


# plt.figure(figsize=(6, 6))
# plt.plot(x, y1, label=r'$\sin(x)$')
# plt.plot(x, y2, label=r'$3\sin(x)$')


# x_point = 3 * np.pi / 4
# y_point = 3 * np.sin(x_point)
# plt.annotate(
#     rf'$(3\sin(\frac{{3\pi}}{{4}}), \frac{{3\sqrt{{2}}}}{{2}})$',
#     xy=(x_point, y_point),
#     xytext=(x_point + 0.5, y_point + 1),
#     arrowprops=dict(facecolor='blue', arrowstyle="wedge,tail_width=1.", lw=2),
#     fontsize=12,
#     ha='center'
# )


# plt.legend()


# plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi], 
#            [r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])


# plt.xlim(-2 * np.pi, 2 * np.pi)
# plt.ylim(-4, 4)
# plt.grid(True)


# plt.show()
# import matplotlib.pyplot as plt
# import matplotlib as mpl

# # Check available styles and choose a valid one
# plt.style.use("seaborn-v0_8-whitegrid")  # Updaưted to a valid style
# import numpy as np
# import pandas as pd

# births = pd.read_csv(ư
#     "https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv"
# )
# quartiles = np.percentile(births["births"], [25, 50, 75])
# mu, sig = quartiles[1], 0.74 * (quartiles[2] - quartiles[0])
# births = births.query("(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)")
# births["day"] = births["day"].astype(int)
# births.index = pd.to_datetime(
#     10000 * births.year + 100 * births.month + births.day, format="%Y%m%d"
# )
# births_by_date = births.pivot_table("births", [births.index.month, births.index.day])
# births_by_date.index = [
#     pd.Timestamp(2012, month, day) for (month, day) in births_by_date.index
# ]

# fig, ax = plt.subplots(figsize=(12, 4))
# births_by_date.plot(ax=ax)

# fig, ax = plt.subplots(figsize=(12, 4))
# births_by_date.plot(ax=ax)
# # Add labels to the plot
# style = dict(size=10, color='gray')
# ax.text('2012-1-1', 3950, "New Year's Day", **style)
# ax.text('2012-7-4', 4250, "Independence Day", ha='center', **style)
# ax.text('2012-9-4', 4850, "Labor Day", ha='center', **style)
# ax.text('2012-10-31', 4600, "Halloween", ha='right', **style)
# ax.text('2012-11-25', 4450, "Thanksgiving", ha='center', **style)
# ax.text('2012-12-25', 3850, "Christmas ", ha='right', **style)
# # Label the axes
# ax.set(title='USA births by day of year (1969-1988)',
# ylabel='average daily births')
# # Format the x axis with centered month labels
# ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
# ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
# ax.xaxis.set_major_formatter(plt.NullFormatter())
# ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'))
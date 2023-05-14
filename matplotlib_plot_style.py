# -*- encoding: utf-8 -*-
'''
@File  :   matplotlib_plot_style.py
@Date  :   2023/05/14 20:42:31
@Author:   单哥
@Email :   chend_zqfpu@163.com
'''

import numpy as np
import matplotlib.pyplot as plt
# plt.style.use('default') # 默认布局，下方和左侧有刻度线（朝外）
# plt.style.use('classic') # 经典布局，四周都显示刻度线（朝内）
# plt.style.use('Solarize_Light2') # 淡黄色背景，白色实线方格
# plt.style.use('bmh') # 下方和左侧有刻度线，刻度线朝内，方格面板，格线是虚线
# plt.style.use('dark_background') # 黑色背景，下方和左侧有刻度线（朝外）
# plt.style.use('fivethirtyeight') # 无坐标轴线，无刻度，方格面板，绘图线条较粗
# plt.style.use('ggplot') # 灰色方格面板，格线是白色实线
# plt.style.use('grayscale') # 黑白图
# plt.style.use('seaborn') # 无刻度线，白色实线方格面板（面板是浅色）
# plt.style.use('seaborn-ticks') # 刻度线稍长

print(plt.style.available) # 输出可用的风格

def plot_scatter(ax, nb_samples = 100):
    """Scatter plot."""
    for mu, sigma, marker in [(-.5, 0.75, 'o'), (0.75, 1., 's')]:
        x, y = np.random.normal(loc=mu, scale=sigma, size=(2, nb_samples))
        ax.plot(x, y, ls='none', marker=marker)
    ax.set_xlabel('X-label')
    ax.set_ylabel('Y-label')
    ax.set_title('title')


def plot_heatmap(ax, size=(20, 20)):
    """Plot an image with random values and superimpose a circular patch."""
    values = np.random.random_sample(size=size)
    ax.imshow(values, interpolation='none')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel('X-label')
    ax.set_ylabel('Y-label')
    ax.set_title('title')


def plot_bar_graphs(ax, min_value=5, max_value=25, nb_samples=5):
    x = np.arange(nb_samples)
    ya, yb = np.random.randint(min_value, max_value, size=(2, nb_samples))
    width = 0.3
    ax.bar(x, ya, width)
    ax.bar(x + width, yb, width, color='C2')
    ax.set_xticks(x + width/2, labels=['a', 'b', 'c', 'd', 'e'])
    ax.set_xlabel('X-label')
    ax.set_ylabel('Y-label')
    ax.set_title('title')


def plot_colored_lines(ax):
    """Plot lines with colors following the style color cycle."""
    t = np.linspace(-10, 10, 100)
    def sigmoid(t, t0):
        return 1 / (1 + np.exp(-(t - t0)))

    nb_colors = len(plt.rcParams['axes.prop_cycle'])
    shifts = np.linspace(-5, 5, nb_colors)
    amplitudes = np.linspace(1, 1.5, nb_colors)
    for t0, a in zip(shifts, amplitudes):
        ax.plot(t, a * sigmoid(t, t0), '-')
    ax.set_xlim(-10, 10)
    ax.set_xlabel('X-label')
    ax.set_ylabel('Y-label')
    ax.set_title('title')



def plot_histograms(ax, nb_samples=10000):
    params = ((10, 10), (4, 12), (50, 12), (6, 55))
    for a, b in params:
        values = np.random.beta(a, b, size=nb_samples)
        ax.hist(values, histtype="stepfilled", bins=30,
                alpha=0.8, density=True)

    ax.annotate('Annotation', xy=(0.25, 4.25),
                xytext=(0.9, 0.9), textcoords=ax.transAxes,
                va="top", ha="right",
                bbox=dict(boxstyle="round", alpha=0.2),
                arrowprops=dict(
                          arrowstyle="->",
                          connectionstyle="angle,angleA=-95,angleB=35,rad=10"),
                )
    ax.set_xlabel('X-label')
    ax.set_ylabel('Y-label')
    ax.set_title('title')


def plot_colored_circles(ax, nb_samples=15):
    for sty_dict, j in zip(plt.rcParams['axes.prop_cycle'](),
                           range(nb_samples)):
        ax.add_patch(plt.Circle(np.random.normal(scale=3, size=2),
                                radius=1.0, color=sty_dict['color']))

    ax.set_xlim([-4, 8])
    ax.set_ylim([-5, 6])
    ax.set_aspect('equal', adjustable='box')  # to plot circles as circles
    ax.set_xlabel('X-label')
    ax.set_ylabel('Y-label')
    ax.set_title('title')


def plot_figure(style_label):
    fig, axs = plt.subplots(ncols=6, nrows=1, num=style_label, figsize=(14.8, 2.5), layout='constrained')
    plot_scatter(axs[0])
    plot_heatmap(axs[1])
    plot_bar_graphs(axs[2])
    plot_colored_lines(axs[3])
    plot_histograms(axs[4])
    plot_colored_circles(axs[5])



if __name__ == "__main__":
    plot_styles = ["default", "classic", "Solarize_Light2", "bmh", "dark_background", "fivethirtyeight", "ggplot",
                   "grayscale", "seaborn", "seaborn-ticks"]


    # plt.style.use(plot_styles[3])
    # fig, ax = plt.subplots(figsize=(3.5, 3), layout='constrained')
    # plot_scatter(ax)
    # plt.show()



    for style_label in plot_styles:
        with plt.style.context(style_label):
            plot_figure(style_label)
    
        # plt.savefig(style_label + ".pdf")
        plt.show()


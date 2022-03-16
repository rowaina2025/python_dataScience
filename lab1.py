{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Statistics_Lab1.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rowaina2025/DotesAndBoxes/blob/dots-and-boxes/Statistics_Lab1.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7EinjAkHU3P1"
      },
      "source": [
        "# Statistics Lab1"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vOuurNeVU2Nv"
      },
      "source": [
        "## Imports"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ku8v1gpvVIFT"
      },
      "source": [
        "import matplotlib.pyplot as plt #Python 2D plotting library\n",
        "from scipy.stats import norm #Python package for distributions\n",
        "import numpy as np #Python package for powerful N-dimensional array operations\n",
        "\n",
        "plt.style.use('seaborn') # pretty matplotlib plots\n",
        "plt.rcParams['figure.figsize'] = (12, 8)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "L0uivaMm6vgV"
      },
      "source": [
        "## Distribution Operations"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "g16cTGoxGtvK"
      },
      "source": [
        "def generate_data(x_min , x_max , num ):\n",
        "   \n",
        "    x = np.linspace(x_min, x_max, num) #Hint: try np.linspace() method\n",
        "    return x"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KxhJt44ns1Tq"
      },
      "source": [
        "def compute_mean_std(x):\n",
        "    \n",
        "    mean = np.mean(x) #Hint: use np for this purpose\n",
        "    std = np.std(x) #Hint: use np for this purpose\n",
        "    return mean, std"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "smXxFLdeuNGJ"
      },
      "source": [
        "def get_normal_pdf(x, mean, std):\n",
        "    \n",
        "    y = norm.pdf(x, mean, std)     #Try to write your own pdf expression. Otherwise, you can use the built-in one\n",
        "    \n",
        "    return y"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IKpQvP0F8wYq"
      },
      "source": [
        "def standardize(y):\n",
        "    mean, std = compute_mean_std(y)\n",
        "    z = (y-mean)/std\n",
        "    return z"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dRvtL-ATVKrk"
      },
      "source": [
        "## Normal Distribution Plot"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TtGDb95ZJYH_"
      },
      "source": [
        "It's required to implement a function that plots normal distribution for a given array of numbers distributed over a given range.\n",
        "\n",
        "Please, follow the following signature:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "poJi4r_UVOpO"
      },
      "source": [
        "def plot_normal(x, y = None):#, xlim_min = -1.0, xlim_max = 1.0, ylim_min = 0, ylim_max = 1.0):\n",
        "    \"\"\"\n",
        "    Plots the pdf of the normal (Gaussian) distribution\n",
        "\n",
        "    Parameters:\n",
        "    x (array-like): the data points to be plotted\n",
        "    xlim_min (float): the lower bound of x axis\n",
        "    xlim_max (float): the upper bound of x axis\n",
        "    ylim_min (float): the lower bound of y axis\n",
        "    ylim_max (float): the upper bound of y axis\n",
        "    \"\"\"\n",
        "    \n",
        "    if y is None:\n",
        "        y = get_normal_pdf(x)\n",
        "    plt.xlim(x_min,x_max)\n",
        "    plt.ylim(ylim_min,ylim_max)\n",
        "    plt.plot(x,y , color = 'blue', linewidth=4)      \n",
        "    plt.show()\n"
      ],
      "execution_count": 48,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rXV5jNUf-0Vk"
      },
      "source": [
        "## Driver Code"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "n1k5iy6CWTqp",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 513
        },
        "outputId": "30873923-df81-41a5-fa51-810a65b92256"
      },
      "source": [
        "x_min = 0.5\n",
        "x_max = 0.75\n",
        "x = generate_data(x_min, x_max, 100000)\n",
        "mean, std = compute_mean_std(x)\n",
        "\n",
        "y = get_normal_pdf(x, mean, std)\n",
        "ylim_max = np.max(y) + np.max(y)/4\n",
        "ylim_min = np.min(y)\n",
        "plot_normal(x, y) #, x_min, x_max, ylim_min, ylim_max)\n",
        "\n",
        "z = standardize(x)\n",
        "\n",
        "x_min = z[0]\n",
        "x_max = z[len(z) - 1]\n",
        "\n",
        "new_mean, new_std = compute_mean_std(z)\n",
        "\n",
        "new_y = get_normal_pdf(z, new_mean, new_std)\n",
        "x_min = np.min(z) \n",
        "x_max = np.max(z)\n",
        "ylim_min = np.min(new_y)\n",
        "ylim_max = np.max(new_y) + np.max(new_y)/4\n",
        "plot_normal(z, new_y)#, x_min, x_max, ylim_min, ylim_max)"
      ],
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "89rmO1NkG9G1"
      },
      "source": [
        "## Bonus Part"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HikLkYe1K_Y_"
      },
      "source": [
        "### CDF "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wf-8aEeq72Rm"
      },
      "source": [
        "def compute_inverse_cdf(p, mean = 0, std = 1):\n",
        "    \"\"\"\n",
        "    Computes the inverse of CDF, where P{X <= x} = p\n",
        "\n",
        "    Parameters:\n",
        "    p (float): the value of the CDF, where 0 <= p <= 1\n",
        "    mean a.k.a µ (float): the mean of the normal distribution\n",
        "    std a.k.a σ (float): the standard deviation of the normal distribution mean\n",
        "\n",
        "    Returns:\n",
        "    x (float): the point that satisfies the equation P{X <= x} = p\n",
        "    \"\"\"\n",
        "\n",
        "    x = #No hints\n",
        "    return x"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0r4z0XVtLEgt"
      },
      "source": [
        "### CDF Plot"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "itF_SPz01xJM"
      },
      "source": [
        "def plot_cdf(x, cdf=0.5):\n",
        "    \"\"\"\n",
        "    Plots the cdf of the normal (Gaussian) distribution at a given certain point\n",
        "\n",
        "    Parameters:\n",
        "    x (array-like): the data points to be plotted\n",
        "    cdf: the plot shaded percentage that representins the normal distribution cdf\n",
        "    \"\"\"\n",
        "    \n",
        "    #No hints\n",
        "    \n",
        "    plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9i9wwFV0HH3-"
      },
      "source": [
        "### Driver Code"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EZpZgCxZRqRv"
      },
      "source": [
        "percent = 0.8\n",
        "plot_cdf(x, percent)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}

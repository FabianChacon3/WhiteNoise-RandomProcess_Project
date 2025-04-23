{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "mount_file_id": "https://github.com/FabianChacon3/WhiteNoise-RandomProcess_Project/blob/Fabian-2214192/Funciones.ipynb",
      "authorship_tag": "ABX9TyO7IUfDZ/o/tpH782CRYWQC",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/FabianChacon3/WhiteNoise-RandomProcess_Project/blob/Fabian-2214192/Funciones.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Funciones*\n"
      ],
      "metadata": {
        "id": "U-xqY7mj1tsg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Funciones.py\n",
        "\n",
        "import numpy as np\n",
        "from scipy.signal import lfilter\n",
        "\n",
        "def generar_AR1(alpha, sigma, n):\n",
        "    w = np.random.normal(0, sigma, n)\n",
        "    x = np.zeros(n)\n",
        "    for i in range(1, n):\n",
        "        x[i] = alpha * x[i-1] + w[i]\n",
        "    return x\n",
        "\n",
        "def aplicar_filtro_fir(x, a):\n",
        "    b = [1, -1/a, 1/(2*a)]\n",
        "    return lfilter(b, [1], x)\n",
        "\n",
        "def aplicar_filtro_impulso(x):\n",
        "    h = np.zeros(3)\n",
        "    h[2] = 3  # h(t) = 3δ(t-2)\n",
        "    return np.convolve(x, h, mode='same')\n",
        "\n",
        "def calcular_autocorrelacion(x):\n",
        "    n = len(x)\n",
        "    x_mean = np.mean(x)\n",
        "    autocorr = np.correlate(x - x_mean, x - x_mean, mode='full') / n\n",
        "    return autocorr\n",
        "\n"
      ],
      "metadata": {
        "id": "qF_7wKSo521g"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
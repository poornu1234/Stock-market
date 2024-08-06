{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "88d67c13-1dca-451c-85d5-eb234183c342",
      "metadata": {
        "id": "88d67c13-1dca-451c-85d5-eb234183c342"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import yfinance as yf"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f3bc102c-1442-4cae-9093-f77f2b7b7e0c",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f3bc102c-1442-4cae-9093-f77f2b7b7e0c",
        "outputId": "b0de019e-cdb7-4670-885d-452bf67e6935"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\r[*********************100%%**********************]  1 of 1 completed\n"
          ]
        }
      ],
      "source": [
        "start = '2012-01-01'\n",
        "end = '2022-12-21'\n",
        "stock = 'GOOG'\n",
        "\n",
        "data = yf.download(stock, start, end)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8657c12a-ec44-4ea9-80c9-7ecbec9b0084",
      "metadata": {
        "id": "8657c12a-ec44-4ea9-80c9-7ecbec9b0084"
      },
      "outputs": [],
      "source": [
        "data.reset_index(inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e8fadd81-946b-47fc-b014-8ecf059302ce",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "e8fadd81-946b-47fc-b014-8ecf059302ce",
        "outputId": "3a603934-9894-44bd-df2c-5ecbe1a52720"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "           Date       Open       High        Low      Close  Adj Close  \\\n",
              "0    2012-01-03  16.262545  16.641375  16.248346  16.573130  16.554291   \n",
              "1    2012-01-04  16.563665  16.693678  16.453827  16.644611  16.625692   \n",
              "2    2012-01-05  16.491436  16.537264  16.344486  16.413727  16.395069   \n",
              "3    2012-01-06  16.417213  16.438385  16.184088  16.189817  16.171415   \n",
              "4    2012-01-09  16.102144  16.114599  15.472754  15.503389  15.485767   \n",
              "...         ...        ...        ...        ...        ...        ...   \n",
              "2756 2022-12-14  95.540001  97.220001  93.940002  95.309998  95.201660   \n",
              "2757 2022-12-15  93.540001  94.029999  90.430000  91.199997  91.096336   \n",
              "2758 2022-12-16  91.199997  91.750000  90.010002  90.860001  90.756721   \n",
              "2759 2022-12-19  90.879997  91.199997  88.925003  89.150002  89.048668   \n",
              "2760 2022-12-20  88.730003  89.779999  88.040001  89.629997  89.528122   \n",
              "\n",
              "         Volume  \n",
              "0     147611217  \n",
              "1     114989399  \n",
              "2     131808205  \n",
              "3     108119746  \n",
              "4     233776981  \n",
              "...         ...  \n",
              "2756   26452900  \n",
              "2757   28298800  \n",
              "2758   48485500  \n",
              "2759   23020500  \n",
              "2760   21976800  \n",
              "\n",
              "[2761 rows x 7 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3419b022-43c7-4ef6-9646-1fb9906bda52\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Date</th>\n",
              "      <th>Open</th>\n",
              "      <th>High</th>\n",
              "      <th>Low</th>\n",
              "      <th>Close</th>\n",
              "      <th>Adj Close</th>\n",
              "      <th>Volume</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2012-01-03</td>\n",
              "      <td>16.262545</td>\n",
              "      <td>16.641375</td>\n",
              "      <td>16.248346</td>\n",
              "      <td>16.573130</td>\n",
              "      <td>16.554291</td>\n",
              "      <td>147611217</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2012-01-04</td>\n",
              "      <td>16.563665</td>\n",
              "      <td>16.693678</td>\n",
              "      <td>16.453827</td>\n",
              "      <td>16.644611</td>\n",
              "      <td>16.625692</td>\n",
              "      <td>114989399</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2012-01-05</td>\n",
              "      <td>16.491436</td>\n",
              "      <td>16.537264</td>\n",
              "      <td>16.344486</td>\n",
              "      <td>16.413727</td>\n",
              "      <td>16.395069</td>\n",
              "      <td>131808205</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2012-01-06</td>\n",
              "      <td>16.417213</td>\n",
              "      <td>16.438385</td>\n",
              "      <td>16.184088</td>\n",
              "      <td>16.189817</td>\n",
              "      <td>16.171415</td>\n",
              "      <td>108119746</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2012-01-09</td>\n",
              "      <td>16.102144</td>\n",
              "      <td>16.114599</td>\n",
              "      <td>15.472754</td>\n",
              "      <td>15.503389</td>\n",
              "      <td>15.485767</td>\n",
              "      <td>233776981</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2756</th>\n",
              "      <td>2022-12-14</td>\n",
              "      <td>95.540001</td>\n",
              "      <td>97.220001</td>\n",
              "      <td>93.940002</td>\n",
              "      <td>95.309998</td>\n",
              "      <td>95.201660</td>\n",
              "      <td>26452900</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2757</th>\n",
              "      <td>2022-12-15</td>\n",
              "      <td>93.540001</td>\n",
              "      <td>94.029999</td>\n",
              "      <td>90.430000</td>\n",
              "      <td>91.199997</td>\n",
              "      <td>91.096336</td>\n",
              "      <td>28298800</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2758</th>\n",
              "      <td>2022-12-16</td>\n",
              "      <td>91.199997</td>\n",
              "      <td>91.750000</td>\n",
              "      <td>90.010002</td>\n",
              "      <td>90.860001</td>\n",
              "      <td>90.756721</td>\n",
              "      <td>48485500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2759</th>\n",
              "      <td>2022-12-19</td>\n",
              "      <td>90.879997</td>\n",
              "      <td>91.199997</td>\n",
              "      <td>88.925003</td>\n",
              "      <td>89.150002</td>\n",
              "      <td>89.048668</td>\n",
              "      <td>23020500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2760</th>\n",
              "      <td>2022-12-20</td>\n",
              "      <td>88.730003</td>\n",
              "      <td>89.779999</td>\n",
              "      <td>88.040001</td>\n",
              "      <td>89.629997</td>\n",
              "      <td>89.528122</td>\n",
              "      <td>21976800</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>2761 rows × 7 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3419b022-43c7-4ef6-9646-1fb9906bda52')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-3419b022-43c7-4ef6-9646-1fb9906bda52 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-3419b022-43c7-4ef6-9646-1fb9906bda52');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-441db063-df31-4846-98ab-8705765a9ae9\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-441db063-df31-4846-98ab-8705765a9ae9')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-441db063-df31-4846-98ab-8705765a9ae9 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_1a5251b8-665b-4bb0-8cec-8e0df646eb7a\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('data')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_1a5251b8-665b-4bb0-8cec-8e0df646eb7a button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('data');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "data",
              "summary": "{\n  \"name\": \"data\",\n  \"rows\": 2761,\n  \"fields\": [\n    {\n      \"column\": \"Date\",\n      \"properties\": {\n        \"dtype\": \"date\",\n        \"min\": \"2012-01-03 00:00:00\",\n        \"max\": \"2022-12-20 00:00:00\",\n        \"num_unique_values\": 2761,\n        \"samples\": [\n          \"2013-06-20 00:00:00\",\n          \"2022-12-19 00:00:00\",\n          \"2017-04-18 00:00:00\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Open\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 35.77607091660626,\n        \"min\": 13.956189155578613,\n        \"max\": 151.86349487304688,\n        \"num_unique_values\": 2697,\n        \"samples\": [\n          47.875999450683594,\n          39.685001373291016,\n          34.90399932861328\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"High\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 36.19567209308303,\n        \"min\": 14.060298919677734,\n        \"max\": 152.10000610351562,\n        \"num_unique_values\": 2717,\n        \"samples\": [\n          72.04199981689453,\n          25.490205764770508,\n          46.54574966430664\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Low\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 35.36684697438592,\n        \"min\": 13.861044883728027,\n        \"max\": 149.8874969482422,\n        \"num_unique_values\": 2723,\n        \"samples\": [\n          45.59349822998047,\n          30.35123634338379,\n          52.4057502746582\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Close\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 35.77509129178351,\n        \"min\": 13.92405891418457,\n        \"max\": 150.70899963378906,\n        \"num_unique_values\": 2736,\n        \"samples\": [\n          26.752052307128906,\n          52.660499572753906,\n          21.761184692382812\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Adj Close\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 35.734427132920885,\n        \"min\": 13.908231735229492,\n        \"max\": 150.53768920898438,\n        \"num_unique_values\": 2736,\n        \"samples\": [\n          26.721643447875977,\n          52.600643157958984,\n          21.7364501953125\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Volume\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 36048129,\n        \"min\": 158434,\n        \"max\": 499561487,\n        \"num_unique_values\": 2670,\n        \"samples\": [\n          20908000,\n          68584110,\n          23714000\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 4
        }
      ],
      "source": [
        "data"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8a478e83-6aee-4809-9405-be6f8b65b16a",
      "metadata": {
        "id": "8a478e83-6aee-4809-9405-be6f8b65b16a"
      },
      "outputs": [],
      "source": [
        "ma_100_days = data.Close.rolling(100).mean()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fc840124-ef3e-40b0-9e74-aa5a174c4c50",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 522
        },
        "id": "fc840124-ef3e-40b0-9e74-aa5a174c4c50",
        "outputId": "c0dbed23-f67a-413b-976f-1e9ebf56d388"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAqQAAAH5CAYAAABXviwdAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAACKWElEQVR4nO3dd3QU1d/H8femh0ASQknoHUFAivQiKEhXsKOIoggWUBELoqKP/lDsYkHBhg1EkSKigBQpKiC9V0FAIKEmIQnp8/wx7mQ3u2mw6Z/XOTl75947s3ezgl9utRmGYSAiIiIiUki8CrsBIiIiIlK6KSAVERERkUKlgFRERERECpUCUhEREREpVApIRURERKRQKSAVERERkUKlgFRERERECpVPYTfgYqSnp3P8+HHKlSuHzWYr7OaIiIiISCaGYXD+/HmqVq2Kl1f2faDFMiA9fvw4NWrUKOxmiIiIiEgOjh49SvXq1bOtUywD0nLlygHmBwwODi7k1oiIiIhIZrGxsdSoUcOK27JTLANS+zB9cHCwAlIRERGRIiw30yu1qElERERECpUCUhEREREpVApIRURERKRQKSAVERERkUKlgFRERERECpUCUhEREREpVApIRURERKRQKSAVERERkUKlgFRERERECpUCUhEREREpVApIRURERKRQKSAVERERkUKlgFRERERECpUCUhEREREpVApIRURERKRQKSAVERERkUKlgFRERERECpUCUhERERFg2uZp3Df/PlLTUwu7KaWOT2E3QERERKQouHf+vQBcXftqBl8xuJBbU7qoh1RERETEwZGYI4XdhFJHAamIiIiUeoejD1vp+JT4QmxJ6aSAVEREREq1qLgoar9b27r2tnkXXmNKKQWkIiIiUqo9/uvjTtc+XlpiU9AUkIqIiEipNn37dJe8gTMHcuN3N2IYRiG0qPTRPwFERESk1EpMTXTJm7VrFttPbgdg/t75DGg0oKCbVeqoh1RERERKrau/vNolb++ZvVb6082f8syyZ0hKTbLyohOjeeOPN7Qa34MUkIqIiEiptfbftS55aelpVnrBvgVM/H0ik9dPtvIe+vkhnlr6FB0/61ggbSwNFJCKiIiIOEgz0lzy9p/Zb6V//ftXAI6dP1ZgbSrpFJCKiIiI5CDAJ8BK22y2QmxJyaSAVERERCQHvt6+VtrLpvDJ0/QbFREREcnB9zu/t9IKSD1Pv1EREREplRznhQKMaDUiy7qOx4na0JC9pykgFRERkRIp3Ujnvvn38cJvL7gtT0lPcbp+r897WT4rOS3ZSmsOqedpY3wREREpkWZsn8Fnmz8DoGe9nnSq2cmpPPMpTNkdGeoYkGrI3vP0GxUREZESadXhVVa687TOfLT+I6fyzNs7ZRdoJqYmWpvja8je8xSQioiISInk2KsJ8NAvDzldpxvpTtc5DcVP3Tg1V/Uk7xSQioiISIkUmxSbbbnjiUy5Yd8QX0P2nqffqIiIiJRI7gJSxyA0cw9pTppWbgooIM0P+o2KiIhIiZSUluSSZx/Gj0+O59nlz+bpefZgNjdzSA3DyHMPbGmmgFRERERKJPsiJEf2gPTFlS+y5OASK79Z5WY5Pi9t7g/w1FO56iG9a95d1JxUk5jEmDy0uPRSQCoiIiIlkrseUnvemn/XOOX/MviXHJ+X/s8/8MYb2E6fzrbe7F2z+WbbNxw/f5yZO2bmvsGlmAJSERERKXFS0lLYFrXNJd/eQ5qanmrlNarYiOrB1XN8ZlrD+uazY85Zee7mod486+Y8t7e0U0AqIiIiJc7Kwyvd5jd8vyExiTGkpGWc0nQm4Uyunpne81po145D5TPyLqRcyPYeAyPbcjEpIBUREZESJzox2m3+hdQLTNsyzWkF/vnk81a6YYWGWT4zzUiHJ5+k3z6HvH+PZNuOzKdBiXsKSEVERKTEya7nMjU9lUYVG1nXjouUrq17rZX+/TPokRDBoCaDgP+G5wcOpJpXSMazOrSDZcs82fRSSQGpiIiIlDiJqYlW2t/b36nM18uXmKSM1e+O80DL+ZWz0p3+tbFk+GquCL8CgE82fcL7Gz7E1refVScm+Tz06AF33gknT7ps9aQh+9xRQCoiIiIlzoVUs4f0tia3cWzMMaeydCOdnSd3WteOw+pDmg8BoOUJYMAAqF/fqQf1kUWPYJQta10PeDDUTEyfDr16sfv4Vqf30pB97uQ5IF21ahXXXXcdVatWxWazMW/evCzrPvDAA9hsNiZNmuSUf/bsWQYPHkxwcDChoaEMGzaMuLi4vDZFRERExC17D2mATwAVylRwKktNT+XMhYyFTI49pJcfucDRt+HPz4BnngHA28vb6X7HXs/t/tGwaBFUqgRbtrD3k1ezrCtZy3NAGh8fT/PmzZk8eXK29ebOncvatWupWrWqS9ngwYPZuXMnS5YsYcGCBaxatYoRI0bktSkiIiIibtnnkAb6BLqUZd6f1GnrpokTqR4LAbfeAW3aAK5Hhbps9dSrF/wXFyX/OMepSD2kueOT1xv69OlDnz59sq1z7NgxHn74YRYvXky/fv2cynbv3s2iRYtYv349rVu3BuD999+nb9++vPnmm24DWBEREZG8sA/ZB/gEuJZlWvBkBZj//ANz55rp/3pHAbxt3u7rO7r5ZhgwgEW2H52y7fueSvY8Poc0PT2dIUOG8OSTT9KkSROX8jVr1hAaGmoFowA9evTAy8uLdevWuX1mUlISsbGxTj8iIiIiWbEP2Qf6uvaQvvL7K07X1rD67NmQng5XXw0OMUzmHlK3w/A2G0yZwlctnLMVkOaOxwPS1157DR8fHx555BG35ZGRkVSuXNkpz8fHh7CwMCIjI93eM3HiREJCQqyfGjVqeLrZIiIiUoz9efRPBs4cyMFzB4Hsh+yz9NNP5uvAgU7ZmeeQRsa5j1eIiHDJStrlelqUuPJoQLpx40beffddvvjiC2w2m8eeO27cOGJiYqyfo0ePeuzZIiIiUvx1+rwTP+79kcFzBgOQmJaxqCknNmxw7hz8/ruZ0b+/U3nmIfv1x9bnul1Jy38FzSPNkUcD0tWrV3Py5Elq1qyJj48PPj4+HD58mMcff5zatWsDEBERwcmTJ53uS01N5ezZs0S4+ZcFgL+/P8HBwU4/IiIiIpkdOneIyLhIvtr6FeB+yD6zkIAQc6V8WhpcfjnUretUnnnIPjQgNNftSY4+Cxs35rp+aeXRgHTIkCFs27aNLVu2WD9Vq1blySefZPHixQB06NCB6OhoNjp8OcuXLyc9PZ127dp5sjkiIiJSyvh4+dB/RkYPp72HdFSbUVneE+IfAgsWmBfXXedSnnnIPs1Ic6mTlSQfYNasXNcvrfK8yj4uLo4DBw5Y14cOHWLLli2EhYVRs2ZNKlRw3uvL19eXiIgILrvsMgAaN25M7969GT58OFOmTCElJYVRo0YxaNAgrbAXERGRS+Lt5c3GExmdXvY5pO/2eZczF87w7Y5vXe4ZdeWD8NJr5kWm4Xpw7SFNSs3YNqphhYbZtifJG/jhB3j1VXPhk7iV5x7SDRs20LJlS1q2bAnAmDFjaNmyJc8//3yunzF9+nQaNWpE9+7d6du3L507d+bjjz/Oa1NEREREnByJOeJ0Xca3DGAGlXXL13Wpv/jOxTyR1s6cQ1qhAnTo4FIn8xxSx5XzqempbtsRUdachpjs5w0HD8KWLXn6HKVNnntIu3XrlqdNXv/55x+XvLCwMGbMmJHXtxYRERHJkyC/ICudObAE6FmvJ0weY1707w/ernVcekgdNtY/FX8KwzCsxdwNwhqw/+x+utTswqxds0iqUQX41+wl/a8zT1zpLHsREREpsYJ8HQJSL9dgE8OA+fPNtJv5o+C6iCkuOeO48/PJ5xm7dKx1be8xtQfCSdX+W7A9a5ZW22dDAamIiIiUWDn1kLJnD/z9N/j5Qc+ebp/RpVaXbN/jjT/fsNL23lN7IJxcOQz8/WH/fti5M6/NLzUUkIqIiEiJVdavrJV220P6439HfV59NZQr5/YZwf65224yMTWR4+ePAxkBaRJp0LWrWWHVqly2uvRRQCoiIiIlVq2QWlbax8t56UyPuj1g3jzz4oYbsn3O3lF7czz1ae/pvS55SWlJ0KmTefHnnzk3uJRSQCoiIiIlzmPtH2Nq/6n4evtaeZmH7H/qOhXWrTMvrr8+2+c1rNCQq+tcnev3b1OtDfDfinz7yn0FpFnK8yp7ERERkaKmUplKnEo4ZV2/3ettlzqZjxEN+OVXM9G+PVSpkuN7hAeFZ1tunz9aM6SmNcyflJoE7dqZe5AeOgQnTuTqvUob9ZCKiIhIsee4H+g1da5xW8dxPimQMVw/cGCu3sO+t2hWElMTAXMzfj9vP+C/IDU4GJo1MyutWZOr9yptFJCKiIhIsecYkHaq0cltHZeAdPly8zWXAanL/Q6iE6OtgDTAJwB/b3/AYRP9jh3NVwWkbikgFRERkWLPfr58rZBaPN7hcbd1HLeAAiAlBRo1gv+ON89J5iF/R+VfK89fx/4CwN/HH38fMyC1jhm1B6SaR+qWAlIREREp9uw9pKvvWU1IQIjbOm57OHPZOwrZB6QA438bD4C/t7/zkD1kBKQbNkBSkrvbSzUFpCIiIlLs2QPSzFs7OXIbkOaw3ZOjnAJSx3ouQ/Z160LlypCcDJs25fo9SwsFpCIiIlKsGYZBupEOZB+QOh4jCkDVqtC6da7fJ7cBqdshe5tNw/bZUEAqIiIixZp9/ijkEJA6zCF9cD0wYAB45T4UyhyQvt/nfbf1/Lz9nIbsDfsZ9gpIs6SAVERERIo1a1ic7APSMr5lrPSzq8jT/FHACjLtqpR1v5+ov7e/NWQPDjsAOAak9iBVAAWkIiIiUsydTjgNgK+Xb7ZbMwX7B3N/9YHcvQWq2YKhW7c8vY+vl6/TdVZD+H7eftaQPTgsbLrySvD1hchIOHw4T+9d0ikgFRERkWItKi4KgPCy4dhstmzrTtnXkC/mAf36gZ9ftnUzczyGFLIOSDP3kFrzSAMCoFUrM639SJ0oIBUREZFiK91I58WVLwIQGhCaQ+V0mDXLTA8YkOf3ytxDGugb6Laen7cf3l7eeNnMMMvqIYWMRVRaae9EAamIiIgUWz/s+oGf9/8MYAWAWVq50jxPPjgYrrsuz+/l2EPqZfNympPqyD5c77L1E2T0kCogdaKAVERERIqtnSd3WultUduyr2zvHb31VijjPpjMjmMPqa+Xb5YBqX3xk8vWT2DOIwUzINXCJosCUhERESm2cuwVtTMM+OknM52HzfAdOfaQ+nn7ue5r+h97z6jLaU0Al19uzl2NjjZ7awVQQCoiIiLFmGMvZaCP+zmdgHlk57//QlAQXHPNRb2XUw+pt6/TvqaOrB5Sd0P2vr5wxRVmWsP2FgWkIiIiUmz9E/2Plc68Ct7JDz+Yr/37m6vdL4Lj8329fLPuIbXPIf3vdcDMAc7D9vZ5pBs3XlQ7SiIFpCIiIlJsTd041Upntyk+S5aYrxexut7OsYc0Kj4qywDY3kN64OwBAI6fP860LdMyKjjOIxVAAamIiIgUU3N3z3U6NtTb5u2+4rlzsGWLmb766ot+v6y2ecrMcQ9SqwkXzmVcOK6018ImQAGpiIiIFFNfbfvK6TrLHtLVq83A77LLICLiot+vclDlXNXLfMSoi6ZNwccHTp8257WKAlIREREpnoxMvYveXln0kK5cab7m8ajQi+V4bKhbAQFmUAqwfn3+N6gYUEAqIiIixVLmnsg3rn3DfcU//jBfr7oqn1tkynyiE+B6pGnnzubrokUF0KKiTwGpiIiIFEsGZg/p0BZDOT7mOIOaDnKtlJQEmzeb6fbtC6Rd7npqbWQKSO0nRS1YYB5pWsopIBUREZFiKSElAYCutbpSpVwV95U2b4bkZKhUCerU8dh7X17p8izLcrVZf9eu5p6oJ07A1q0ea1dxpYBUREREiqXE1ETA/ap2y7p15mv79pB52PwSZBd02ntDb21ya0Ze5vf294cePcz0L794rF3FlQJSERERKZbsm81nu4ho7VrztV07j753dgGpvaxXvV5Wntstqfr2NV8VkCogFRERkeLn3bXv8sdRc7FStj2k9oDUw/NH7UGnYy9o5rKzF85aeemGm3miffpktPHMGY+2r7hRQCoiIiLFyr+x/zJ68WjrOsAni6NAo6Lgn3/Mofo2bTzaBnvQ+dXAr1gzbI3bsq61ulp5TufZ29WoAc2amYuafv3Vo+0rbhSQioiISLHy4ooXna6zHLK3zx+9/HIIDvZoG0IDQq33bl/duffV3p421drQtlpbAJLSknDL3ku6cKFH21fcKCAVERGRYuOnvT/x6eZPnfKyHLLPh+H6b274hmaVmzG1/1S35ZXKVKJLzS7WdacanYAsekghYx7pwoWQlua+TimQxRlbIiIiIkXP9TOvd8kL8gtyX/mvv8xXDy5oGnzFYAZfMdgl/62eb3Es9hhv9nzTaUW9ffP+LAPSjh0hLMw8RnTFCuje3WNtLU7UQyoiIiLFQuajQu3sw+eZKsPGjWa6dev8a9R/xnQYw1u93nLZ3snee5tlQOrrCzffbKZnzMjPJhZpCkhFRESkWMgqqHMbkB46BNHR4OcHTZrka7uyk2MPKcCt/63UL8XHiCogFRERkWIhLjnOSr/YLWNhU6BPoGtle+/oFVeYQWkhyVVA2r49eHnB8ePmTymkgFRERESKhfiUeMAcBn++6/P88+g/nHj8hOspSJARkF55ZQG20JWvty+QQ0AaFGTuBACwYUMBtKroUUAqIiIixcL5pPMAlPUrC0Ct0FpElI1wX3nTJvO1VauCaFqW7Cc0pRk5rKC375O6fn0+t6hoUkAqIiIixUJkXCQA4WXDs69oGEUmIPXxMjc0Sk1Pzb6ifSeAVavyuUVFkwJSERERKRaOnzfnV1YtVzX7iv/+ax7F6eMDTZsWQMuy5u31Xw9peg49pNdea77++SfExuZzq4oeBaQiIiJSLNgD0iplq2Rf0d47evnlEJDFsaIFxD5kv+pwDj2fdetCw4aQmgrz5uV/w4oYBaQiIiJSLOS6h3TzZvO1kIfrIWPu6LnEc8Qm5dDzOWSI+TptmlP2jpM7iE6MzofWFR0KSEVERKRYOBF3AshFQGrvIW3ZMp9blLOk1Iwz7L/f+X32q+0H/3cC1KpVEGnOl11+aDnNPmrGPT/ek5/NLHQKSEVERKRYsC9qynJlvV0R6iG1zyEFGP7TcJ5e+nTWlevUgbZtIT0dfvgBgMnrJwMwb8+8/GxmoVNAKiIiIsWCfR9S+7ZPbp06ZS5qstmgefMCalnWMh93+uH6D7O/4bbbzNfvvgMg1D/UKko30j3ZtCJFAamIiIgUSY4r02fumMmmE+ZQvP18eLfsvaP160O5cvnZvFwxcA5I3W7i7+iWW8zXP/6AqCi8bBmhmuPwf0mjgFRERESKnKHzhlJzUk2iE6NJS0/j9tm3W2X+PtkEpEVk/1G7PPdq1qhhni5lGPDTT04BaWJqoodbV3QoIBUREZEi58utX3L8/HGmbZ7mdIY9QIBPNls52XtIi8CCJnANSG3k0EMKcP315uvPPzvdn5SmHlLLqlWruO6666hatSo2m415DntlpaSkMHbsWJo1a0ZQUBBVq1blrrvu4vjx407POHv2LIMHDyY4OJjQ0FCGDRtGXFwcIiIiIo5ik2JdtkvKdsi+iPWQZp5DmuOQPUDfvubr0qX8dWydlb3yn5WebFqRkueAND4+nubNmzN58mSXsoSEBDZt2sT48ePZtGkTc+bMYe/evVxvj/T/M3jwYHbu3MmSJUtYsGABq1atYsSIERf/KURERKREik2K5eyFs0559uM4XSvHwoEDZrqI9JC6zCHNTQ9pq1ZQuTLExbHt5HYr+6mlT3m6eUVGFt9o1vr06UOfPn3cloWEhLBkyRKnvA8++IC2bdty5MgRatasye7du1m0aBHr16+ndevWALz//vv07duXN998k6pVc9hbTEREREqNNf+u4YrwK5zysjwXfssW87VGDahYMX8blksuQ/bZ9JB+v/N7xiwew6xbZtHh9tvh3XedyhtVbJQvbSwK8hyQ5lVMTAw2m43Q0FAA1qxZQ2hoqBWMAvTo0QMvLy/WrVvHDTfc4PKMpKQkkpIy5k3ElsIzXkVEREqjNf+uISElwbquUrYKTSo3cV+5iM0fBTdD9tn0kN72g7nl0+A5gzn47Dr46CMgYyP9HnV65Esbi4J8XdSUmJjI2LFjuf322wkODgYgMjKSypUrO9Xz8fEhLCyMyP9OJchs4sSJhISEWD81atTIz2aLiIhIIcocxG2N2grAVbWu4vjjx51WnjspQic02ZUPLO90nas5pACVKsF99zllpaSneKpZRU6+BaQpKSnceuutGIbBRx99dEnPGjduHDExMdbP0aNHPdRKERERKWqyGpKvV75e9jcWwR7Su5rf5XSdmzmk5fzN/VON8eOd8rM9drSYy5che3swevjwYZYvX271jgJERERw8uRJp/qpqamcPXuWiAj3R4H5+/vj75/NijoREREpMbIKvPy8/bK+6cIF2LXLTF95ZT606uJk2+Ys2HuAx+/6wCk/JU09pLlmD0b379/P0qVLqVChglN5hw4diI6OZuPGjVbe8uXLSU9Pp127dp5ujoiIiBQzWQ1N+3r5Zn3Tjh2QlmYuZqpWLZ9aduncTTfYeHwjtSbVsq7tC6FeXv2yU73kCyV3i8w895DGxcVxwL6lAnDo0CG2bNlCWFgYVapU4eabb2bTpk0sWLCAtLQ0a15oWFgYfn5+NG7cmN69ezN8+HCmTJlCSkoKo0aNYtCgQVphLyIiIhfXQ+q4/2hu52kWAndzSG+ffTtHYo5Y145HpjpKPrAn39pV2PLcQ7phwwZatmxJy//mZ4wZM4aWLVvy/PPPc+zYMebPn8+///5LixYtqFKlivXz559/Ws+YPn06jRo1onv37vTt25fOnTvz8ccfe+5TiYiISLGV1dB05j09nRTB+aPu2PdQPZNwhrf+fIvIuEiXHuGsjhv94czqEjtsn+ce0m7durmsfnOUXZldWFgYM2bMyOtbi4iISCmQVQ/p5PWTebvX2+5vsk8FLCInNGUl2N9cV3Pn3DtZdGARM3bMcOn5TTfS3faSHve5wBt/vM4zVz1bIG0tSDrLXkRERIqUrALSLFeZX7iQsSl+mzb50ygPsQekiw4sAmDTiU38E/2PU500Iy3LebTfbf46X9tXWBSQioiISJGSVTD2eo/X3d+wYQOkpkKVKlC7dv41zANS01NZc3SNU17mQDvdSHfKe7Ljk1baOy6BkkgBqYiIiBQpWfWE9qrfy/0Nf/xhvnbsWKQXNAFsi9pGx887ZlvHMAzeX/e+dV0ntI6VVkAqIiIiUgDeW/ee23x/7yz2JLcvnO6YfaBXXKQZaTz323PWdYBPgJX2Pl8yt35SQCoiIiJFypdbv3Sb7+/jJiA1jIyAtFOnfGxVwcm8yt5x0ZP3hSSIiiroJuU7BaQiIiJSLLjtId23D86cAX//Ir/lU25lDkh9vTMOBPA2gKVLC7hF+U8BqYiIiBQZiamJWZYF+ga6Zi5bZr62awd+eT+msyiKT453unbqIU0H5s0r2AYVAAWkIiIiUmTcMfuOLMtCA0JdMxcvNl97ZbHgqRiKSYqx0s90fsapZ9jbABYuhISStbhJAamIiIgUGXP3zLXSD7d92Eo/3elp18rJybB8uZkuwgHptzd9e9H3Xl7pchpVbGRde/sHQnw8zJnjiaYVGQpIRUREpEj4cP2HTtdBvkFWull4M9cb1qyBuDioVKlIzx8d1HQQRx87elH3BvkFUad8xrZPzar99zmnTfNE04oMBaQiIiJSJIz8ZWSWZZmP1wQyhuuvvRa8inZIE+jjZv5rLpQPKA/A6HajAfBt1tzca3X5cjh0yFPNK3RF+9sTERERIYeAtHfvgm3MRXC7ZVUuhAWGAeDt5Q1AWrmy0L27Wfil++2xiiMFpCIiIlIkBfllDNm7BKQnT8KmTWa6Z88CbNXFcRtQ50I5/3IAeNnMkC0tPQ3uvdcs/OILSE/P4s7iRQGpiIiIFDk96vbgpsY3WdcuAd2SJeZrixYQHl5wDbtIvl6+OVdyw9vm7fSabqTDwIEQEgKHD8Nvv3mqiYVKAamIiIgUuqTUJKfrJUOWUNavrHXtmAbg99/N1x498rtpHmGz2Xik7SN5vs/eM2r1kBppEBgIt99uVvj8c4+1sTApIBUREZFCdy7xnJVuGWGuJHecdxnsH+x8w4YN5mubNvneNk95t8+7PNru0TzdYw9ErTmk6WlmgX3Yfs4ciI72VBMLjQJSERERKXTRidGAuap80/3m3FDHYe4yvmUyKicnw7ZtZrp164Jqoke4Pf40G1ZA+t+QfVxKHJ9s/IRjDatAkyaQmAgzZ3q8nQVNAamIiIgUunMXzB5Sx9OYHBc1VQ6qnFF5xw4zKC1fHupk7NFZHDh+ptzIPGT/1davGLFgBP+38sWMXtJPPwXD8Gg7C5oCUhERESl0fx37C3A+r97P249Djx7i0KOHCPAJyKi8caP5euWV5p6cxYjjZv+5kXnI3u7TzZ/CnXdCQID5+1i0yGNtLAwKSEVERKTQrT++HoDD0Yed8muH1qZ2aG3nyo4BaTGT1x5SeyDqdtuoypXhoYfM9CuvXGrTCpUCUhERESl09hOJ+jfsn3Nl+4KmYhiQ5vXEJnsPqf334+Lxx8HPz9x1YNmyS21eoVFAKiIiIoUuNT0VgMsrXZ59xaSkYrugCcDXO2/7kdoDUvuJTS6qVoV77jHTt9wCJ05cSvMKjQJSERERKXT2gNTHyyf7ijt2QEqKuaCpdu38b5iH2VfL55Y9IA0vm83m/6++Ck2bwrlz8Oabl9K8QqOAVERERApdSnoKkIuA1D5/tHXrYregCXLx+TKxB6QNKzTMulJoKLzxhpmeMgXOnLnI1hUeBaQiIiJS6Ow9pDkesVmMFzTBxQekFQIrZF+xVy+zlzQhAX7++WKbV2gUkIqIiEihy3UPaTFe0ATQpHKTHOvcfPnNVtoekNoy9QY3qtjI+SabDQYMMNMKSEVERETyLldzSJOSYPt2M10MFzQB1A+rn235xO4TsZERfNoD0szCg9zMKe3Xz3xdvBhSUy+6jYVBAamIiIgUOmvIPrtV6Nu3mwuawsKgVq0CalnBiXk6hqc7P+2U5xicjm432kqnGWmuD2jbFipWhJgY+PPP/GpmvlBAKiIiIoUuJS0XQ/bFfEFTToL9g51ewXmo3nFz/LR0NwGptzf07m2mi9mwvQJSERERKXS5GrIv5vNHc8tlfuh/HHuP04109zf37Wu+zp1brM63V0AqIiIihS5Xq+wde0hLsKx+B049pO6G7AH694egINi/H1avzo/m5QsFpCIiIlLoclxln5hobooPJb6HNKvfwUNtHrLSbofsAcqVgzvuMNMff+zppuUbBaQiIiJS6HIcsrcvaKpQAWrWLMCWFbysfgcVy1Rk4eCFQDZD9gAjRpivP/xQbDbJV0AqIiIiBcIwDJ5a8hQTV090KbMvaspylX0JXNAU4h9ipYN8g6x0dvNo7WVZDtmD2YPcooW5TdbXX19yOwuCAlIREREpEFsit/DGn2/wzPJnSEpNcirLsYe0BC5o8vX2JeqJKJ7o8AQbR2y08rMLSL1t3gAkpyVn/WCbLaOX9KOPIC2b4LWIUEAqIiIiBeKf6H+sdGRcJIsOLOKJX58gJS0l50VNJXBBU6OKjagcVJk3er7BZRUvs/KzC0jtG+XvO7Mv63mkAIMHm2fc79sHixZ5qsn5RgGpiIiIFIgzFzLmMy7Yt4A+0/vw1pq3+GzzZ9kvarpwoUQtaPrkuk8I8AngkbaPuC3P7nCA0wmnrXRkXGTWbxIcDEOGmOlZsy6qnQVJAamIiIgUiGOxx6z0qIWjrPQ/0f9kP2S/ZYt5FGZ4ONSokd/NzHf3tbqP2KdjuaXJLW7L21Zrm+W9jsGq/XdmF5MYQ3xyfEbGzTebrz/+aO5SUIQpIBUREZF8N3vXbP5v5f+5LTufdD77o0PXrTNf27YtMQuasusFrR1am10P7SLycdce0H4N+lnpC6kXrHR8cjyhr4VS6Y1KGZU7dTID+OhomD7dI+3OLwpIRUREJN+NXTo2y7IPN3xIYqrZg+e2h/Svv8zXdu3yo2lFUuNKjQkvG+6S7+3lTZWyVQC4kJIRkO46tcvMcwhS8faGRx8102++CenZbBVVyBSQioiISL7LrkcQ4GT8SSCHgLRt1kPZpUmgbyCAFcRnThuOR4YOH27OJ92zB379tcDamFcKSEVERCTfNa3cNFf1XFbZnz4Nf/9tptu08XCriif7XNyvtn5l5TkFpDgEpMHBcPfdZroI70mqgFRERETy3Q+7fshVPZce0rVrzdfLLjO3MRKS0sw9XKdsnGLlOQ7Vu5ziZF9tP3s2nDiR7+27GApIRUREpMjw8/Zzzli50ny96qqCb0wRdW+LewGsuaSQzZA9mHu3tm1rntxURLeAUkAqIiIiBSa7LY0AKgdVds5Ytcp8VUBq6dugLwB1y9e18hwDUpceUpsNbrzRTC9blu/tuxgKSEVERKTAfDXwq2zL/X38My7i4jJOaFJAarEvarqQeoHfDv3GjpM7sg9IAXr0MF9/+83c07WIyfpsKhEREREPCfQJ5ELqBdcheQfB/sHOGX/+aZ7DXqsW1KyZzy0sPgJ9zID04LmDXPPVNQA80/kZq9xtQNqihRnUt2kD8fEQElIQTc01BaQiIiKS7+xBkreXd5Z1XOY+2ofru3bNr2YVS/Ye0ujEaCtv4YGFVtpplb2dt3fGfNwiSEP2IiIiku/sAamXLevQo0+DPs4Zmj/qlr2H1NHmyM1W2rGH9I8jf7D4wOICadelUA+piIiI5Ls0Iw0wA9I2Vduw/vh6q+ytnm+RnJbMfa3uy7ghMTHjyFAFpE7sPaRZcQxIO0/rDMD64etpXbV1vrbrUuS5h3TVqlVcd911VK1aFZvNxrx585zKDcPg+eefp0qVKgQGBtKjRw/279/vVOfs2bMMHjyY4OBgQkNDGTZsGHFxcZf0QURERKTosobsbd6sumeVld+3QV/GdBjD052fpmKZihk3rFsHyclQpQrUr1/QzS3SAnwCsi23T31wnAKx7GDRXF1vl+eAND4+nubNmzN58mS35a+//jrvvfceU6ZMYd26dQQFBdGrVy8SEzNWfw0ePJidO3eyZMkSFixYwKpVqxgxYsTFfwoREREpshwDIy+bFwE+AaQ9n8Zf9/3F7Ftnu7/JcbjeZiuAVhYf7obsHdmDf8ee0sMxh/O1TZcqz0P2ffr0oU+fPm7LDMNg0qRJPPfccwwYMACAr776ivDwcObNm8egQYPYvXs3ixYtYv369bRubXYdv//++/Tt25c333yTqlWrXsLHERERkaLGPlwPGYuavGxetKmWzVGgmj+apdwO2TsGpI4LoIoijy5qOnToEJGRkfSw73UFhISE0K5dO9asWQPAmjVrCA0NtYJRgB49euDl5cU6+1yRTJKSkoiNjXX6ERERkeLBMTDKblGTJSXF3PIJFJC6kVMPqX2VveM/BGKSYvK1TZfKowFpZGQkAOHh4U754eHhVllkZCSVKzufwuDj40NYWJhVJ7OJEycSEhJi/dSoUcOTzRYREZF8lJbu0ENqy3rbJ8vGjZCQABUqwOWX52PLiqfsts6CjH8AOP7e45KL9lqdYrHt07hx44iJibF+jh49WthNEhERkVzKcw+pfbi+SxfwKhahSoHr16BflmVWQOrQQ5qaXvROZ3Lk0W85IiICgKioKKf8qKgoqywiIoKTJ086laempnL27FmrTmb+/v4EBwc7/YiIiEjxcNEBqYbrs5TdSnvDMJiwagIVX8/YtSAlLaUgmnXRPBqQ1qlTh4iICJYty9haIDY2lnXr1tGhQwcAOnToQHR0NBvtZ9MCy5cvJz09nXbt2nmyOSIiIlIEuFvUlHXlNFi92kwrIM1S7dDaWZalpqcy/rfxpKRnBKGO6aIoz6vs4+LiOHDggHV96NAhtmzZQlhYGDVr1mT06NFMmDCBBg0aUKdOHcaPH0/VqlUZOHAgAI0bN6Z3794MHz6cKVOmkJKSwqhRoxg0aJBW2IuIiJRAeeoh3bYNYmOhXDnz/HVxK6Ks+1FlgPiUeJe8ot5DmueAdMOGDVx99dXW9ZgxYwC4++67+eKLL3jqqaeIj49nxIgRREdH07lzZxYtWkRAQEbX8vTp0xk1ahTdu3fHy8uLm266iffee88DH0dERESKGseANMdFTfbh+s6dzfPXxa2q5bLuxEtMTXTJS0pLys/mXLI8B6TdunVz2uA2M5vNxksvvcRLL72UZZ2wsDBmzJiR17cWERGRYshxtbctp03uV640XzVcn62bL7+ZwXMGuy1zG5CmFu2AVEvXREREJF/Ze0hzHK43DC1oyiU/b78sy4pjD6kCUhEREclX9kVNOQ7X794NZ85AYCA4HKAjeeMuIHWXV5QoIBUREZF8leseUnvvaIcO4Jd1D6C4GtlmpJX+dse3LuUashcREZFSzR6Q5rjlk+aPXrQP+n5gpb/Z9o1LeVJaUrZrgAqbAlIRERHJV+v+XQdkP+8Rw1BAepEqlamUq3pHYo7kc0sungJSERERyTcHzx1k0OxBAJTzK5d1xU2b4MQJKFPGHLKXHK0Ztoara1/Nr0N+zVX92u/Wzt8GXYI8b/skIiIikltrjq6x0uX8swlI5883X3v1goCsj8WUDO2rt2f53cvzdE98cjxBfkH51KKLpx5SERERyTe/HPjFSpf1K5t1RXtAOmBAPreo9BjZZiT1ytdzyjsRd6KQWpM9BaQiIiKSb1YfXm2ly/iWcV/p8GHYsgW8vKBv34JpWClQIbAC+x/e75SXmp5aSK3JngJSERERyTcGGSu7s1zU9PPP5mvHjlApdwt0JGf+Pv4uJ2MpIBUREZFS59/Yf620j1cWS1cWLjRf+/UrgBaVHu7+AZCSllIILcmZAlIREREpEDbcnGOfmAjL/1uY07t3wTaohPP18nXJUw+piIiIlCqZN2J3e1LT779DQgJEREDz5gXUstLB3e9bAamIiIiUKvYTmuwOnD3gWsk+XN+7N9jc9KDKRXN3MpYCUhERESlVMgc/u0/vdq20aJH52qdPAbSodLH3kI7rPM7KU0AqIiIipUqakZZ9hSNHYNcuc7una68tmEaVIt42s4f0patfsvIUkIqIiEipkmPwYx+ub98eypfP/waVcJ9e96nTtb2H1MfLhyurXAlASrpW2YuIiEgpkpaeQw+phus96uo6VztdO84htW+5pR5SERERKZGOnz9O8ynNmbR2klN+5uCnQ/UOGRdpafDbb2a6Z898bmHpkHmbJ8dV9gpIRUREpESbumEq26K28djix0hMTbTyHYOfYP9gVgxdkXHTjh0QEwNly0KrVgXY2pIr88ED9jmkjmXaGF9ERERKpJikGCu98p+VVtq+qMnP24+Yp2OcTw5atcp87dQJfLI4wUnyxNc76x7S8LLhAByOOVygbcotBaQiIiJySZLTkq30vjP7rLwvtnwBOPfUWewB6VVX5XfzSo3MQ/aOc0jrla8HwLHYYwXaptxSQCoiIiKXJD4l3kpfSL0AwGu/v8b438YDbs6wNwxYvdpMKyD1mMy/Z8ce0iDfIAASUhIKtE25pYBURERELsnWyK1W2h7wzNo1y8pzCUj374eoKPD3hzZtCqSNpUHmIXvHnulA30AANkdudjlBqyhQQCoiIiIX7VT8KbZGuQakjsP4LkdY2ofr27c3g1LxiOx6SM8nnQdg44mNRXKlvQJSERERuSiHow/z9NKnnfK+3fEt4ByQuvSQav5ovvCyeTkFoY7/EDh+/riVdlpcVkQoIBUREZGLUv/9+ny+5XOnvH9j/2XS2kkcij5k5fl7Z+oF/f1387VLl/xuYqljw2alHYPTAY0GAHBZhcsKvE25oX0WRERE5KJkNfT72OLHnK6deuROnYJD/wWrbdvmV9NKLftWWwBxyXFWuk/9PqwZtkYBqYiIiJQMhmHQ85vcn67kFJCuX2++XnYZhIR4uGXiyPGQApvNRvvq7QuxNdnTkL2IiIjkyZbILSw9uDTX9d0GpOodzXcXUi4UdhNyTQGpiIiI5Mmx8+43V29SqYnb/M2RmzMu7AGptnvKd449pEWdAlIRERHJk1Pxp1zynu70NK9f+3r2NxqGAtICVKFMhcJuQq4pIBUREZE8SUlPccmLT4mnUplK2d945AicPGmeXd+iRf40TiyDmg4q7CbkmgJSERERsRiGwR9H/iA2KTbLOu5W14cFhlEpyH1A2qF6BzNh7x294goICLjktkrWKgRWcN3/tQhTQCoiIiKWL7d+Sedpnen8eecs66Slm1sL3drkVpYOWco9Le7h0XaPElE2wqXuR/0+YsZNM8wLDdcXGMc9SIuD4hM6i4iISL77etvXAGw/uT3LOvYeUh8vH7rX7U73ut2tsqrlqlqnAn19w9fcecWdGTeuW2e+KiDNdwpIRUREpESzb77ubfN2Kds0YhO/7P+F25vdToCPw7B8Sgr89ZeZ7tixIJpZqikgFRERkRLNsYc0s/Cy4dzT8h7XmzZvhgsXICzM3BRf8lVxC0iLV2tFRESk0NnnkLrrIc3SH3+Yrx07gpfCj/ymgFRERERKNGvI3usiA1LJdwpIRUREpETLbsjerfR0+P13M92pUz61ShwpIBUREZESLc9D9uvXQ1QUlCsH7drlY8vETgGpiIiIlGh57iGdNs187dsX/P3zqVXiSAGpiIiIlGh5mkO6eTN88omZfuCBfGyVOGpauWlhNyFPFJCKiIhIntiH7HPsIU1JgREjzDmkt94K3brlf+NKuXX3rWNYy2FM6T+lsJuSJ9qHVERERAA4e+Esyw8tz7Gefcg+xzmkr7wCGzZAaCi8/bYHWig5aVutLW2rtS3sZuSZekhFREQEgGeXPZurelZAmt2Q/YED8PLLZvrDD6FatUttnpRg6iEVERERAPae2Ztjndtn387MHTMBKOtXNuuK48aZQ/a9e8Ptt3uqiVJCqYdUREREAIhNis22PC45zgpGAYL9g91XXLMGfvjBPJHp9dc92UQpoRSQioiICABdanZxujYMw+k6LjnO6TrLgPSZZ8zXoUOhWTNPNU9KMAWkIiIiAkCQX5DTdUp6itP1+aTzTtcVAiu4PuS332DFCvDzgxdf9HQTpYTyeECalpbG+PHjqVOnDoGBgdSrV4///e9/Tv/KMgyD559/nipVqhAYGEiPHj3Yv3+/p5siIiIieZCYmuh0nZKWKSBNdg5Im4Vn6v00DHjuOTM9fDhUr+7xNkrJ5PGA9LXXXuOjjz7igw8+YPfu3bz22mu8/vrrvP/++1ad119/nffee48pU6awbt06goKC6NWrF4mJidk8WURERPJTUmqS03VOPaRlfMs4P+D77+HPP6FMGXNRk0gueXyV/Z9//smAAQPo168fALVr1+bbb7/lr7/+Asze0UmTJvHcc88xYMAAAL766ivCw8OZN28egwYNcnlmUlISSUkZf0hiY7OfdC0iIiJ5F5fiPEc0cw9pfEq807W/t8MxoAkJ8OSTZvrpp7XNk+SJx3tIO3bsyLJly9i3bx8AW7du5ffff6dPnz4AHDp0iMjISHr06GHdExISQrt27VizZo3bZ06cOJGQkBDrp0aNGp5utoiISKl37sI5p+vMPaTxyc4Bqa+3b8bF1Klw9CjUrAlPPJFvbZSSyeM9pE8//TSxsbE0atQIb29v0tLSePnllxk8eDAAkZGRAISHhzvdFx4ebpVlNm7cOMaMGWNdx8bGKigVERHxsLMXzjpdZ+4hzbzK3sv2X79WUhK8+aaZfu45CAzMtzZKyeTxgPT7779n+vTpzJgxgyZNmrBlyxZGjx5N1apVufvuuy/qmf7+/vj7++dcUURERC5Kcloyq4+sdspz6SHNNGRv+fJLOH7cHKa/6678aqKUYB4PSJ988kmefvppay5os2bNOHz4MBMnTuTuu+8mIiICgKioKKpUqWLdFxUVRYsWLTzdHBEREcmFzSc2W2kbNgwMktOSrbzktGSeWfaM642GAe++a6bHjAF1IMlF8Pgc0oSEBLy8nB/r7e1Neno6AHXq1CEiIoJly5ZZ5bGxsaxbt44OHTp4ujkiIiLixs/7fqbcxHKs/Xct4Nz7GVHW7DxyDEjvmH2Hy7ZPACxfDrt2QVAQDBuWv42WEsvjPaTXXXcdL7/8MjVr1qRJkyZs3ryZt99+m3vvvRcAm83G6NGjmTBhAg0aNKBOnTqMHz+eqlWrMnDgQE83R0RERNzo/21/ADp81gHjBYOYxBgArqxyJacTTgPOc0hn757t/kH2bR3vvhtCQvKvwVKieTwgff/99xk/fjwPPfQQJ0+epGrVqtx///08//zzVp2nnnqK+Ph4RowYQXR0NJ07d2bRokUEBAR4ujkiIiKSC8Pmm72bG09stPJm755Nm2ptsr7p0CGYP99MjxqVn82TEs5mZD6othiIjY0lJCSEmJgYgoOzOEdXREREsmR70QZAzZCaHB592LrOzHjBDBPCXgvjXKLztlBG3BPm6vqePWHx4vxtsBQ7eYnXdJa9iIhIKfPCby9Y6Wrlst/A3r73aLqR7lr46afm68MPe6xtUjopIBURESlFNp/YzEurXrKuE1ISMAyD7nW6A/C/q//nVP/l1S8DkJTmfKwoANHRUK8e9O2bb+2V0kEBqYiISBH326HfrIVGlyrzsPvWqK3cMecOqwe0Xvl6TuXbT24HnFfcOxk5ErwUTsil0X9BIiIiRdjLq17mmq+uoc/0Pvn2HjN3zOTMhTMABPoGcl/L+6wyGzZS01PdD9kHBcE99+Rbu6T0UEAqIiJSRMUmxfLcb88BsOH4Bo88My09zW3+tqhtAAT4BPBUp6esfJvN5tQ72rB8g4ybhg6F0FCPtEtKNwWkIiIiRdT3O7/3+DOzPP7zPxUCK9CgQkbQWaVsFRJTE63rF/4yz6m/dY83PPmkx9snpZMCUhERkSLK8ThPyGKlex6dvXA22/LaobUBeLvn24DZSxuXHAeAn+HNHdO3cegjf2YM+wVq1brk9oiAAlIREZEiK3Nv5oWUC5f8zHfXmefO39viXpcyL5sXlYIqARASYJ66FJMUYwWk5S6Yw/21P/gG7x49L7ktInYKSEVERIqY0wmniYqLIjIu0ik/ISXhkp9tnyt6Iu4EM26c4VTWrHIzKx3sb25kHhkXSb8pXQAomwy8+CLcfPMlt0PEkcePDhUREZGLtzVyK20/bet2m6X4lHgqUemin+045J+SnsI1da5xKrf3hAIE+QYBsOnEpozycv4wfvxFv79IVtRDKiIiUoR8sumTLPf8vNQhe8ce1td7vE6QX5BTea3QjDmhQSmu95/xTgKb+yNGRS6FekhFRESKkMzD9I7cnpaUC+lGOl42L84nnbfyWkS0wJYpuPzkuk+sdJlZcy/qvUQuhnpIRUREihDHYXO7sMAwAJJS8x6Qrvt3HSGvhjB4zmDafdoOgBD/EJdgtHZobeqWr2tenDlD0BczMj9KJN8oIBURESlCsg1IL6KHdOB3A4lLjmPG9hkcjT0KQFm/slb5C11fAGBKvykZN73xBkHnst+vVMSTNGQvIiJShLgLSAN9zM3oL6aH1N0UgHL+5az0C11f4OG2D1OhTAUzIzERJk+mjJstTxtXbJzn9xfJDfWQioiIFCGnEk655AX4BAAXP4c0M8ceUpvNlhGMAixbBnFxBFWs6nRPlbJV+OHWHzzy/iKZKSAVEREpIn4/8jvHzx93ygv2D8bfxx/Iew/pzB0z3eY7BqQufvwRgIDrBjplH3/8OJdXujxP7y+SWwpIRUREioje3/R2yXus/WP4e/8XkOaxh/T22be7zS/nV85tPmlpVkBqG3hDnt5L5FIoIBURESki7Md22gX5BjG6/eiL6iHNbs/SLHtI162DkychJAS6ds31e4lcKgWkIiIiRUSd0DoAvHLNKxgvGMQ9E0doQOhF9ZCuPLwyy7Ise0j/6x2lb1/w9c31e4lcKgWkIiIiRcSRmCMAdKrZySn/YnpIX/vjtSzLsuwhnTfPfB04EEBzRqXAKCAVEREpAtKNdGuf0JohNZ3K8tJDeuL8CaZumMqKf1ZkWcdtQLpnD+zbZ/aM9jbnss66ZRb9GvRj/fD1ufwUIhdH+5CKiIgUAafiT5GclowNG9XKVXMqswLSXPSQtvmkDcfOH7Ou3+v9Ho8sesSpTuYz7IGM4fprroHgYMDsIV1wx4K8fAyRi6IeUhERkSJg+vbpAAT6BuLr7Tx/82ziWQCeX/E8hmFk+xzHYBRgVNtRTO0/lYWDF1p59o32ndiH6wcMyGPLRS6dAlIREZEiwH5CU0JKgkvZD7syNqTvO6Nvrp/ZvU53bDYbI64cQZeaXaz8QN9MAWlkpLnCHuD66/PQahHPUEAqIiJSBMQnm2fHP9ruUZeypzo+ZaUXHViU62cuO7TMSvt4ZczSs5/8ZPnpJzAMaNMGqjlPFxApCApIRUREigB7z6i7LZm61e6Wq2ekpKVkWeYYkLoM2dvnj2q4XgqJAlIREZEi4IP1HwBg4DpH1DGYBGDhQpc6AOcSzzld922QMbzvZcv4X75TD2lcHCxdaqYVkEohUUAqIiJSSJLTkmnzSRtsL9qsvG93fOtSL/MiJ/r2hc8/d6kXnRjtdD2572QrbbNlvIfTHNKFCyEpCerWhSZN8vgJRDxDAamIiEgh2XRiExuOb3DKG9tprEs9nz17XW++/3747TenrH9j/3W6jigb4fZ9m1VuZiYMA956y0zfeis4BK0iBUkBqYiISCF5dJHrAqb+Dfs7Z6Sm4vviy855gwZBairceCPsNYPV+OR4un/V3ala5sVLUU9EcfCRg1QKqmRmLFtmrq4PCIDRoy/ps4hcCm2MLyIiUgj+Pvs3fx37yyU/yDfTpvXffYfP4aPOedOmweHDsGYN9OsHa9Yw98Ripypv93wb0tLgwAG4cAEaN6ZyUGWwP/7sWRg2zEzfdx+Eh3vok4nknQJSERGRAhKfHE+3L7vRo04P6ofVB6BauWqUDyzPjpM7gEynKKWlwcsv45ue6UEBAebK+Hbt4O+/oVkzYh9qYxU/H3Ebj/0YBTdWN/cYBTPg7NgRWrUyT2N65RU4cgTq14eXM/XAihQwDdmLiIgUkFm7ZrHh+AZe/eNVa75n3wZ9WXbXMppWbsrDbR92XlE/fTrs3o132WDXh1WqBL/8Ag0aQFQUAfMyjvgM+OY7eO01MxgNCgJ/f4iKgrlzYfx46NQJfv4ZvL1h5kzrqFCRwqIeUhERkQLieOzn7tO7AagdWpvKQZXZ/uB258opKfB//wdA0rC7Ifl91wc2agQ7dsBXX+G1/G3AfKZ/pQi4ty/06AE33WQuXlq1CnbtguXLYf16s5f1pZfgyivz46OK5IkCUhERkQKy5/QeK/3dzu8AaFihofvKn38Ohw5BeDj+dwyBL8yA1MvmhWEYGds4+fnBffeR1soGP90HwPWfrob/pgRYrr3W/HnUdSGVSGHTkL2IiEgB+PXvX3n9z9dd8ssHlHetnJgI//ufmX7mGZrUasPjHR4HIN1IJz4l3uWWNCMNgHrl61nzU0WKCwWkIiIiBWDG9hlu84P93czf/OwzOHYMatQw9xsF3rj2DXy9zA3yz10453JLWroZkDaPaO6hFosUHAWkIiIi+SzdSOfY+WNuy8r5Zzq7Pi0tY7P6sWPNBUmYJy2FBoQCricyQUYPqbfN2yNtFilImkMqIiKl1tQNUzmffJ4nOj6Rb++Rlp5G8ynN2Xlqp9vy8KBM+3/OnWvOHa1QAe65x6nIvtF9clqy2/cB8PZSQCrFjwJSEREplZJSk3jg5wcAGHLFEMLL5s/G8AfPHXQKRo+NOUa6kU7bT9rSuWZnygc6zCE1DHO7JoCHHoIyZZyeFZMUYz3zyqoZq+MHzBzA/L3zAfWQSvGkgFREREqlUwmnrHS6kXnnec9JTU+10r5evlQtVxUwA1Nb5rPjf/wRNmwwA9FRo1yeFZsUC8CtP9yK0cSwnm8PRgEOnD3g6Y8gku80h1RERPLVphObuHPOnRw6d6iwm+Lk+PnjVjo/A9K45DgrXcY3o8fTJRhNSYFnnzXTo0dD5cq5ev6Pe350ut4Wte2i2ilSmNRDKiIi+erKj82h5XQjnRk3uV9pXhjafdrOSjv2Ynra6YTTuav4/vvmxvUVKsATuZ/TevOsm52uU9JT8tI8kSJBPaQiIlIg9p/dX9hNyJJ9hbqnJaYmcs+PGQuTbmx8o/uK69bB00+b6VdegfJu9ibNQpWyVZyu8zO4FskvCkhFRKRAHDx3kJu/v5n9Z/bz876f6TejHyfOnyiUtmQeorevUM/JoXOHqPdePd5Z806WdaLiovj1718xDIP/rfwfUfFRANQKqcW4zuNcbzh8GG65xRyyv/lmGD489x8E6Fq7a57qixRFCkhFRCTfOPbWnb1wltm7Z9Pwg4b0/7Y/v+z/hYcXPlwo7cq8sXxuexVf/+N1Dp47yJhfx7gt3xK5hdaftKbXN734Zts3vPL7K1bZlP5TaFChgfMNiYlw/fVw9Chcdhl88glknluaA3dbQIkUNwpIRUQk3ySmJmZbvjlycwG1BFLSMuZWnohz7pnN7ZB9kF9QlmXfbv+WllNb8m/svwBMWjfJOlkJoHm4mxOUnn4atm2DSpVg6VIIDc1VOxwpIJWSQAGpiIjkm5wCUseV7vlp35l9lH+tPE/8ai4W2nFyh1N5bntIq5WrZqUTUhKcyp5c8qTTdUJKAgbm1kx/3vsnVco5z/VkwQJ4910zPW0aVK+eqzZklpSa5HR9eaXLL+o5IoVJAamIiOSbnALSVlVaFUg7nvj1CeJT4nlrjXkk57KDy5zKczuH1PHc+aMxR53Kqgc7B5RnEs5Yga5LkPjvvzBkiJl+5BHo1y9X7+9O5h7SBbcvuOhniRSWfAlIjx07xp133kmFChUIDAykWbNmbNiwwSo3DIPnn3+eKlWqEBgYSI8ePdi/v+iuvhQRkYuTU0BaUMPN9hOOAKZtnsanmz91Ks9tD6nj0P6RmCPZPsNx4/2yfmUzCgwD7rsPoqOhTRt4441cvXdm+87sAyApzbmHtE75Ohf1PJHC5PGA9Ny5c3Tq1AlfX18WLlzIrl27eOuttyjvsIXF66+/znvvvceUKVNYt24dQUFB9OrVi8TE7P/iEhGR4iVzQNqkUhOn61zv0XmJfLwytt2+d/69AHjZvKxezdzOIXXsSXUMSL/d/i0bT2wEIDQg1Ome2qG1nc+X/+wzWLwYAgLg66/Bzy9Pn8Vuyd9LSE1PZdepXVbeY+0fu6hniRQ2jwekr732GjVq1GDatGm0bduWOnXq0LNnT+rVqweYvaOTJk3iueeeY8CAAVxxxRV89dVXHD9+nHnz5nm6OSIiUojsAWloQCjnxp6jZkhNp/IzCWes9NKDSxm7ZGy+7KPpGJDaBfoEEuRrLlLK7ZC943ZR9/10Hz/t/QmAO+bcYeVvGrHJ6Z6+9ftmXBw5AmP+W6E/YYK5sj4Pvhr4lZW22WxsOrHJOk506ZClvNbjtTw9T6So8HhAOn/+fFq3bs0tt9xC5cqVadmyJZ988olVfujQISIjI+nRo4eVFxISQrt27VizZo3bZyYlJREbG+v0IyIiRVu6kU6bT9oAUD6gPKEBobSMaOlU53zyeZLTkjmTcIZrv76W1/983eUozEuVlp7GwXMHXfLjU+KtnsuLGbIHuH7m9fT+prdTXu3Q2k7X1hC6YcCwYXD+PHTsaB4PmkfVgjMWVdmwEZ0YDcAV4VfQvW53fL19s7hTpGjzeEB68OBBPvroIxo0aMDixYt58MEHeeSRR/jyyy8BiIyMBCA8PNzpvvDwcKsss4kTJxISEmL91KhRw9PNFhERD3NcQX8o2jzHfnzX8TQPb86wlsPwspn/CzoVf4ohc4dYdT09r/Shnx/iwNkDLvkzb5qJt80MSL/Y+kWunuWuJ3Xx34ut9LQB01zOqA8LDDMTH39sbu0UEGCuqvf2Jq/s7bWz76ca4h+S52eJFCUeD0jT09Np1aoVr7zyCi1btmTEiBEMHz6cKVOmXPQzx40bR0xMjPVz9OjRnG8SEZFC9cCCB6y0n7c5TzLAJ4AtD2zh0+s/tQK1wXMGs/DAQquup4fsP970sUvegtsXcFvT26zh7q+2fsWx2GM5PiunuaZW8OmgVZVW5mlM9vPpJ06Ehg1z0XJXjlMPbDYb07dPB8zfq0hx5vGAtEqVKlx+ufP2Fo0bN+bIEXPyd0REBABRUVFOdaKioqyyzPz9/QkODnb6ERGRS/fDrh+YuWOmx553Pum8tS/m7tO7rfzxV413qVupTCUAVh5e6ZSfcPo4LF8O27d7rF2Zta3WFsA61hOg+jvVeeOP7Fe85zTX1Gk1/X9ahDeH+++HuDjo1Mnc5ukiOS6OsmGjYpmKgDn9QKQ483hA2qlTJ/bu3euUt2/fPmrVqgVAnTp1iIiIYNmyjD3gYmNjWbduHR06dPB0c0REJAvTt03nllm3cPvs21nxz4pLfl5CSgLBrwYT8HIAF1Iu0LhiYwCe7fIsz3Z51qV+5u2KrOc89zR07w5XXGGe7X7Adbg9L+wr6R03tQ8JMIe47dMG7J5a+lS2z8qph7RyUGUAagSbU8s+ue4TmD7dXFXv72+usPe6+P/1Zu4htfcm39joxot+pkhR4PGA9LHHHmPt2rW88sorHDhwgBkzZvDxxx8zcuRIwPwDNHr0aCZMmMD8+fPZvn07d911F1WrVmXgwIGebo6IiGThzrl3Wumrv7zaqWzi6omMX+7aq5mdv8/+baW/3Pql1WvXtHJTl3mVkPUw8/kAG9jXCsyeDS1bwvff56ktdifOn7CO8hzUdJCVb59CkHlOZk5y6iGNKGuO9K29by2zb57FvX8Hm72jAM8/n+dV9Zk5tnfTiU18ve1rwP0uAiLFiccD0jZt2jB37ly+/fZbmjZtyv/+9z8mTZrE4MGDrTpPPfUUDz/8MCNGjKBNmzbExcWxaNEiAgI0B0ZEpLAdiTnCM8ufYcLqCUTFReV8w3/ikuOs9OHow/wT/Q/gfhgb4PEOjztde/23o9LRh+40t0favh2uusoc6r7tNrjxRsjjGoLbfrjNSj/a7lHGdR7Hb3f/ZuU5BqmW1FRzRTxATIz5nunppO3dQ9r6dVm+18vlb6bivn/hxAmqTv6KG697Cq9bb4OEBOjTB558Mst7c8txyH7qxqlu80WKo3w5qal///5s376dxMREdu/ezfDhw53KbTYbL730EpGRkSQmJrJ06VIaXuQEbxERuTiOG7hfEX6FlXbc8D3zme/ZcZwL+t3O76yA1L7XZ2b3tLiH64OutK6/ONQcgL8TzB5NmjaFZcvgmWfMFelz50LjxvD22xkBYw5WH1ltpcMCw3il+yt0q93NypvUexJ3NLvD6Z5ttQMhNDTjp2ZN0n286fxGY16M/9mpbt99GelnHv3B7M2tWhXGjYNDhyAkxAxE580D30vfkimrHl31kEpxp7PsRURKobT0NGISM47TtM9F/GbbN3yyKWPv6Lvm3ZXrZzr2ptq3eQJoV72d2/q2N95g7lMbef1XWH2gC/X+710A/j6XMfSPjw+8/DJs3mwuCIqPh8cfN4NSN77b8R2XfXAZ26K2YWQKWsv4lnGpX8a3DJN6TXLKG98lFWJjzd5RAG9vltWBtZl2HKxTphovdHsBgIrpAdCtG9gX3bZpA59/DsePw+uvX/RpTJm5m/oACkil+NN/wSIipdCZC2cwyAjYklKTiE6MdtoPFJz3Es1Kcloy3b7oxpp/XQ83uaHRDW4DQf76C555Bi8DnrzqaZgwgagL5jGiR2OOkpSahL+Pf0b9Zs1g1SozuBs3Dp5+Gjp0MDeYdzBotjkEf++P9zL71tlWvg1blsFcUIrz9fxGwM6dZq9s5cpQrhwffN0Pjvxq1akTWoc9o/bg5+3H5siB5glUL4ZBejqcOwcVKmT3K/M4BaRS3KmHVESkFPp5n/PQc3JasrXJel7tOb3HbTAKEB4U7pqZkABDhkBaGgwaZO7L6e1N5aDK+Hj5YGBwKuGU631eXjB2rHlPaircfrt56pEbsUmxnIg7YV1PGzDNfePPniWwz3Uu2TF1q5kLkMqXJyrxDPMdglEwt4uyL4xqEdEiY/9RL68CD0ZBAakUfwpIRURKoed+e87pOjktmbMXzrrUc7fRe2bnk9wHhQAVyrgJzsaOhX37zLmWkydb2TabDX9vs1fUfiSmC5vNPPGodm1z4dOzrttJAew/u5/IOPP0v5YRLbm7xd2ulVJSoH9/bGtdFyrtPWNuX3ji/AnunX+vS/mEqye4b18hyetuASJFjQJSEZFSyD4U36NuDyDrgDQhJSHHZzmurs/MZWunn36CDz4w059/DmHOAa+917HZR82yDkrLlTODUjCftcbsnc08Z/SG724AnBdvOXnpJfPeENdjNzcc38DBcwep9nY1ftn/i5X/RIcn+O7m7xjdfrT7Z4rIRVFAKiJSyjgGmc91MXtKk9OSWfvvWpe6iamJpBvp2T7vfHJGD+nbPZ0XG/l6Oaws37QJ7v6vp3L0aOjVy+VZjhvVz9szL+s3vfZaGDrUXG0/bBjEx7PumPstmeqE1nHNXL3aXCwFMHUqz3Z5lvIB5a3iuXvmMnPHTKd5tgBv9HyDW5vcmuV81Pzm9Pt0YO8NFimuFJCKiJQyY5eMtdL1wuoBZkD6/Irn3dZPTE3M9nn2HtI+9fvwWIfHnMp8vHzMoHHSJGjf3lzw06YNvPqq22eduXDGSjuebw9wIeUC1359bcbxnm+9BeHhsHs33HEHW45vcvtMl+H6U6fMOayGYQbIt93GhGsmcPqp0wy5wlzUlZaexvaTzkeX3n/l/dn+HgpC/bD6bvNT0lPc5osUFwpIRURKEcMw+GD9B9a1fc5mdgGN4/ZQdvHJ8dz0/U3cPvt2aw6pfQP8YP9gq17VclXNwPGxx8w5mwMGwMKF5jGaOfh+5/ecjD9pXU/ZMIWlB5dmHO8ZFgZz5oC/Pwt3zWfKvOfcPqdLzS4ZF3FxMHAgHD4MdevCe+9ZRV42L65raC5wSklPYeaOmU7PGdlmZI5tzm9Z9czGJ+sseyneFJCKiJQijsPr3938nTVnMzvuVtB/s+0b5uyew8wdM619Q8v5lQNg7bC1NKzQkMH1b+TWV+dnnFA0YYK5uX0eVqHXfKcmnT7vxOHowxw8d9C1QseO8O239L0Ttvq73yXACuLOn4feveHPP80N7xcsyNg39D+BvoFmVTcLtezn1BdFTSs3LewmiFwSBaQiIqXIqXhzO6UyvmW4tcmt2Qakvev3BmB7lDl0vfKflVR5qwo/7PrBqefy6MHNAJTd/w98/jmNV+5k77k7+WbUcrxn/NfL+NRT5olLeZx7mZSWxJ9H/+T+BfezJWqL2zpnel3lklfNuzz3NrubjSM2mhlxcWYw+scfZjD666/mqU+Z2Odobo3a6lJWsUzFPLW9IDSq2IhPrvuEmy6/qbCbInJJtHGZiEgpkJqeytKDS63FL7VCagFkG5A2DW3IIhYRt3oZbCvPTdHPcMaI55ZZtzBmbxhcZtabc2oVAOUWLofly50f0qoVTJ0KrVtfUvsPnD1gHUXqKN1IZ/7e+U55t+yE72edg1orYEIPqHQKxoyBXbugfHlYsgSuvNLlWQC+3lkf71lUzov38fKxTtZqXLEx97W6r5BbJHLpFJCKiJQCUzdMZdTCUdZ1yyotgeyDrDIzZkFDSFi7Gn5ZzZn/yyiLiXfdIqpirUbQty5ER0NSEgwfbq6A98n9/2p61evF4r8Xu+RHJ0aTZqS55I9dMpY317zplJfWrCn8ec6cJzrE4eSpiAiYPz/LYBSyXsVelGx/cDuNJ5u9u+5+JyLFkYbsRURKgU83f+p0XSEw53mcZQ6bJx0lNKoHt97qVBbdo7NL/QqPPgM//2wOi2/YAPffn6dgFGD+7fNZOmSpS77j6nuA1YdXA7gEowDJ9WubG++//LI5XzUgAB56CLZtM1f4ZyNzD+m6+9bRuWZnFty+IE+fIz81qtjISue0A4JIcaGAVESkFKgZUtPpOquA9Lp6femQEMb8GVDGZgZnCR2uhO++c6p3upxrz2pIgOsG83nl5+1H97rdc6x31RdX8ffZv92WnU44DWXKmHNWT50yjyqdPBkqVcrV+9s1qdSEttXasvqe1fRr2C/3H6IAudsBQaQ4UkAqIlJCbT6xmc6fd2blPytJTkt2KnN7pCfQfuXf/Pn6Wa475EuZe819N7/f+b3LKUgrD68E4PmrMvYu7VC9gyebn6ONJza6PcP9qY5PZVzYbHlaSOU4ZF8+sHw2NYsGxy22RIozBaQiIiXUsPnD+OPoH3T7shsnzp9wKsuqhzR4215ziHvJEsq07mjlbzrhftP5wVcMJvLxSA4+cpBKQTn3QHrS/jP7rcU9ANc1vI4DDx/ghsY3XPQzHYfsNxzfcEnty08LBy+ka62ufNjvw8JuiohHKCAVESlh5uyew4frP3TatzPzNkb2E5oAnu70tJXucRBzVXzXrk7D147bPNn5e/vTsEJDwsuGU6e8m+M5L4H9SNNs6/zmXKdBWAOnz3UxvG0ZUxFyOjK1MPWu35sVQ1dkeXKTSHGjVfYiIiXIyfiT3PR91ntS7n94P3tO76FN1YzFPYnr/7TSde4fC3fdBeB0jvuc3XNcnlXGt4wnmuzWgEYDmLB6Qq7rD2s5jPFdx1/y+zouEvr5jp8v+XkikjsKSEVESpDwN8OzLHun1zvUD6vv3Ku2di2pq1dBO/PS/38TrSLHeaOZV+kDnEt0fzKSJ+TmBClHH1/3MV62Sx/0u7zS5XSs0ZFq5arRo26PS36eiOSOhuxFREoId8Pqjvo1yLRSPD0dRo92znNYAOTYQ+pOlbJV8tK8PHFchHXwEecjQzvXdN1yyhPBKJj7sv5x7x98f8v3HnmeiOSOAlIRkRLi2WXPZltetVxV54xvv4V16zB83Q+WdanZJdvnvdbjtTy1Ly/CgzJ6esPLZqS/velbrSwXKYEUkIqIlBC7Tu+y0muHraVdtXZO5UF+QRkX58/D2LEAGK3dn1xUpZxrD+jGERvx9/bn3hb3MqT5EDd3eUaNkBosGryI9cPXU8a3DEuGLGHl0JUMajqI13u87lS3T/0++dYOESkYmkMqIlJC1A6tzZ9H/+Ttnm/Trno71t63lipvVbHOr3fywgtw7BjUrQvNW8DmdTk+39vmTasqrUh8rmBOB+pVv5eVdpzP2aRyE6d6WnwkUvyph1REpAT4/cjv/HnUXC3v7+Nv5beIaAFkmmO5ahVMmmSmJ0/m5ma3AVArpJbLc2fdMguAK8KvYP/D+z3fcA+w5WHjexEpmtRDKiJSzLX/tD3rjmX0cAb4BFjpyX0n88yyZ3ii4xNmRnQ0DBkChgFDh0Lv3lwNbL5/M3VCXfcSvfnymzFeyH5xU2Hw9fIlJT2lsJshIh6iHlIRkUKwLWobthdt2F60cfbCWaey80nneX/d+y6nK7lz4vwJp2AUzA3r7eqWr8vMm2fSumpriIuD66+HI0fMofr33rPqtYho4ZGz6AtKXreFEpGiTQGpiEgBS0hJoPmU5tb1L/t/cSofNn8Yjyx6hKE/Ds3xWQ/8/IBLnuOQvSU2Fvr0gdWrITgYZs+GcuXy3PaiwrEXWESKPwWkIiIF7O01bztde9u82XVqF4ZhkJyWzKxd5rzNX//+Ncdnzd873yXP6QSl5GT48ENo2BB+/x1CQuDXX6FFi0v6DIXty4FfYsPG4x0eL+ymiIgHaA6piEgB23lqp9P10B+HkpyWzNs936Z73e5Wfu3Q2tk+JzktGS+bF+lGOpWDKlsb419V6yqzwvHj0L8/bN5sXtetC999B61be+yzFJZ+Dftx8smThAWGFXZTRMQDFJCKiBSwzNsw2U8lGvPrGO6/8n4r390iI0f3/HgP6UY6AEuHLOXY+WN0rtmZsn5lzSH5kSMhKgoqVICXXoL77gO/kjP3smKZioXdBBHxEAWkIiIFyDAMtkdtB8yh9YSUBKusRnANpm6cal1HJ0Zn+6wZ22dY6WrB1WgW3gwiI2HUUDMgBbj8cvjpJ7N3VESkiNIcUhGRAmIYBoPnDObMhTN42bwo5+e8qOho7FGn682RmzmTcMa6Tk5L5ljsMQBSUpOd6pa/4XZo2tQMPGfPBm9vePZZ2LRJwaiIFHkKSEVECoBhGLyw4gW+3fEtADVDavLGtW+4rRvoE2ilH/rlISt9/4L7qf5OdWwv2visn3msp28apL0ItsW/ws6dcOECtGwJ69fDhAng72bFvYhIEaMhexGRAtD/2/5O2zvVCqnFnVfcSWxSLKMXjyY1PdUqqx5cnf1nzVORvt/5PYOaDKJimYp8seULq86DHc29S1O8watrN7juOmjeHCIizGF6nV4kIsWIAlIRkQKQea/RlhEtsdlsjGw7kjbV2tDu03ZWWYMKDehaqyufbv4UgBu/vzH7h//2m8fbKyJSkDRkLyKSz84nnXfJqx9W30q3qdrGqaxbrW58fN3H1C2f89xPbXskIiWBAlIRkXy28cRGwFxF/8o1r3BNnWu4t+W9VrnNZqN3/d7WdZ3ydbAZBptThrk8q3q56lx/2fXW9br71rnUEREpbjRkLyKSzzYc3wBAm2ptGNdlHOO6jHOpE58cb6XDfUKgf3+CFy6E/3Ou9+n1n9KuejveW/ceI64cQUTZiPxsuohIgVBAKiKSz+wb4dcrXy/LOo5D7x1HTICVq6BMGb4KuY13Arfg7eXNs12epVf9XgA83/X5/G20iEgBUkAqIpLP7L2fQb5BWdZ5pfsrLD6wmFF/h+G9chUEB8MvvzCkUyeGFFRDRUQKiQJSEZF8Fp9iBqRlfMtkWefyaF+iP6uE/z9HITQUFi+Gtm0LqIUiIoVLi5pERPKZPSAN8suih3T3buja1QxG69eHP/5QMCoipYp6SEVE8lFKWgpzds8Bshiy37kTrrkGTp6EZs1g6VKoXLmAWykiUrjUQyoiko/2nN5jpTvX7OxcuGMHXH21GYy2bGlucK9gVERKIQWkIiL5yL7CvkJgBeqFOayyP3MG+vaFU6egVSuzZ7RChUJqpYhI4VJAKiLiIQfOHuDar69l6cGlVl5UfBQALSJaZFRMT4chQ+DoUWjQwAxGw3TikoiUXppDKiLiAWcSztDg/QYArPhnBSnjU4CMHlKnDexfegkWLoSAAPjhByhfvsDbKyJSlCggFRHJg5jEGI6fP07jSo2tvLjkOJ5b/px1nZqeymOLHqNZeDM+3fQpAFXKVjELv/kGXnzRTH/4IVxxRYG1XUSkqFJAKiKSB0N/HMq8PfNYNHgRPev15LU/XmPcMtejQCetm+R0fXuz22H5crj3vzPsn3wS7rmnAFosIlL0KSAVEcmDeXvmAfDqH68SEhDiNhjNLMg3iFZHUuD66yElBW6+GV59NZ9bKiJSfOT7oqZXX30Vm83G6NGjrbzExERGjhxJhQoVKFu2LDfddBNRUVH53RQRkUsSmxRrpZPTkunwWQen8ic6PMFlFS5zue/ReoPNFfXx8dCjhzls76U1pSIidvn6N+L69euZOnUqV2SaI/XYY4/x008/MWvWLFauXMnx48e58cYb87MpIiIuft73M12/6MrfZ//OVf2tkVut9P4z+61022ptmdJvCm/0fAMvW8Zfq4+3foQ+toY8OGYGnD0L7drB3Lng7++5DyEiUgLYDMMw8uPBcXFxtGrVig8//JAJEybQokULJk2aRExMDJUqVWLGjBncfPPNAOzZs4fGjRuzZs0a2rdvn+OzY2NjCQkJISYmhuDg4PxovoiUArYXbQC0qdqGv4b/lWW9hJQEgl5xf+xnWGAYZ546Y13/efRPrv/2el7y68VDr/8GJ06YBW3awC+/QMWKnvsAIiJFWF7itXybQzpy5Ej69etHjx49mDBhgpW/ceNGUlJS6NGjh5XXqFEjatasmWVAmpSURFJSknUdGxvrUkdEJC/+jf3XSq8/vt6lPN1I5/ud33Ms9hiXV7o8y+f8fMfPZiIlBRYsoOMXX3D6t2Q4P8PMr10bXn4ZBg3SML2ISBbyJSCdOXMmmzZtYv1617/kIyMj8fPzIzQ01Ck/PDycyMhIt8+bOHEiL9q3SRER8QD7dkx207dNZ0CjAZT1KwvAB399wKOLHs32GfXK16N9TDn44Gn44gtwnAtfqRI88ww8+KCG6EVEcuDxf64fPXqURx99lOnTpxMQEOCRZ44bN46YmBjr5+jRox55roiUPKnpqUzdMJWf9/3slJ+Wnsats26l/aftWfnPSl5c6fyP3Dvn3smgHwZZ1+6C0ZFtRmI8n85LjUfSiZqsmO4LTZvCa6+ZwWh4OIwdCxs3mkP1o0crGBURyQWP95Bu3LiRkydP0qpVKysvLS2NVatW8cEHH7B48WKSk5OJjo526iWNiooiIiLCzRPB398ff/2lLlJsxCbFEpccR9VyVQv8vVtNbcX2k9sBuKfFPQxvNZznfnuObrW6MWvXLAC6fdnN7b0/7zeD2LT0NLxsXqQb6U7lrRdtg1H1GH/oEOPtmb6+0KcPDB0K/fub1yIikiceD0i7d+/O9u3bnfLuueceGjVqxNixY6lRowa+vr4sW7aMm266CYC9e/dy5MgROnTo4O6RIlLMdJnWhW1R2zg25liBBqWLDiyyglGAaVumMW3LNACWH1ru9p6ral3FqsOrrOslBxZzcv1K0o10vNJh1TToPMwsu+ar1RCDeeRnz54wcKD5o6M/RUQuiccD0nLlytG0aVOnvKCgICpUqGDlDxs2jDFjxhAWFkZwcDAPP/wwHTp0yNUKexEpeqZvm86dc+/k4/4fM7TFULZFbQPgxz0/8mCbBwFYenApDcIaUCu0VrbP2hK5hQ/++oAXu71IteBqeWrH/Qvuz1P9CVdPoEVEC6eAtOf03lb68lPQIC0EMwqFyvePgauugW7dIMj9qnsREcm7Qjmp6Z133sHLy4ubbrqJpKQkevXqxYcfflgYTRGRSxSXHMedc+8EYMSCERyNzZjjnZiaCMCKf1Zw7dfX4uPlQ8r4lGyf1/rj1qQZaXy2+TOMF/K2K92RmCMADG42mCc7PkmLqS1c6jzW/jFaV23NbU1uw9vLmz2ndmf5vJRa1an8z0Fm7PkBP28/Ai6/KU/tERGR3CmQgHTFihVO1wEBAUyePJnJkycXxNuLSD5JS0+j6YfOIyL/W/U/K30q4RQAP+39CTAXHGXl39h/CfINIs1Is/LOXThH+cDcDYenpWfc93avt6kcVBnjBYPtUdu5YkrG4Rxv9XwLm83cf5SVK2k47mlaXgGbq7g+06tsOfD1Nc+hFxGRfKNN8UTkop1OOM3hmMNZlu89sxeAs4lns33OntN7qPFODcJeD3PKj0uOy3VbHI/1DPEPsdLNwpuxdMhSRrYZSfJzyWYwumkT9O4N3brhtWYt6792vyPIh/00ciMiUhAUkIrIRTtw9kC25XN2z+FMwhnOXsgISDMfDjdn9xwaT27s9n77kH9OTsWfcgpm/X2cd+XoXrc7H/T9AN9/j8PgwXDllbB4Mfj4wIMP4r3f+ejQcn7lqB1am441Oubq/UVE5NIUyhxSESneDMPggQUP8PGmj3Osu/v0bqeANDkt2QoYk1KTuOn7rOdlOgakvx36jbvn3c1LV7/E0BZDneq9vPplK92tdreMgrg4szd03TrzZ8ECsJ/6dscd8NJLUK+e07PK+ZVj/8P78ffxx8/bL8fPJyIil049pCKSZyv+WeEUjFYqU4nU8am8fM3L9G/YnyVDllA/rD4AX239it+P/G7VdRyGf2zxY9m+z4X778X45htISODmWTdzNPYo9/x4D48sfMSpnuPRn1ObjoP//Q86dYLQUOjaFZ56CmbPNoPRq682N66fPt0pGP1iwBeU8S3DD7f+QHjZcEIDQi/mVyMiIhfBZmQePysGYmNjCQkJISYmhuDg4MJujkip88CCB5i6cap1fUOjG5hz2xynOm0+acOG4xtc7v3n0X+oEVydJd9N5Po9z5PsZf4VNH023LYDvAzw+j+z7l1bYEFDGLzbh/evdF4QtTHtPlpdfQeHy6ZR+5drAfhjVQM6Lt/v/IbVq0O7dtC2LXTpAu3bg31RUyZp6Wl4e3nn+vcgIiJZy0u8piF7EcmT+XvnOwWjABO7T3Spl5LmfnunuIO7WfzKAPo222qN0Sw61Ztez9wNjRpB5crwibn/6FctzPLMwSjA0NOfsu2aT+k9Eqhk5tXcsB+8vODaa+Gmm8zN62tlv++pIwWjIiKFQwGpiOTJgJkDrHTrqq2pWKYiDSs0dKl3T4t7GL14tEv+dV/14VAz57zGL0+FkJrWdfvq7Vn779ps27E9HNIqhnE66Bxg9rJWf/9L8xjPSpVy/4FERKTQaQ6piORafHK8lS7nV471w9ezcPDCjH09HTzQ+gG3zzjkZlvRzMeLPtru0SzbkPBMgpUe+nFfTpcxg9GNIzbCXXcpGBURKYYUkIpIrkXFR1np2HGx2dR03XopOz5ezoM17au7P0b41e6vEugbaF1/s+0bK31Zhcty/X4iIlK0aMheRHItKdXcMiksMCyHmsCyZXQ5HcTqivHZVutep7tLXkTZCKfr3+/5nWPnj3Frk1uzfE6Qn86WFxEprtRDKiK5lpRmBqT+3tn0fhoGvPoq9OjBwqnxfLWoDGeqvcctl99iVelepzsxT8fwfp/3+aDvBy6PCPAJoFe9XgDMumUWnWp2cgpG3+39rlP9I6OPXMrHEhGRQqYeUpFSalvUNiLKRlA5qHKu77H3kGY5HJ+SAiNHwiefABB0930MefllqFyZ0J+2W9VuufwWgv2DGdV2VJbvtejORVmWPdLuER5dZM4ztWGjRkiNXH8GEREpehSQipRCe0/vpfmU5njbvEl93nVLpayciDsB4P4EoxMnYNAgWLXK3Odz0iR4JGMD+9d6vMa6Y+sIDQjlvlb3XepHsGQe3hcRkeJHAalIKbTxxEYA0ow0jsYcxcBg0tpJRMZF8lG/jwgJCHG553zSeW747gbAebU9YPaM9u4N27ZBuXLw9dcwYIBTlfKB5dn6wFaPfYYO1Tuw5t813HnFnR57poiIFA4FpCKlUJWyVaz0l1u/ZP3x9czfOx+AwzGH+ePeP1zu+XHvj1b62PljzoVvvGEGoxUrwh9/QEPXfUk9bd6geSzYt4DbmtyW7+8lIiL5SwGpSClkkHFi8OmE0/z696/W9aYTm1zrGwZD5g5x/7B9++Cll8z0O+8USDAKUDmoMve2vLdA3ktERPKXVtmLlEKp6RnzRn/Z/wuJqYnWddtqbQGIjIvk3h/vZf2x9dw7P4vALz0dRoyApCTo1QsGD87XdouISMmkHlKRUigtPc1K7z+736ls1eFVvLv2XebsmcOqw6uYtmWay/13Nb/LTHzyCaxcCWXKwEcfmYuZRERE8kgBqUgp5NhD6o67M+jBXClfr3w9etXvBQcPwuOPmwUTJkCdOh5upYiIlBYKSEVKoTQjLedKmYQGhPJUp6fMi/R0GDoU4uPhqqvg0azPnhcREcmJ5pCKlEKZe0ht2Ng3al+294QHhWdcTJoEq1dDUBBMmwZe+qtEREQunnpIpcSKioti75m9lA8oT5PKTfCyKWiyswek4UHhbHlgCxFlI4iMi8z2nvCy/wWkW7fCM8+Y6bffhrp187OpIiJSCuj/0FIiLdy/kIi3Iuj6RVeumHIF3i958+rvr5JupBd204oE+6KmK8KvsE46KutX1qXekx2ftNL1y9eH6Gi49VZzVX3fvjB8eIG0V0RESjYFpFLinE44Td8ZfV3yxy0bxwd/fXBJzz6TcIZ/Y//NstwwDHad2pXjoqHCZm+ft5e3lVfGt4xLvaEthlrp1oF1oVMnc9/R6tXhyy+1ql5ERDxCAamUKDtP7qTWpFpZls/cMfOinz1vzzwqvlGRGu/UYNbOWS7lu07tYtLaSTT5sAlv/PHGRb9PQbAHpD5eGbN2Mk9pCPYPpm75jOH4ys+/Drt2QbVq8Msv5qlMIiIiHqCAVEoEwzDYd2YfTT9qSkJKAgD9G/bHeMHggSsfsOpFxUfl+dnHYo8xdslY6xx3gFt/uJXYpFie/PVJbvvhNmbtnEWTD5sw5tcxADyz/BmiE6Mv7UPlI/sqe8eA1FHz8OZEj40mIC6RN0+3Yuhm6LsxFpo3hzVroFmzgmyuiIiUcFrUJCVC52md+fPon055H/Qxh+fvan4XUzZOAeDguYOkpac5DVVnZ/OJzbT6uJXbsp/2/sSba94E4Pud37uUXzXtKhbcsYCaITVz/TlykpKWgo+XD7ZLHCq3huxt7n8Pver1xDZ7Njz6KI8fP26uoh87Fl54Afz9L+m9RUREMlMPqRRrhmHwwIIHXILR0IBQaoWaQ/cdanTg1zszzmr/ZNMnpKSl5Or5N31/U5Zld869M9t7t5/cTq1JtUh9/DH49ltYuBBWrYKdOyEt7/uALj6wGL8Jfgz8biApaSms+3fdRc9VjU+OB1znja4auor76t/G2Pc3wy23wPHj0KAB/P47vPKKglEREckX6iGVYu2tNW8xdeNUl/x+Dfo5XV9b71rCAsM4e+EsD/78IO/OGcvmWWEEnI0150JWrQpVq/JlrXOkBPhxT/lr8KpVm0PRhy65jd8vmcQdb2fKrFgRBg40g76rrwZf3xyf8/yK5wGYv3c+t8++ndm7Z/Ncl+f43zX/s/L9vP3oXb93js86nXAagPIB5TMyk5Pp8tUKukycDxcugJ8fPP00jBsHAQG5+qwiIiIXQz2kUiylG+k8teQpnlzypNvyB1s/6Jxx6hR3RmVs7L7HP5bbr/wH4+xZc9X4ihVEz5nBUP+FDDd+xOfso9RdPsCqP3A3NDoFu34I5/8OOS+amlj+FhqkhrD4j7psmgJnX4UbdmeUH+nZjuSrOjHhtirsbFMLypaF06fh00+hVy9o3BhmzTJPP8rGyfiTVnr27tkATFg9AYDYpFgGzBxAn+l9iEuOy/Y5AK//+ToA5QP/C0h//x3atIHnnzeD0W7dzP1GX3xRwaiIiOQ7BaRSLH2y8RPe+DPrleydanbKuDh6FFq2pPGq3U515jWGN2aPgRUrYMYM9v3fw07l/zh0Hs79qQy7J0PjHVGM/+owTf6LDdsfhbGPzmLfhBh6LjlIy9M+lB84iDkjV1n3GgMGMPnVmxjf+ARN+x3m0MGNsHQpPPCA2VP699/m3p4NGsBTT5kBcibnk87zT/Q/bj9rWnoap+JPWdcr/lmR5e/Fzj5UXzYxHe68E7p0gW3boEIFmD4dli+HRo1yfI6IiIgnKCCVYmnJwSVO13tG7rHSV9W6KqMgLg6uvx6OHeOuuHouzxm7/W3o2hVuv539fdq5fa//6/p/5nNOnoQ1a/D6+ht2hD6D8WdP1iyrja1zZxgzBmbOhH//NeeLdunCuM7jAPgn+h9r9T1A3Q8vY3vTyvDRR3DokLlQqGxZOHgQ3njD7DEdOtQMVIFhPw4j+NXgLH8X7657lzMXzljXC/YtAGDfmX1OgSqpqXDqFEZUlDX39JZhb5kBqM1mbnK/ezfccYf2FxURkQJlMwzDKOxG5FVsbCwhISHExMQQHJz1/6il5DkcfZg+0/uw+7TZ23lt3Wt5uO3DXHfZdTy44EG+2PoFp588TZBfkDkEfuON8OOPUKkS/PUXG/3O0PqT1k7PNF4w/wi88NsLvLTqJZf33PbANpqF532bow/++oCHFz6cbZ0Xur7AC11fwBYfD4sWwRdfwM8/M7sx/F3BxuiK/fFv8ZNVv3319qz9d63Lc1pEtGBL5JYs3+eBveVISjjP4nrwzRy4ZqiZH/8ylLmyPbz/PrRuneX9IiIieZWXeE0BqRQbx2KPcesPtzqtqI8eG01IQIj7G8aOhddfN1eGL18OHTsSnRhN+dfKO1X75Y5f8LJ50Xu6uRiod/3etAhvwb6z+4hNimXh4IVZ7teZna+3fs1d8+7KsV7/hv15pO0jPLX0Kb4a+BVND1/Aa6H73trhRite+bs2KTu2sTf9JFffGJvndtWMhiOhUDYJzjMOJkwwt3USERHxIAWkUuIkpCRQ9a2qxCTFOOXbezddfPYZ3HefmZ4+3RyG/s+YxWN4Z+07Wb7XvNvmMaDRgCzLc2tb1DaaT2luXU/tP5UuNbtw+YeXZ3vf6SdPU/EN96cgfTwfhm8y0/G+cPlIM7i8GHVD6vD36IMXd7OIiEgO8hKvqVtEiqwjMUc4n3SetPQ0Fuxb4BKMbntgm/sbv/sORoww0+PHOwWjAG9c+wYDGw3M8n271u56Kc22XBF+hdP1dQ2vo3GlxqQ9n8aekXsI8Xffs/vNtm9c8kZHDOS1lG4Maz0c/vc/WLiQoE3bOfDIfia0esKqN6zhICs9ss1IpvSbQmhAqNv3ORx75CI+lYiIiOdpH1IpcgzDoNc3vayFS+FB4U5Hfq6+ZzWda3Z2f/NPP5mrxtPTzUU6L77oUsXby5u5t83l1d9fZdyycU5lzSo3yzKAuxgtI1qyOXIzAFXKVQHMM+Mvq3gZ+x/eT+U3K7vcs+jvRU7X3et055275rp9vi/wTO3XOWScIzQglAnXTKDB2hbc2uRW6pSvA8CdV9zJyfiTVA6qzKOLHuWzzZ8B0KVWF099TBERkUuiIXspcvaf2U/DDxq6LXu609NM7DHR/Y1Ll0K/fpCcDIMHw5dfgnfWR4T+ffZv2nzShnOJ56y8w6MPe/Soz0E/DOK7nd8B7qcXfLX1K+6ed3e2z0h7Pg0vm2cGMwzD4Ld/fmPG9hm80v0VKge5BsQiIiKeoCF7KdZG/jLSbf41da6xTiVy8fvvMGCAGYzecIO5Wj2bYBSgXlg9Tj91mvf7vE94UDjL7lrm0WAUzOkBfer34Zc7fnFbXiskY5P9ZpVdV/Lf0+IejwWjADabjWvqXMOn13+qYFRERIoM9ZBKkWN7MWMPzBsa3cDcPXP539X/47mrnnN/w/r10L07nD8PvXvDvHnF5sz1f6L/oc675tD6B30+YNTCUVZZ1BNRChpFRKTYUg+pFGt96vcB4MO+HzLntjkYLxhZB6MbN5rHb54/bx53OWdOsQlGAaoHV6dSmUqU9SvLsFbDCPAxj+lsV62dglERESk1tKhJipw0Iw2Acv7lsq+4eDHcfLN5ilL79jB/PgQGFkALPcfHy4c9o8xTpgJ8Atg7ai9vr3mbsZ3GFnLLRERECo4CUilyktOSAfD18nVfIT0dJk6E55830927mz2j5XIIYIuosMAwK10zpCaTek8qvMaIiIgUAg3ZS5FjD0j9vP1cC9esgXbt4LnnzGD03nvhl19Ac4lFRESKLQWkctEMwyDdSM+yfM3RNQz7cRg7T+7M03NT0lIA8PV26CE9fhzuugs6doQNG8ze0M8+M3/83ASuIiIiUmwoIJWL1uPrHni/5M3vR353KUtLT6Pj5x35fMvnNP2oKVsjt7L80HLS0tNc6qYb6VYQCpl6SM+fh5deggYN4OuvwWYze0X37TNfRUREpNjTHFK5KIZhsPzQcgC6TOtC2vNpxCfH0//b/lQtV5X65es71W8xtQUAg5oO4tubvrXy31v3Ho8uehSAPSP3cFnFy9gatRUA3x/mwBt3wJkzZuWOHeHdd6F163z+dCIiIlKQFJDKRTkZf9Lp+o0/3uDpZU/neN/MHTMZ1GQQAxoNYMKqCYz/bbxV1mhyIwbEVoX/poNe+GwqnMHsHZ0wAW65xewhFRERkRJFG+PLRXHcvD47a4etpf1n7V3ye/pcxq+pe7O99+RX4VR6biIMGQI++reTiIhIcaKN8SVfHY4+nKt6r3Z/lXbV23Hkvp08UrY7q//uapU5BqOzfq9KkOG8xdMLZftTadvfcM89CkZFRERKOAWk4iIlLcVaWOTOF1u+sNKp41OdzmCfNmAaNza+kVe7T2SsVxe4915qNGzDu08so/PXK6lzzvlZFf3Kc/Ov/xL3f8l8et2nVv7jo2ZAUJDHPpOIiIgUXR4PSCdOnEibNm0oV64clStXZuDAgezd6zw0m5iYyMiRI6lQoQJly5blpptuIioqytNNkYtwPuk8Qa8E4T/Bn082fuK2zvHzxwG4ps41eHt5s+3BbawauoqDjxxkaINbmH28C2Pv/xo6dYJp0yAhARo3hv/7P5ZeN4txHZ6ynvXc1S9Y80JvaXILNza+kY/7f5zzKU0iIiJSYnh8Dmnv3r0ZNGgQbdq0ITU1lWeeeYYdO3awa9cugv7r8XrwwQf5+eef+eKLLwgJCWHUqFF4eXnxxx9/5Oo9NIc0//x26Deu+eoa63rOrXPoVLMTIf4h+Pv4s+/MPi774DIApt84nTua3WFWTE2FL74wT086ccLMCwyE226D4cOhQwenBUlxyXFsOL6BrrW6YtNCJRERkRInL/Favi9qOnXqFJUrV2blypVcddVVxMTEUKlSJWbMmMHNN98MwJ49e2jcuDFr1qyhfXvXBTCZKSD1PMMweHHli8zcMZO9Z1wXG/Wu35t5t80j4OUAK+/4mONUKVcFliyBRx6BPeaZ7NSpA08+CXfcASEhBfURREREpAgpUouaYmJiAAgLM8/r3rhxIykpKfTo0cOq06hRI2rWrMmaNWvcPiMpKYnY2FinH/GsX/b/wosrX7SC0U41OjmVLzqwyCkYrRNahypJvubpST17msFohQrw1luwezc8+KCCUREREcmVfA1I09PTGT16NJ06daJp06YAREZG4ufnR2hoqFPd8PBwIiMj3T5n4sSJhISEWD81atTIz2aXKulGOu+seYf+3/Z3yv/u5u/Ycv8WetTt4fa+JX7DoFGjjNOTHnkE/v4bxowBf/+CaLqIiIiUEPkakI4cOZIdO3Ywc+bMS3rOuHHjiImJsX6OHj3qoRYWf6+sfoX+M/qz93T2e3pm5YstXzDm1zFOebNvnU214Go0j2jOvNvmcWWVK53fc0tF6j30nHmC0hVXwNq15glK6hEVERGRi5BvAemoUaNYsGABv/32G9WrV7fyIyIiSE5OJjo62ql+VFQUERERbp/l7+9PcHCw009pZxgG7T5tx7PLn+Xn/T/TaHIjhs4bSrqRnutnbIncwrD5w6zrSb0mYbxgcGPjG628IL8gvr9hBteWaWrlNdl9GipWhEmTYMMGaNvWI59JRERESiePB6SGYTBq1Cjmzp3L8uXLqVOnjlP5lVdeia+vL8uWLbPy9u7dy5EjR+jQoYOnm1Nizd87n7+O/eWU9+XWL9l0YlO29xmGwet/vM5V066ix1cZw/FlfMvwaPtHnSvHxcHkydRt24tfn9rBzskwbaE//Qc9DwcPwqOPgq8vIiIiIpfC40fgjBw5khkzZvDjjz9Srlw5a15oSEgIgYGBhISEMGzYMMaMGUNYWBjBwcE8/PDDdOjQIVcr7MX08aaP3eanpKW4zTcMg+0nt7P+2HrGLh3rVHZ709uZfuN08+LECfj9d1iwAGbPhvh4M79SJS5/5BEuf+gh+G+BmoiIiIgneDwg/eijjwDo1q2bU/60adMYOnQoAO+88w5eXl7cdNNNJCUl0atXLz788ENPN6XEOn7+OL/s/wWAn27/iW61u1FuormRfHxKvNt7Rv0yig83uP8dvxDVCNvdd8Mff5g9n47q14fRo80jPMuU8dhnEBEREbHzeECam21NAwICmDx5MpMnT/b025d4n2z8hBELRgBQr3w9+jc0V8e3q9aOdcfWEZ/sHJBujdzK6YTTWQajAOWfegHst9ls5kKlrl1h0CBo395pQ3sRERERT/N4QCr5Z9GBRVYwCjD+qvFWOsjPPAVr5s6Z7D69myc6PkFyWjIdP+9IQkqCy7NWTINu90DYBQhr2xU6X2Ue9dm+vVbLi4iISIFSQJpLCSkJlPEtnCHrLZFbaDm1pUv+bU1vs9K1QmoBMHPHTGbumElSQizldh90CkZv2A2D9wcQ1rgVXR+7lT2tauHbuAk+FRvk/4cQERERyUK+Hx2aHwry6FDDMBi3bByv//E6X9/wNYOvGJzjPWnpacQlxxEScOk9jfHJ8ZSdWNYpr0JgBfaM2kPFMhWtvCV/L6HnNz2zfM6tZyL4psMb+A68yTxjXkRERCQfFamjQ4u7C6kXeO2P1zAw+GD9BznWT0hJwOd/PoS+Fkr3r7pz3bfXcTTm4jfy/3Hvj07Xb/d8m9NPnXYKRklL49o1UWz+pSYPrHfzjGs/57v3TuB7+50KRkVERKTIUUCagzK+ZVgzbA0Aa/9dS7OPmrHq8Kos6w+ZO8RKLz+0nAX7Frhss5TV1kyOTpw/QYspLRg8x+yRvbHxjRgvGDzW4bGMSmlpMHMmNG0KQ4bQ4q8jTFrr3Cs7otUIruswNMf3ExERESksmkOaC00rZ5xStOPkDh5b/BgbR2y08v48+ic/7PqBNlXbMGf3HJf7j8QcITktGT9vPx5b9BifbfqUVT2/pcWV/bJcwf7mn2+yNWqrdT20+dCMwrg4+O47eOcd2LnTzAsLgyefxH/UKOL8bHy741tiEmMY02EMNq2SFxERkSJMc0hzqcLrFTh74SwAfer3oXPNzjy7/Fm3dQdcNoCXr3mZph81dVtud+HjygRc2Q5q14aICPM4zooV2RIQTcv1GUd67o94hfrHLsChQ+bP1q1mUAoQGgqPPw6PPAI6UlVERESKiLzEawpIc2lL5BZu+v4mDp47SJuqbVh/3M1kzf/seHAHTSo3Yfau2dw86+Ys6119CJZ/mXG9rhqsrwbL68Dcxmbemk+h/b9ubq5fH4YPhxEjzKBUREREpAhRQJpPpm+bzp1z73RbFugTyIXUC9zX8j4+uf4TwJwr6jfBL9tn3urfijvO1yboXDzXhi92Kmtz3Ma6FfWx1a4Ddf77qV0bGjSAli21Yb2IiIgUWXmJ1zSHNA8uq3iZ0/XjHR7nzZ5vWtdnEs5QPrC8de3r7UvcuDhmbJ/BNXWuYdepXXSp1YXIuEgaTza7QL9P2sT3fpsg3PX9vnllD7YKDfPnw4iIiIgUEeohzaMG7zfgwNkDZjuejqWcf7mLes69P97LtC3TsixvW60t6+5bd1HPFhERESls6iHNR0uGLOGTjZ/wUJuHLjoYBZjSfwpl/cry/l/vO+V/NfArvGxe3NHsjkttqoiIiEixoB7SQpaQksDmE5u5rOJlBPsH4+ed/ZxTERERkeJAPaTFSBnfMnSq2amwmyEiIiJSaHRSk4iIiIgUKgWkIiIiIlKoFJCKiIiISKFSQCoiIiIihUoBqYiIiIgUKgWkIiIiIlKoFJCKiIiISKFSQCoiIiIihUoBqYiIiIgUKgWkIiIiIlKoFJCKiIiISKFSQCoiIiIihUoBqYiIiIgUKgWkIiIiIlKoFJCKiIiISKFSQCoiIiIihUoBqYiIiIgUKp/CbsDFMAwDgNjY2EJuiYiIiIi4Y4/T7HFbdoplQHr+/HkAatSoUcgtEREREZHsnD9/npCQkGzr2IzchK1FTHp6OsePH6dcuXLYbLZ8f7/Y2Fhq1KjB0aNHCQ4Ozvf3k9zR91I06XspuvTdFE36XoomfS+XzjAMzp8/T9WqVfHyyn6WaLHsIfXy8qJ69eoF/r7BwcH6j7II0vdSNOl7Kbr03RRN+l6KJn0vlyannlE7LWoSERERkUKlgFRERERECpUC0lzw9/fnhRdewN/fv7CbIg70vRRN+l6KLn03RZO+l6JJ30vBKpaLmkRERESk5FAPqYiIiIgUKgWkIiIiIlKoFJCKiIiISKFSQCoiIiIihUoBqYiIiIgUKgWkuTB58mRq165NQEAA7dq146+//irsJpVY//d//4fNZnP6adSokVWemJjIyJEjqVChAmXLluWmm24iKirK6RlHjhyhX79+lClThsqVK/Pkk0+Smppa0B+lWFu1ahXXXXcdVatWxWazMW/ePKdywzB4/vnnqVKlCoGBgfTo0YP9+/c71Tl79iyDBw8mODiY0NBQhg0bRlxcnFOdbdu20aVLFwICAqhRowavv/56fn+0Yi+n72bo0KEuf4Z69+7tVEffjWdNnDiRNm3aUK5cOSpXrszAgQPZu3evUx1P/d21YsUKWrVqhb+/P/Xr1+eLL77I749XbOXme+nWrZvLn5cHHnjAqY6+lwJiSLZmzpxp+Pn5GZ9//rmxc+dOY/jw4UZoaKgRFRVV2E0rkV544QWjSZMmxokTJ6yfU6dOWeUPPPCAUaNGDWPZsmXGhg0bjPbt2xsdO3a0ylNTU42mTZsaPXr0MDZv3mz88ssvRsWKFY1x48YVxscptn755Rfj2WefNebMmWMAxty5c53KX331VSMkJMSYN2+esXXrVuP666836tSpY1y4cMGq07t3b6N58+bG2rVrjdWrVxv169c3br/9dqs8JibGCA8PNwYPHmzs2LHD+Pbbb43AwEBj6tSpBfUxi6Wcvpu7777b6N27t9OfobNnzzrV0XfjWb169TKmTZtm7Nixw9iyZYvRt29fo2bNmkZcXJxVxxN/dx08eNAoU6aMMWbMGGPXrl3G+++/b3h7exuLFi0q0M9bXOTme+natasxfPhwpz8vMTExVrm+l4KjgDQHbdu2NUaOHGldp6WlGVWrVjUmTpxYiK0quV544QWjefPmbsuio6MNX19fY9asWVbe7t27DcBYs2aNYRjm/6y9vLyMyMhIq85HH31kBAcHG0lJSfna9pIqc9CTnp5uREREGG+88YaVFx0dbfj7+xvffvutYRiGsWvXLgMw1q9fb9VZuHChYbPZjGPHjhmGYRgffvihUb58eafvZezYscZll12Wz5+o5MgqIB0wYECW9+i7yX8nT540AGPlypWGYXju766nnnrKaNKkidN73XbbbUavXr3y+yOVCJm/F8MwA9JHH300y3v0vRQcDdlnIzk5mY0bN9KjRw8rz8vLix49erBmzZpCbFnJtn//fqpWrUrdunUZPHgwR44cAWDjxo2kpKQ4fR+NGjWiZs2a1vexZs0amjVrRnh4uFWnV69exMbGsnPnzoL9ICXUoUOHiIyMdPoeQkJCaNeundP3EBoaSuvWra06PXr0wMvLi3Xr1ll1rrrqKvz8/Kw6vXr1Yu/evZw7d66APk3JtGLFCipXrsxll13Ggw8+yJkzZ6wyfTf5LyYmBoCwsDDAc393rVmzxukZ9jr6/1HuZP5e7KZPn07FihVp2rQp48aNIyEhwSrT91JwfAq7AUXZ6dOnSUtLc/oPESA8PJw9e/YUUqtKtnbt2vHFF19w2WWXceLECV588UW6dOnCjh07iIyMxM/Pj9DQUKd7wsPDiYyMBCAyMtLt92Uvk0tn/z26+z07fg+VK1d2Kvfx8SEsLMypTp06dVyeYS8rX758vrS/pOvduzc33ngjderU4e+//+aZZ56hT58+rFmzBm9vb303+Sw9PZ3Ro0fTqVMnmjZtCuCxv7uyqhMbG8uFCxcIDAzMj49UIrj7XgDuuOMOatWqRdWqVdm2bRtjx45l7969zJkzB9D3UpAUkEqR0qdPHyt9xRVX0K5dO2rVqsX333+vP9QiuTBo0CAr3axZM6644grq1avHihUr6N69eyG2rHQYOXIkO3bs4Pfffy/spoiDrL6XESNGWOlmzZpRpUoVunfvzt9//029evUKupmlmobss1GxYkW8vb1dVkJGRUURERFRSK0qXUJDQ2nYsCEHDhwgIiKC5ORkoqOjneo4fh8RERFuvy97mVw6++8xuz8XERERnDx50qk8NTWVs2fP6rsqYHXr1qVixYocOHAA0HeTn0aNGsWCBQv47bffqF69upXvqb+7sqoTHBysf7BnI6vvxZ127doBOP150fdSMBSQZsPPz48rr7ySZcuWWXnp6eksW7aMDh06FGLLSo+4uDj+/vtvqlSpwpVXXomvr6/T97F3716OHDlifR8dOnRg+/btTv/DXbJkCcHBwVx++eUF3v6SqE6dOkRERDh9D7Gxsaxbt87pe4iOjmbjxo1WneXLl5Oenm79hd+hQwdWrVpFSkqKVWfJkiVcdtllGhL2oH///ZczZ85QpUoVQN9NfjAMg1GjRjF37lyWL1/uMt3BU393dejQwekZ9jr6/5F7OX0v7mzZsgXA6c+LvpcCUtirqoq6mTNnGv7+/sYXX3xh7Nq1yxgxYoQRGhrqtOJOPOfxxx83VqxYYRw6dMj4448/jB49ehgVK1Y0Tp48aRiGuXVKzZo1jeXLlxsbNmwwOnToYHTo0MG6375FR8+ePY0tW7YYixYtMipVqqRtn/Lo/PnzxubNm43NmzcbgPH2228bmzdvNg4fPmwYhrntU2hoqPHjjz8a27ZtMwYMGOB226eWLVsa69atM37//XejQYMGTlsLRUdHG+Hh4caQIUOMHTt2GDNnzjTKlCmjrYVykN13c/78eeOJJ54w1qxZYxw6dMhYunSp0apVK6NBgwZGYmKi9Qx9N5714IMPGiEhIcaKFSuctg9KSEiw6nji7y779kJPPvmksXv3bmPy5MnaXigbOX0vBw4cMF566SVjw4YNxqFDh4wff/zRqFu3rnHVVVdZz9D3UnAUkObC+++/b9SsWdPw8/Mz2rZta6xdu7awm1Ri3XbbbUaVKlUMPz8/o1q1asZtt91mHDhwwCq/cOGC8dBDDxnly5c3ypQpY9xwww3GiRMnnJ7xzz//GH369DECAwONihUrGo8//riRkpJS0B+lWPvtt98MwOXn7rvvNgzD3Ppp/PjxRnh4uOHv7290797d2Lt3r9Mzzpw5Y9x+++1G2bJljeDgYOOee+4xzp8/71Rn69atRufOnQ1/f3+jWrVqxquvvlpQH7HYyu67SUhIMHr27GlUqlTJ8PX1NWrVqmUMHz7c5R/Q+m48y933ARjTpk2z6njq767ffvvNaNGiheHn52fUrVvX6T3EWU7fy5EjR4yrrrrKCAsLM/z9/Y369esbTz75pNM+pIah76Wg2AzDMAquP1ZERERExJnmkIqIiIhIoVJAKiIiIiKFSgGpiIiIiBQqBaQiIiIiUqgUkIqIiIhIoVJAKiIiIiKFSgGpiIiIiBQqBaQiIiIiUqgUkIqIiIhIoVJAKiIiIiKFSgGpiIiIiBSq/wePKYRCtrw5kAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "plt.figure(figsize=(8,6))\n",
        "plt.plot(ma_100_days, 'r')\n",
        "plt.plot(data.Close, 'g')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1158c05f-1a2c-41f8-8add-85720074cdcd",
      "metadata": {
        "id": "1158c05f-1a2c-41f8-8add-85720074cdcd"
      },
      "outputs": [],
      "source": [
        "ma_200_days = data.Close.rolling(200).mean()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "97a1b79b-2302-43d7-883a-a0a255c864bf",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 522
        },
        "id": "97a1b79b-2302-43d7-883a-a0a255c864bf",
        "outputId": "72d77798-f0a7-441c-8c78-82fe723e508f"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAqQAAAH5CAYAAABXviwdAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAACgE0lEQVR4nOzdd3hUVRrH8e+kQ0ih914E6SgdFAWluqAioliQZkNBLBTBiqJiQREFUVEUFKkiSkeKNOm9Si8JNQlJSJ3ZPy4zmcmUJJCQ9vs8D8+ce+65d86wu+7rKe8xWSwWCyIiIiIi2cQruzsgIiIiIvmbAlIRERERyVYKSEVEREQkWykgFREREZFspYBURERERLKVAlIRERERyVYKSEVEREQkW/lkdweuh9ls5syZMwQFBWEymbK7OyIiIiKSisVi4cqVK5QpUwYvL89joLkyID1z5gzly5fP7m6IiIiISBpOnjxJuXLlPLbJlQFpUFAQYPzA4ODgbO6NiIiIiKQWFRVF+fLlbXGbJ7kyILVO0wcHBysgFREREcnB0rO8UpuaRERERCRbKSAVERERkWylgFREREREspUCUhERERHJVgpIRURERCRbKSAVERERkWylgFREREREspUCUhERERHJVgpIRURERCRbKSAVERERkWylgFREREREspUCUhERERHJVgpIRURERCRbKSAVERERkWylgFREREREspUCUhERERHJVgpIRURERCRbKSAVERERAaZsm0K/+f1IMidld1fyHZ/s7oCIiIhITtBnfh8A7qp0F73q9crm3uQvGiEVERERsXMi8kR2dyHfUUAqIiIi+d7xiOO2ckxiTDb2JH9SQCoiIiL5Wnh0OJU+r2S79jZ5Z19n8ikFpCIiIpKvvbzkZYdrHy9tsbnZFJCKiIhIvjZt1zSnum6/duOBGQ9gsViyoUf5j/4VQERERPKtuKQ4p7qZe2ey69wuAOYfmE/Xml1vdrfyHY2QioiISL511493OdUduHjAVv5227eMWD6C+KR4W11EXARj147VbvxMpIBURERE8q0NpzY41SWbk23lBQcXMOafMUzYNMFW99yfz/Hastdo8V2Lm9LH/EABqYiIiIidZEuyU92hi4ds5SX/LQHg9JXTN61PeZ0CUhEREZE0BPgE2Momkykbe5I3KSAVERERSYOvt6+t7GVS+JTZ9Dcq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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "plt.figure(figsize=(8,6))\n",
        "plt.plot(ma_100_days, 'r')\n",
        "plt.plot(ma_200_days,'b')\n",
        "plt.plot(data.Close,'g')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "0ac073de-1a30-487c-a1f8-c809cbba06db",
      "metadata": {
        "id": "0ac073de-1a30-487c-a1f8-c809cbba06db"
      },
      "outputs": [],
      "source": [
        "data.dropna(inplace=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "64246466-177b-46f9-b4eb-6ee5005bfd6b",
      "metadata": {
        "id": "64246466-177b-46f9-b4eb-6ee5005bfd6b"
      },
      "outputs": [],
      "source": [
        "data_train = pd.DataFrame(data.Close[0: int(len(data)*0.80)])\n",
        "data_test = pd.DataFrame(data.Close[int(len(data)*0.80): len(data)])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "0f4c0b4b-2b5e-4f62-bd84-47a86ed3da3e",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0f4c0b4b-2b5e-4f62-bd84-47a86ed3da3e",
        "outputId": "4fd01050-e7d0-4233-96b2-4103a519fcdb"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2208"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ],
      "source": [
        "data_train.shape[0]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "0a609554-633d-4edf-abc1-21bd874a3cd1",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0a609554-633d-4edf-abc1-21bd874a3cd1",
        "outputId": "ce0b4643-cc8c-4347-9e17-95d4e305cc88"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "553"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ],
      "source": [
        "data_test.shape[0]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d5144e93-eab7-479f-9fde-9bf8c5786dc6",
      "metadata": {
        "id": "d5144e93-eab7-479f-9fde-9bf8c5786dc6"
      },
      "outputs": [],
      "source": [
        "from sklearn.preprocessing import MinMaxScaler\n",
        "scaler = MinMaxScaler(feature_range=(0,1))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "4c2793bd-1def-45f7-8fd2-9115eed1c2c1",
      "metadata": {
        "id": "4c2793bd-1def-45f7-8fd2-9115eed1c2c1"
      },
      "outputs": [],
      "source": [
        "data_train_scale = scaler.fit_transform(data_train)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d55d63c2-132a-40b5-9398-e576ceba14fd",
      "metadata": {
        "id": "d55d63c2-132a-40b5-9398-e576ceba14fd"
      },
      "outputs": [],
      "source": [
        "x = []\n",
        "y = []\n",
        "\n",
        "for i in range(100, data_train_scale.shape[0]):\n",
        "    x.append(data_train_scale[i-100:i])\n",
        "    y.append(data_train_scale[i,0])\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "998369e6-f1ad-4cf5-af58-0aa5b7aa315c",
      "metadata": {
        "id": "998369e6-f1ad-4cf5-af58-0aa5b7aa315c"
      },
      "outputs": [],
      "source": [
        "x, y = np.array(x), np.array(y)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "3c9c6717-e792-4206-960f-0689203555ca",
      "metadata": {
        "id": "3c9c6717-e792-4206-960f-0689203555ca"
      },
      "outputs": [],
      "source": [
        "from keras.layers import Dense, Dropout, LSTM\n",
        "from keras.models import Sequential"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "14867cd4-c1ed-4cf9-b339-245bfaec0852",
      "metadata": {
        "id": "14867cd4-c1ed-4cf9-b339-245bfaec0852"
      },
      "outputs": [],
      "source": [
        "model = Sequential()\n",
        "model.add(LSTM(units = 50, activation = 'relu', return_sequences = True,\n",
        "               input_shape = ((x.shape[1],1))))\n",
        "model.add(Dropout(0.2))\n",
        "\n",
        "model.add(LSTM(units = 60, activation='relu', return_sequences = True))\n",
        "model.add(Dropout(0.3))\n",
        "\n",
        "model.add(LSTM(units = 80, activation = 'relu', return_sequences = True))\n",
        "model.add(Dropout(0.4))\n",
        "\n",
        "model.add(LSTM(units = 120, activation = 'relu'))\n",
        "model.add(Dropout(0.5))\n",
        "\n",
        "model.add(Dense(units =1))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c69edcc2-b11d-4702-8a6c-f6a6e677e79a",
      "metadata": {
        "id": "c69edcc2-b11d-4702-8a6c-f6a6e677e79a"
      },
      "outputs": [],
      "source": [
        "model.compile(optimizer = 'adam', loss = 'mean_squared_error')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f36e439a-0106-4108-9630-7cdd7e5428e4",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f36e439a-0106-4108-9630-7cdd7e5428e4",
        "outputId": "81d21c06-a7c5-4bd9-8873-1f33bfdb5159"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/50\n",
            "66/66 [==============================] - 27s 320ms/step - loss: 0.0258\n",
            "Epoch 2/50\n",
            "66/66 [==============================] - 19s 285ms/step - loss: 0.0067\n",
            "Epoch 3/50\n",
            "66/66 [==============================] - 18s 267ms/step - loss: 0.0065\n",
            "Epoch 4/50\n",
            "66/66 [==============================] - 17s 260ms/step - loss: 0.0050\n",
            "Epoch 5/50\n",
            "66/66 [==============================] - 19s 282ms/step - loss: 0.0042\n",
            "Epoch 6/50\n",
            "66/66 [==============================] - 18s 275ms/step - loss: 0.0040\n",
            "Epoch 7/50\n",
            "66/66 [==============================] - 17s 262ms/step - loss: 0.0035\n",
            "Epoch 8/50\n",
            "66/66 [==============================] - 19s 288ms/step - loss: 0.0051\n",
            "Epoch 9/50\n",
            "66/66 [==============================] - 17s 258ms/step - loss: 0.0038\n",
            "Epoch 10/50\n",
            "66/66 [==============================] - 17s 260ms/step - loss: 0.0032\n",
            "Epoch 11/50\n",
            "66/66 [==============================] - 18s 278ms/step - loss: 0.0033\n",
            "Epoch 12/50\n",
            "66/66 [==============================] - 17s 260ms/step - loss: 0.0034\n",
            "Epoch 13/50\n",
            "66/66 [==============================] - 19s 296ms/step - loss: 0.0035\n",
            "Epoch 14/50\n",
            "66/66 [==============================] - 19s 289ms/step - loss: 0.0034\n",
            "Epoch 15/50\n",
            "66/66 [==============================] - 17s 258ms/step - loss: 0.0032\n",
            "Epoch 16/50\n",
            "66/66 [==============================] - 17s 264ms/step - loss: 0.0030\n",
            "Epoch 17/50\n",
            "66/66 [==============================] - 18s 275ms/step - loss: 0.0027\n",
            "Epoch 18/50\n",
            "66/66 [==============================] - 18s 270ms/step - loss: 0.0028\n",
            "Epoch 19/50\n",
            "66/66 [==============================] - 17s 263ms/step - loss: 0.0028\n",
            "Epoch 20/50\n",
            "66/66 [==============================] - 23s 344ms/step - loss: 0.0028\n",
            "Epoch 21/50\n",
            "41/66 [=================>............] - ETA: 6s - loss: 0.0027"
          ]
        }
      ],
      "source": [
        "model.fit(x,y, epochs = 25, batch_size =32, verbose =1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "62f9decd-83a6-4c03-8963-dc3298b2a104",
      "metadata": {
        "id": "62f9decd-83a6-4c03-8963-dc3298b2a104"
      },
      "outputs": [],
      "source": [
        "model.summary()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "89cf9dc7-4e14-4c80-82bc-d6dcac8c98a2",
      "metadata": {
        "id": "89cf9dc7-4e14-4c80-82bc-d6dcac8c98a2"
      },
      "outputs": [],
      "source": [
        "pas_100_days = data_train.tail(100)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "67ef7a1e-63cc-4874-9b61-634026572822",
      "metadata": {
        "id": "67ef7a1e-63cc-4874-9b61-634026572822"
      },
      "outputs": [],
      "source": [
        "data_test = pd.concat([pas_100_days, data_test], ignore_index=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "7a0512e4-0eaf-4137-b61d-8bb0e48ca041",
      "metadata": {
        "id": "7a0512e4-0eaf-4137-b61d-8bb0e48ca041"
      },
      "outputs": [],
      "source": [
        "data_test_scale  =  scaler.fit_transform(data_test)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "536de9d0-2cc7-41dd-b500-affd3e3fec9d",
      "metadata": {
        "id": "536de9d0-2cc7-41dd-b500-affd3e3fec9d"
      },
      "outputs": [],
      "source": [
        "x = []\n",
        "y = []\n",
        "\n",
        "for i in range(100, data_test_scale.shape[0]):\n",
        "    x.append(data_test_scale[i-100:i])\n",
        "    y.append(data_test_scale[i,0])\n",
        "x, y = np.array(x), np.array(y)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "4602f57f-8832-4bf6-a50e-bb5164ff7872",
      "metadata": {
        "id": "4602f57f-8832-4bf6-a50e-bb5164ff7872"
      },
      "outputs": [],
      "source": [
        "y_predict = model.predict(x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "ca2d2d64-b69a-4eb3-b4f6-5356bfb5b74a",
      "metadata": {
        "id": "ca2d2d64-b69a-4eb3-b4f6-5356bfb5b74a"
      },
      "outputs": [],
      "source": [
        "scale =1/scaler.scale_"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "b3e3794a-785d-4ac8-96a3-70fab6259f1c",
      "metadata": {
        "id": "b3e3794a-785d-4ac8-96a3-70fab6259f1c"
      },
      "outputs": [],
      "source": [
        "y_predict = y_predict*scale"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "5acb458b-7488-4860-9ccd-8999d67510f7",
      "metadata": {
        "id": "5acb458b-7488-4860-9ccd-8999d67510f7"
      },
      "outputs": [],
      "source": [
        "y = y*scale"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "6ab280be-9494-4ea1-baf2-45fc38130366",
      "metadata": {
        "id": "6ab280be-9494-4ea1-baf2-45fc38130366"
      },
      "outputs": [],
      "source": [
        "plt.figure(figsize=(10,8))\n",
        "plt.plot(y_predict, 'r', label = 'Predicted Price')\n",
        "plt.plot(y, 'g', label = 'Original Price')\n",
        "plt.xlabel('Time')\n",
        "plt.ylabel('Price')\n",
        "plt.legend()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "22143940-722e-4c05-8b46-d2f7d9abb882",
      "metadata": {
        "id": "22143940-722e-4c05-8b46-d2f7d9abb882"
      },
      "outputs": [],
      "source": [
        "model.save('Stock Predictions Model.keras')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "bd3bc001-da88-44ba-85d1-9b72ebfde3a6",
      "metadata": {
        "id": "bd3bc001-da88-44ba-85d1-9b72ebfde3a6"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
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
      "version": "3.11.6"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}
{
  "cells": [
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "import requests\n%matplotlib inline\nimport matplotlib.pyplot as plt\nimport json \nfrom PIL import Image\nfrom io import BytesIO",
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "#save subscription key and end_point as variables\nmy_cv_sub_key = \"<REPLACE WITH YOUR SUB KEY>\"\nmy_cv_end_point = \"<REPLACE WITH YORU ENDPOINT>\"",
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "# build the rest of the uri\nmy_analyze_url = my_cv_end_point + \"vision/v2.1/analyze\"\nmy_analyze_url",
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "#my_image_url = \"https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Pont_des_Arts%2C_Paris.jpg/2560px-Pont_des_Arts%2C_Paris.jpg\"\n#my_image_url = \"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Paris_Night.jpg/2560px-Paris_Night.jpg\"\nmy_image_url = \"https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Paris_vue_d%27ensemble_tour_Eiffel.jpg/1920px-Paris_vue_d%27ensemble_tour_Eiffel.jpg\"",
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "#configure the requests object - this is how we send the request to the api\nheaders = {'Ocp-Apim-Subscription-Key': my_cv_sub_key}\nprint(headers)\nparams = {'visualFeatures':'Categories,Description,Objects'}\nprint(params)\ndata = {'url': my_image_url}\nprint(data)\nresponse = requests.post(my_analyze_url, headers=headers,params=params,json=data)\nprint(type(response))\nresponse",
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "#store the results in the analysis object\nanalysis=response.json()\nprint(type(analysis))\nprint(analysis)",
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "#Display the image with the caption\nimage = Image.open(BytesIO(requests.get(my_image_url).content))\nplt.imshow(image)\nplt.axis(\"off\")\n_ = plt.title(analysis[\"description\"][\"captions\"][0][\"text\"].capitalize(), size=\"large\")\nplt.show()\n",
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true
      },
      "cell_type": "code",
      "source": "",
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "name": "python36",
      "display_name": "Python 3.6",
      "language": "python"
    },
    "language_info": {
      "mimetype": "text/x-python",
      "nbconvert_exporter": "python",
      "name": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.6",
      "file_extension": ".py",
      "codemirror_mode": {
        "version": 3,
        "name": "ipython"
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 1
}
# RIO Airbnb Predictive Model

<h3 align='center'> Table of Contents: </h3>

* [Acknowledgements](#acknowledgments)
* [Abstract](#abstract)
* [Getting Started](#getting-started)
* [Dependencies](#dependicies)
* [Web Portal](#web-portal)
* [Jupyter Notebooks](#notebooks)

<h2 align="center" id="acknowledgments"> Acknowledgments </h2>

### Purpose of Research
Our research aims to create price predictive models & online tools for Airbnb properties in Los Angeles using a set of key features. To set the context for our investigation, we reviewed recent literature related to these features and methods, paying particular attention to their frequency, importance, and usage.

### Faculty Mentors:
- #### **Sonya Zhang**
  - Developed the literature review and coding structure, reviewing articles, coding, advising on data collection, methodologies, data analysis, and visualization, revising, proofreading, and formatting the report.

### Fellow Researchers:
- #### **Minh Khoi Tran**
  - Reviewed articles, data cleaning, preliminary analysis and visualization on overall variables, regression and classification models, as well as Clustering and Text Mining.
  - Developed interactive website (linked below) for hosting analyses and visualizations.

- #### **Jin Im**
  - Reviewing articles, coding, preliminary analysis and visualization on `listing` Attributes, Clustering, and Text Mining.
  - Testing classification models with feature selection techniques.

- #### **Christine Pugay**
  - Generated preliminary analyses and data cleaning on Airbnb `policy`, `neighborhood`, and `points-of-interest` (POIs) attributes.
  - Constructed visualizations for these attributes using Tableau.
- #### **Kelly Lee**
   - Generated preliminary analyses and visualizations on Airbnb `reviews` and `host` attributes.
   - Performed analysis of classification models with `Scikit-learn`

This repository contains Jupyter Notebooks and Python libraries used in this project, as well as more detailed information on what we have accomplished throughout this project.


<h2 align="center" id="getting-started"> Getting Started </h2>

The Jupyter Notebook `.ipynb` files can be opened using either [Google Colaboratory](https://colab.research.google.com) or locally using [Visual Studio Code](https://code.visualstudio.com) and 3-rd party extensions.

If you decide to use Visual Studio Code to open the `.ipynb` files locally, be sure to download these required software:
* [Python](https://www.python.org/downloads/) (3.10 or above)
* [Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) (can be installed within Visual Studio Code through the `Extensions` tab)

Since the `listings.csv` was too large to be directly published to GitHub, it has been included inside `dataset.zip`. Remember to unzip the folder and make sure the folder's name is `dataset`.

**CAUTION:** The `airbnblib` folder is meant to house custom-made functions used in the notebooks. Remember to include the `airbnblib` folder in the same directory as your notebooks, or else many functionalities would not work.

<h2 align='center' id="dependencies"> Dependencies </h2>

All required dependencies are now listed in the `requirements.txt` file

To install these Python libraries, run `pip install -r requirements.txt` in the root directory of the project, i.e.:
```bash
$ pip install -r requirements.txt
```

<h2 align='center' id="web-portal"> Web Portal </h2>

This is a web portal created to serve this project by showcasing exploratory data analysis, model results, and interactive demos of the model itself. 

The repository for the web portal itself has been migrated a separate repository. You can check them here: [RIO Airbnb Web Portal](https://github.com/marked01one/rio-airbnb-web-portal)

<h2 align='center' id="notebooks"> Jupyter Notebooks </h2>

### `rough_clean`
* Notebook for making broad strokes to clean and refine the data. 
* For more involved data refining processes such as sentimental analysis, future notebooks will be created specifically for those purposes 

### `exploratory_analysis`
* Notebook for doing exploratory data analysis into the data, which will be used to determine which variables to delete, edit, etc.

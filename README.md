# 🎬 EDA of Amazon Prime Movies & TV Shows

## **Project Overview**

This repository contains an Exploratory Data Analysis (EDA) of Amazon Prime Video content (movies and TV shows). The goal is to uncover patterns and insights related to content distribution, temporal trends, ratings (IMDb & TMDB), genres, countries of origin, and contributor performance (cast/crew). The analysis is implemented as a self-contained Jupyter Notebook and accompanied by a set of exported visualizations in the `visuals/` folder.

## **Why this analysis matters**

- **Content strategy**: helps identify genres and countries where supply is strong or lacking.
- **Quality signals**: compares IMDb and TMDB scores to understand audience vs platform-based reception.
- **Temporal insights**: shows how content volume and popularity evolved over time (useful for trend forecasting).

## **Dataset**

- **Source**: The notebook reads one or more CSV datasets (commonly collected public Amazon Prime listings datasets). The repository does not include the original raw CSV by default — place your dataset(s) alongside the notebook or update the notebook's data path.
- **Key fields used**: `title`, `type` (Movie/TV Show), `release_year`, `country`, `genre` (or `genres`), `imdb_score`, `tmdb_score`, `popularity`, and contributor fields such as `cast` or `director`.

## **Notebook**

- **Main file**: `EDA_of_Amazon_Prime_Movies_&_TV_Shows.ipynb` — contains the full analysis pipeline: data loading, cleaning, feature extraction, visualizations, and commentary.
- The notebook is annotated with markdown sections and charts so it can be run interactively and re-used as a reproducible analysis.

## **Project Structure**

- `EDA_of_Amazon_Prime_Movies_&_TV_Shows.ipynb`: Jupyter Notebook with the analysis.
- `visuals/`: directory containing exported plot images used in reports or presentations.
- `README.md`: this file — project overview, how-to, and findings.

## **How to run the analysis**

1. Create (or activate) a Python environment with the required packages.

  ```powershell
  python -m venv .venv; .\.venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  ```

  If you don't have a `requirements.txt`, install common packages used in the notebook:

  ```powershell
  pip install pandas numpy matplotlib seaborn plotly jupyterlab
  ```

2. Open the notebook in Jupyter or JupyterLab:

  ```powershell
  jupyter lab
  ```

3. Run cells sequentially. If your dataset path differs, update the data-load cell near the top of the notebook.

## **Dependencies**

- **Core**: `pandas`, `numpy`.
- **Visualization**: `matplotlib`, `seaborn`, `plotly`.
- **Optional**: `scipy` (statistical tests), `tqdm` (progress bars when processing large datasets).

## **Analysis methodology (summary)**

- **Data ingestion**: read CSV(s) into pandas DataFrames and inspect columns for missing values and data types.
- **Cleaning & parsing**: normalize `country` and `genres` strings, parse dates/years, convert numeric fields, and handle missing ratings.
- **Feature engineering**: extract primary genre, compute yearly counts, rolling averages for ratings/popularity, and contributor-level aggregates (average rating per director/actor).
- **Exploratory plots**: distribution charts (content type), time-series trends (release counts, popularity), bar charts (top genres/countries), heatmaps (genre vs country), and scatter/violin plots for rating comparisons.
- **Interpretation**: quantify and summarize observed trends, highlight outliers and notable contributors.

## **Key findings (high-level)**

- **Content mix**: Movies typically make up the majority of catalog entries; TV shows form a smaller but impactful portion.
- **Growth over time**: A notable increase in titles after 2010 with a peak near 2020, reflecting streaming expansion.
- **Geographic concentration**: US-produced content dominates, with India and the UK commonly following.
- **Genre and ratings**: Certain genres (e.g., Documentary, History) show higher median IMDb ratings, while platform/popularity metrics favor genres like Animation or Reality depending on dataset specifics.
- **Ratings vs popularity**: TMDB and IMDb often disagree; shows can have higher platform scores while movies drive popularity spikes.

Note: these findings are a summary of the notebook's visual outputs — verify details by inspecting the notebook cells and charts.

## **Visuals & outputs**

- The `visuals/` folder contains the notebook's exported figures (e.g., `chart1_content_type.png`, `chart2_yearly_trend.png`). Use these for presentations or reports.

## **Reproducibility tips**

- Keep a copy of the raw dataset (original CSV) and a cleaned export (e.g., `data/cleaned_amazon_prime.csv`).
- If running on different machines, consider exporting intermediate processed DataFrames to CSV to speed repetitive work.

## **Next steps & ideas**

- Add time-series forecasting (ARIMA/Prophet) for content volume trends.
- Enrich data with external metadata (genre taxonomies, region-specific popularity metrics).
- Perform sentiment analysis on user reviews (if available) and correlate with ratings.
- Build an interactive dashboard (Plotly Dash or Streamlit) for stakeholder exploration.

## **Contributing**

- To suggest improvements or add data, open an issue or submit a pull request. Describe new data sources, preprocessing steps, or improved visualizations.

## **Acknowledgments & Sources**

- This repository contains EDA work using public datasets and open-source Python libraries. Cite the original dataset source if you publish findings.

---





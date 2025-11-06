# Spotify Performance Dashboard

🎧 **Spotify Performance Dashboard** is a professional data analytics dashboard that visualizes Spotify's quarterly financial and user performance from 2016–2023. It is designed to provide insights into revenue, profit, user growth, and cost structure in an interactive and user-friendly interface.

---

## Features

- Key Performance Indicators (KPIs) displayed at the top:
  - Total Revenue (€M)
  - Gross Profit (€M)
  - Profit Margin (%)
  - QoQ Growth (%)
  - Premium Share (%)
  - Ad Share (%)
  - MAUs (M)
  - Revenue Change (€M)
- Interactive charts:
  - Revenue vs. Profit over time
  - User Growth over time
  - Cost Breakdown (last quarter)
- Theme switcher:
  - Light, Dark, and Spotify custom theme
- Fully responsive layout
- Designed for Streamlit with Plotly charts

---

## Tech Stack & Libraries

- **Python 3.10+**
- **Streamlit**: for creating the interactive dashboard
- **Pandas**: for data cleaning and processing
- **Plotly**: for interactive and aesthetic visualizations
- **Plotly Express & Graph Objects**: for line, bar, and pie charts
- **HTML/CSS**: minor customization for theme styling

---



---

## How It Works

1. **Data Loading**: Reads the `Spotify Quarterly.csv` dataset and cleans numeric columns.
2. **KPI Calculation**: Computes Total Revenue, Gross Profit, Profit Margin, MAUs, Premium & Ad share, QoQ growth, and Revenue Change.
3. **Visualization**: Generates interactive charts:
   - Bar + line chart for Revenue & Profit
   - Line chart for User Growth
   - Pie chart for Cost Breakdown
4. **Theme Switching**: Users can choose Light, Dark, or Spotify custom theme, dynamically updating colors and styles.

---

## Installation & Usage

```bash
git clone https://github.com/netblag/Spotify-Dashboard.git
cd Spotify-Dashboard
pip install -r requirements.txt
streamlit run app/streamlit_app.py


## Project Structure


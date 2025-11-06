import plotly.express as px

def get_plotly_template(theme):
    if theme == "Light":
        return "plotly_white"
    if theme == "Dark":
        return "plotly_dark"
    if theme == "Spotify":
        return {
            "layout": {
                "paper_bgcolor": "#121212",
                "plot_bgcolor": "#121212",
                "font": {"color": "#FFFFFF", "family": "Arial"},
                "colorway": ["#1DB954", "#191414", "#9be7a8", "#f7b267", "#ef476f"]
            }
        }
    return "plotly_white"

def revenue_and_profit_chart(df, theme="Light"):
    tpl = get_plotly_template(theme)
    fig = px.line(df, x="Date", y=["Total Revenue", "Gross Profit"], markers=True)
    fig.update_layout(template=tpl)
    return fig

def user_growth_chart(df, theme="Light"):
    tpl = get_plotly_template(theme)
    cols = ["MAUs"]
    extras = []
    if "Premium MAUs" in df.columns:
        cols.append("Premium MAUs")
    if "Ad MAUs" in df.columns:
        cols.append("Ad MAUs")
    fig = px.line(df, x="Date", y=cols, markers=True)
    fig.update_layout(template=tpl)
    return fig

def cost_breakdown_chart(df, theme="Light"):
    tpl = get_plotly_template(theme)
    cost_cols = [c for c in ["Sales and Marketing Cost", "Research and Development Cost", "Genreal and Adminstraive Cost"] if c in df.columns]
    if not cost_cols:
        return None
    fig = px.bar(df, x="Date", y=cost_cols)
    fig.update_layout(template=tpl)
    return fig

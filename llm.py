import plotly.express as px

def generate_chart(df, x_col, y_col):
    fig = px.line(
        df,
        x=x_col,
        y=y_col,
        title=f'{y_col} 趋势分析'
    )

    return fig

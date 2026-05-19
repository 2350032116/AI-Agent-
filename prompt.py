import plotly.express as px


def sales_by_product(df, product_col, sales_col):
    grouped = df.groupby(product_col)[sales_col].sum().reset_index()

    fig = px.bar(
        grouped,
        x=product_col,
        y=sales_col,
        title="产品销售额分析"
    )

    return fig


def sales_trend(df, date_col, sales_col):
    grouped = df.groupby(date_col)[sales_col].sum().reset_index()

    fig = px.line(
        grouped,
        x=date_col,
        y=sales_col,
        title="销售趋势分析"
    )

    return fig

import pandas as pd
import statistics as stat

def q1():
    # google sheet url  'https://docs.google.com/spreadsheets/d/16i38oonuX1y1g7C_UAmiK9GkY7cS-64DfiDMNiR41LM/edit#gid=0'
    sheet_id = '16i38oonuX1y1g7C_UAmiK9GkY7cS-64DfiDMNiR41LM'
    sheet_name = 'Sheet1'
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    data = pd.read_csv(url)

    stat.mean(data['order_amount'])
    s = sorted(data['order_amount'])
    order_amount_per_item_sorted = sorted(data['order_amount'] / data['total_items'])

    data[(data.shop_id==42)]

    # AOV per shop in descending order
    aov_per_shop = data.groupby('shop_id')['order_amount'].mean().sort_values(ascending=False)

    # AOV excluding shop 42 and 78
    max_aov_shop_id = aov_per_shop.argmax()

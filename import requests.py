import yfinance as yf
from datetime import datetime, timedelta

# Функция для получения данных за определенный час
def get_hourly_stats(ticker, date, hour):
    stock = yf.Ticker(ticker)
    start_time = datetime.strptime(f"{date} {hour}", "%Y-%m-%d %H")
    end_time = start_time + timedelta(hours=1)
    data = stock.history(start=start_time, end=end_time, interval='1m')
    
    if not data.empty:
        price_start = data.iloc[0]['Close']
        price_end = data.iloc[-1]['Close']
        percent_change = ((price_end - price_start) / price_start) * 100
        min_price = data['Low'].min()
        max_price = data['High'].max()
        price_difference = max_price - min_price
        
        return percent_change, price_difference
    else:
        return None, None

# Получаем статистику за каждый час 10 мая
ticker = 'ATNF'
date = '2024-05-10'
for hour in range(24):
    percent_change, price_difference = get_hourly_stats(ticker, date, hour)
    if percent_change is not None:
        print(f"Час: {hour}:00")
        print(f"Процентное изменение: {percent_change:.2f}%")
        print(f"Разница между мин. и макс. ценой: {price_difference:.2f}\n")

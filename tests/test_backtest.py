from src.data import load_data
from src.stategy import moving_average_crossover

def main():
    data = load_data('APPL','2020-01-01','2023-01-01')
    signals = moving_average_crossover(data)
    print(signals[['Close','short_ma','long_ma','signal','position']].tail(10))

if __name__ == '__main__':
    main()


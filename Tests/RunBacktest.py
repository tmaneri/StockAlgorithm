from Tests.Backtesting import Backtesting


def PrintStockAlgoMetrics(iteration_count, algo_cash, algo_trades, avg_stock_profit_sum, algo_portfolio_profit):
    avg_algo_cash = algo_cash / iteration_count
    print("Stock algorithm info for {} iterations".format(iteration_count))
    # metrics for stock algo
    print("Total algorithm cash average: {}".format(avg_algo_cash))
    avg_pct = 0
    if algo_trades != 0:
        avg_pct = avg_stock_profit_sum / algo_trades
    print("Total algorithm trades executed: {}".format(algo_trades))
    print("Average algorithm trade profit: {}".format(avg_pct))
    avg_portfolio_profit = algo_portfolio_profit / iteration_count
    print("Total average profit percentage for buy and hold: {}%".format(avg_portfolio_profit))
    print("Commencing next iteration...")
    print("_" * 150)
    print("\n")


def PrintBuyHoldMetrics(iteration_count, bh_cash, bh_trades, bh_avg_stock_profit_sum, bh_portfolio_profit):
    print("Buy and hold info for {} iterations:".format(iteration_count))
    # metrics for buy and hold
    print("Buy and hold executed {} total trades".format(bh_trades))
    avg_bh_cash = bh_cash / iteration_count
    print("Total buy and hold cash average: {}".format(avg_bh_cash))
    avg_bh_pct = 0
    if bh_trades != 0:
        avg_bh_pct = bh_avg_stock_profit_sum / bh_trades
    print("Average buy and hold trade profit: {}".format(avg_bh_pct))
    avg_portfolio_profit = bh_portfolio_profit / iteration_count
    print("Total average profit percentage for buy and hold: {}%".format(avg_portfolio_profit))
    print("_" * 150)


def RunTest(start_date="2007-01-01", end_date="2015-01-01", iterations=2):
    NYSE = "../Data/NYSE.txt"
    SPY = "../Data/SPY.txt"
    PENNY = "../Data/PENNY.txt"  # Data is biased for penny stock info.
    USA = "../Data/USA.txt"
    API_KEY = "MA6YR6D5TVXK1W67"

    total_algo_cash = 0
    total_avg_stock_profit_sum = 0
    total_algo_trades = 0
    total_algo_portfolio_sum = 0

    total_bh_cash = 0
    total_avg_bh_profit_sum = 0
    total_bh_trades = 0
    total_bh_portfolio_sum = 0

    for i in range(1, iterations + 1):
        historical_test = Backtesting(start_date=start_date, end_date=end_date, api_key=API_KEY)
        tickers = historical_test.get_random_ticks(file=SPY, amount=1)
        tickers.append("HSY")
        print(tickers)
        historical_test.test_algorithm(tickers)

        total_algo_cash += historical_test.cash
        total_algo_trades += historical_test.trades_count
        total_avg_stock_profit_sum += historical_test.stock_trade_percent_sum
        total_algo_portfolio_sum += historical_test.algo_portfolio_profit

        total_bh_cash += historical_test.buy_hold_money
        total_bh_trades += historical_test.buy_hold_trades_count
        total_avg_bh_profit_sum += historical_test.buy_hold_profit_percent_sum
        total_bh_portfolio_sum += historical_test.buy_hold_portfolio_profit

        PrintBuyHoldMetrics(i, bh_cash=total_bh_cash,
                            bh_trades=total_bh_trades,
                            bh_avg_stock_profit_sum=total_avg_bh_profit_sum,
                            bh_portfolio_profit=total_avg_bh_profit_sum)
        PrintStockAlgoMetrics(i, algo_cash=total_algo_cash,
                              algo_trades=total_algo_trades,
                              avg_stock_profit_sum=total_avg_stock_profit_sum,
                              algo_portfolio_profit=total_algo_portfolio_sum)

    print("Backtest complete.")


if __name__ == '__main__':
    RunTest()

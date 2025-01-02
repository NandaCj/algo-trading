import apache_beam as beam
from core.pipeline import GetStockDataFromYahooApi, GetStockToTrade
from core.pipeline_configs import p_options
from core.trading.algos.reversal import DayHighReversalStrategy

pipeline = beam.Pipeline(options=p_options)


(
    pipeline
    | beam.Create([None])
    | "Yield List of stocks to Trade" >> beam.ParDo(GetStockToTrade())  # TODO : make this as side input
    | "Break Fusion" >> beam.Reshuffle()
    | "Get Stocks Current Price" >> beam.ParDo(GetStockDataFromYahooApi())  # TODO make this as side input
     # TODO : DoFn to decide on initial order or profit order, for current price
    | "Break Fusion 1 " >> beam.Reshuffle()
    | "DayHighReversalStrategy" >> beam.ParDo(DayHighReversalStrategy())
)


if __name__ == '__main__':
    res = pipeline.run()
    res.wait_until_finish()
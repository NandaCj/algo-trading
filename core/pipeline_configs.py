from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions



class AlgoTradingPipelineOptions(PipelineOptions):
    """
    Add all the cli variables here for the pipeline
    """
    pass


options_dict = {
    "streaming": True,
    "runner": "DirectRunner",
    "direct_num_workers": 10,
    "direct_running_mode": "multi_processing"
}

p_options = AlgoTradingPipelineOptions.from_dictionary(options_dict)
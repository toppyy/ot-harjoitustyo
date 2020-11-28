from math_helper.mean import mean
from math_helper.median import median
from math_helper.standard_deviation import standard_deviation
from gui.output_elements.header import Header
from gui.output_elements.text   import Text

def summary(column):

    data = column["data"]

    return [
        Header(column["column_name"]),
        Text( "Median: {}".format(median(data)) ),
        Text( "Mean:   {}".format(mean(data)) ),
        Text( "Std.dev: {}".format(standard_deviation(data)) )
    ]

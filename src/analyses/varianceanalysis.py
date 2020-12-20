from scipy.stats import f
from analyses.summarytable  import summarytable
from math_helper.mean       import mean


def squares_between_groups(summary_by_group,total_mean):

    between_groups = []
    for group in summary_by_group:
        stat = group[1] * ( (group[2]-total_mean)**2 )
        between_groups.append(stat)

    ss_between_groups = sum(between_groups)

    dfn = ( len(summary_by_group)-1 )
    ms_between = ss_between_groups / dfn

    return (
        ss_between_groups,
        ms_between,
        dfn
    )

def squares_within_groups(group_by_data,analyse_data,summary_by_group):

    # terrible, but will do for now
    groups = {}
    for idx,group in enumerate(group_by_data):
        obs = groups.get(group,[])
        obs.append(analyse_data[idx])
        groups[group] = obs

    ss_within = 0
    for group in groups:
        obs = groups[group]
        group_mean = list(filter(lambda g: g[0]==group,summary_by_group))[0]
        group_mean = group_mean[2]


        diff = [(x-group_mean)**2 for x in obs]
        ss_within = ss_within + sum(diff)

    dfd = ( len(analyse_data) - len(summary_by_group) )
    ms_within = ss_within / dfd

    return (
        ss_within,
        ms_within,
        dfd
    )


def varianceanalysis(column_to_group_by,column_to_analyse):
    """Analysis of variance

    Args:
        column_to_group_by: the column describing groups to compare
        column_to_analyse: column for the data to use in comparison

    Returns:
        A list of test statistics
    """


    group_by_data = column_to_group_by['data']
    analyse_data  = column_to_analyse['data']

    summary_by_group = summarytable(column_to_group_by,column_to_analyse)

    total_mean  = mean(analyse_data)

    ss_between_groups,ms_between,dfn = squares_between_groups(summary_by_group,total_mean)

    ss_within,ms_within,dfd = squares_within_groups(group_by_data,analyse_data,summary_by_group)


    f_statistic = ms_between/ms_within

    pvalue = 1 - f.cdf(f_statistic, dfn, dfd)


    return [
        ss_between_groups,
        ss_within,
        ms_between,
        ms_within,
        f_statistic,
        pvalue
    ]

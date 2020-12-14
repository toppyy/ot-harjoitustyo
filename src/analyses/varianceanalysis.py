from analyses.summarytable  import summarytable
from math_helper.mean       import mean

def varianceanalysis(column_to_group_by,column_to_analyse):


    group_by_data = column_to_group_by['data']
    analyse_data  = column_to_analyse['data']

    summary_by_group = summarytable(column_to_group_by,column_to_analyse)

    summary_by_group.pop(0) # Remove headers

    group_means = [x[2] for x in summary_by_group]
    total_mean  = mean(analyse_data)

    between_groups = []
    for group in summary_by_group:
        stat = group[1] * ( (group[2]-total_mean)**2 )
        between_groups.append(stat)

    ss_between_groups = sum(between_groups)
    ms_between = ss_between_groups / ( len(summary_by_group)-1 )

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

    ms_within = ss_within / ( len(analyse_data) - len(summary_by_group) )


    F_statistic = ms_between/ms_within

    return [
        ss_between_groups,
        ss_within,
        ms_between,
        ms_within,
        F_statistic
    ]

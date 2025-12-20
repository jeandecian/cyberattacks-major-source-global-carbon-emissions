from scipy import stats
import constants as c


def format_statistics(
    metric,
    attack_type,
    n,
    statistic,
    p_value,
):
    return (
        metric,
        attack_type,
        n,
        f"{statistic:.2f}",
        f"{p_value:.2e}",
        get_significance_label(p_value),
    )


def get_significance_label(p_value):
    return ("No", "Yes")[int(is_statistically_significant(p_value))]


def is_statistically_significant(p, alpha=0.05):
    return p < alpha


def perform_wilcoxon_signed_rank_test(df, base_index, attack_index):
    headers = df.columns.tolist()
    base = df[headers[base_index]].values
    attack = df[headers[attack_index]].values

    return stats.wilcoxon(attack, base, alternative="greater")

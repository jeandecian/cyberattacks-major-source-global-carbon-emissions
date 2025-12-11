import constants as c


def calculate_mean(df):
    return df.mean(numeric_only=True).round(2).tolist()


def calculate_mean_where(df, match):
    mask = df[c.STUDY].str.contains(match)
    return df[mask].mean(numeric_only=True).round(2).tolist()


def calculate_median(df):
    return df.median(numeric_only=True).round(2).tolist()


def create_numbers_list_latex(numbers):
    return [f"\\num{{{number:.2f}}}" for number in numbers]


def generate_attack_metric_table(attack, metric, df):
    if "Power" in metric:
        metric = metric.replace("Power", "Power Consumption")

    caption = f"Baseline and {attack.lower()}-induced {metric.split(' (')[0]}"
    columns = "llrrr"
    headers = generate_headers(df.columns)

    latex_table = generate_table_header(caption, columns, headers)
    latex_table += generate_attack_metric_content(df)
    latex_table += generate_table_mean_subtotals(attack, df)
    latex_table += generate_table_mean_median_totals(df)
    latex_table += generate_table_footer()

    return latex_table


def generate_caption_label(caption):
    label = f"tab:{'_'.join(caption.lower().split())}"

    return f"""\\caption{{\\textbf{{{caption}}}}}
    \\label{{{label}}}"""


def generate_attack_metric_content(df):
    content = ""

    for index, row in df.iterrows():
        study, host = row[0:2]
        numbers = create_numbers_list_latex(row[2:])
        content += f"""    {str(study)} & {str(host)} & {" & ".join(numbers)} \\\\
    """

    return content


def generate_headers(columns):
    headers = []

    for column in columns:
        column = (
            column.replace("°C", "$^\circ$C").replace("(%", "(\%").replace(" \\#", "")
        )
        headers.append(f"""\\textbf{{{column}}}""")

    return headers


def generate_subtotal_mean_of(means, description):
    if str(means[0]) == "nan":
        return ""

    means_list = create_numbers_list_latex(means)

    return f"""    \\multicolumn{{2}}{{r}}{{Mean ({description})}} & {" & ".join(means_list)} \\\\
    """


def generate_table_footer(span=""):
    return f"""    \\bottomrule
    \\end{{tabular}}
\\end{{table{span}}}"""


def generate_table_header(caption, columns, headers, span=""):
    return f"""\\begin{{table{span}}}
    \\centering
    {generate_caption_label(caption)}
    \\begin{{tabular}}{{{columns}}}
        \\toprule
        {" & ".join(headers)} \\\\
        \\midrule
    """


def generate_table_mean_median_totals(df):
    means = calculate_mean(df)
    means_list = create_numbers_list_latex(means)

    medians = calculate_median(df)
    medians_list = create_numbers_list_latex(medians)

    return f"""    \\midrule
        \\multicolumn{{2}}{{r}}{{Mean}} & {" & ".join(means_list)} \\\\
        \\multicolumn{{2}}{{r}}{{Median}} & {" & ".join(medians_list)} \\\\
    """


def generate_table_mean_subtotals(attack, df):
    subtotals = []

    descriptions = c.ATTACK_CATEGORIES.get(attack.lower().replace(" ", "-"), ())
    for description in descriptions:
        means = calculate_mean_where(df, description)
        subtotal = generate_subtotal_mean_of(means, description)

        if subtotal != "":
            subtotals.append(subtotal)

    if len(subtotals) < 2:
        return ""

    return f"""    \\midrule
    {"".join(subtotals)}"""

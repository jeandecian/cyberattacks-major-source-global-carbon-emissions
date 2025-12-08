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


def generate_content(df):
    content = ""

    for index, row in df.iterrows():
        study, host, base_metric, attack_metric, variation = row
        content += f"""    {str(study)} & {str(host)} & \\num{{{base_metric:.2f}}} & \\num{{{attack_metric:.2f}}} & \\num{{{variation:.2f}}} \\\\
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


def generate_table(attack, metric, df):
    if "Power" in metric:
        metric = metric.replace("Power", "Power Consumption")

    caption = f"Baseline and {attack.lower()}-induced {metric.split(' (')[0]}"
    label = f"tab:{'_'.join(caption.lower().split())}"
    headers = generate_headers(df.columns)

    latex_table = f"""\\begin{{table}}
    \\centering
    \\caption{{\\textbf{{{caption}}}}}
    \\label{{{label}}}
    \\begin{{tabular}}{{llrrr}}
        \\toprule
        {" & ".join(headers)} \\\\
        \\midrule
    """

    latex_table += generate_content(df)

    if attack == "Cryptojacking":
        temp_table = []

        for description in ("CPU", "GPU"):
            means = calculate_mean_where(df, description)
            subtotal = generate_subtotal_mean_of(means, description)

            if subtotal != "":
                temp_table.append(subtotal)

        if len(temp_table) > 1:
            latex_table += f"""    \\midrule
    """
            latex_table += "".join(temp_table)
    elif attack == "Denial of Service":
        temp_table = []

        for description in ("HTTP", "ICMP", "SYN", "TCP", "UDP"):
            means = calculate_mean_where(df, description)
            subtotal = generate_subtotal_mean_of(means, description)

            if subtotal != "":
                temp_table.append(subtotal)

        if len(temp_table) > 1:
            latex_table += f"""    \\midrule
    """
            latex_table += "".join(temp_table)

    means = calculate_mean(df)
    means_list = create_numbers_list_latex(means)

    medians = calculate_median(df)
    medians_list = create_numbers_list_latex(medians)

    latex_table += f"""    \\midrule
        \\multicolumn{{2}}{{r}}{{Mean}} & {" & ".join(means_list)} \\\\
        \\multicolumn{{2}}{{r}}{{Median}} & {" & ".join(medians_list)} \\\\
    """

    latex_table += f"""    \\bottomrule
    \\end{{tabular}}
\\end{{table}}"""

    return latex_table

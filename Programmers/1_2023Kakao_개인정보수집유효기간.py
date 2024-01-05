def solution(today, terms, privacies):
    answer = []
    t_year, t_month, t_date = today.split(".")
    dic_terms = {t.split(" ")[0]: int(t.split(" ")[1]) * 28 for t in terms}

    for i, priv in enumerate(privacies):
        date, term = priv.split(" ")
        p_year, p_month, p_date = date.split(".")

        a = int(t_year) - int(p_year)
        b = int(t_month) - int(p_month)
        c = int(t_date) - int(p_date)
        period = dic_terms.get(term)

        if (a * 12 + b) * 28 + c >= period:
            answer.append(i + 1)

    return answer

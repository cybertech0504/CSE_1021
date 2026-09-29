def check_patt(domain,url):
    score = 0
    count = 0
    for char in domain:
        if char == "-":
            count += 1

    if count > 2:
        print("  something is wrong \"_SUSPECIOUS_\"")
        score += 10

    if len(domain) < 5:
        print(" it didn't seems like a real Domain")
        score += 5

    if "https://" not in url:
        print(" here is no \"https://\" here")
        score += 15

    suspicious_words = ["login", "verify", "confirm", "update", "secure", "account", "suspend", "alert"]
    url_lower = url.lower()

    for word in suspicious_words:
        if word in url_lower:
            print("Suspicious word found:" + word)
            score += 8
            break

    dot_c = 0
    for char in domain:
        if char == ".":
            dot_c += 1

    if dot_c == 3:
        print(" it's not domain it's the \'I.P ADRESS\'")
        score += 20

    return score

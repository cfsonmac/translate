import translators as ts


# text = "ich liebe dich"
# print(ts.translate_text(text, "google", "auto", "zh"))
def arr_translate(arr):
    recognized_text = arr
    final_text = recognized_text[0]
    for i in range(1, len(recognized_text)):
        s1 = recognized_text[i - 1]
        s2 = recognized_text[i]
        common_substring = longest_common_substring(s1, s2)
        r1 = len(common_substring) >= 10
        r2 = (len(s1) - s1.rfind(common_substring) - len(common_substring)) < 10
        r3 = s2.find(common_substring) < 10
        if r1 and r2 and r3:
            # Concatenate the strings, removing the common substring from s2
            final_text = final_text[:final_text.rfind(common_substring)] + common_substring + s2[s2.find(
                common_substring) + len(common_substring):]
        else:
            final_text = final_text + s2
    print(final_text)
    print(ts.translate_text(final_text, "google", "auto", "zh"))
    return final_text


def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    end_pos = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i  # Update the end position of the longest common substring
    common_substring = s1[end_pos - max_len:end_pos]

    return common_substring


if __name__ == "__main__":
    recognized_text = ["aber nicht in erster Linie mit mehr Geld für Eltern die bessere Lösung W",
                       "die bessere Lösung wäre mehr Unterstützung der Kinder bessere Bildung",
                       "wieder bessere Bildungseinrichtungen bessere Betreuungsmöglichkeiten",
                       "Zeiten immer höhere Transferleistungen lösen"]
    arr_translate(recognized_text)

"""
translate_text(query_text: str, translator: str = 'bing', from_language: str = 'auto', to_language: str = 'en', **kwargs) -> Union[str, dict]
    :param query_text: str, must.
    :param translator: str, default 'bing'.
    :param from_language: str, default 'auto'.
    :param to_language: str, default 'en'.
    :param if_use_preacceleration: bool, default False.
    :param **kwargs:
            :param is_detail_result: bool, default False.
            :param professional_field: str, default None. Support alibaba(), baidu(), caiyun(), cloudTranslation(), elia(), sysTran(), youdao(), volcEngine() only.
            :param timeout: float, default None.
            :param proxies: dict, default None.
            :param sleep_seconds: float, default 0.
            :param update_session_after_freq: int, default 1000.
            :param update_session_after_seconds: float, default 1500.
            :param if_use_cn_host: bool, default False. Support google(), bing() only.
            :param reset_host_url: str, default None. Support google(), argos(), yandex() only.
            :param if_check_reset_host_url: bool, default True. Support google(), yandex() only.
            :param if_ignore_empty_query: bool, default False.
            :param limit_of_length: int, default 20000.
            :param if_ignore_limit_of_length: bool, default False.
            :param if_show_time_stat: bool, default False.
            :param show_time_stat_precision: int, default 2.
            :param if_print_warning: bool, default True.
            :param lingvanex_mode: str, default 'B2C', choose from ("B2C", "B2B").
            :param myMemory_mode: str, default "web", choose from ("web", "api").
    :return: str or dict
"""

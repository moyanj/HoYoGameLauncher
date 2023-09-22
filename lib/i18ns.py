import i18n

i18n.set("file_format", "json")
i18n.set("locale", "zh-CN")
i18n.set("fallback", "zh-CN")
i18n.set("filename_format", "{locale}.{format}")
i18n.set("enable_memoization", True)
i18n.load_path.append("data/language")


def t(key, *args, **kwargs):
    return i18n.t(key, *args, **kwargs)


def set_language(lang):
    i18n.set("locale", lang)

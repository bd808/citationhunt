#-*- encoding: utf-8 -*-
import os

# Most (all?) Wikipedias support these English settings in addition
# to the localized ones, so make sure to handle them!

EN_WIKILINK_PREFIX_BLACKLIST = [
    'File:',
    'Image:',
    'Media:'
]

EN_CITATION_NEEDED_TEMPLATES = [
    'Citation needed',
    'cn',
]

lang_code_to_config = dict(
    en = dict(
        # A friendly name for the language
        name = 'English',
        # The database to use on Tools Labs
        database = 'enwiki_p',
        # The domain for Wikipedia in this language
        wikipedia_domain = 'en.wikipedia.org',

        # The name of the category containing articles lacking
        # citations, without the 'Category:' prefix
        citation_needed_category = 'All_articles_with_unsourced_statements',

        # The names of templates that mark statements lacking
        # citations. The first letter is case-insensitive. When
        # adding a new language, this may help:
        # https://www.wikidata.org/wiki/Q5312535
        citation_needed_templates = EN_CITATION_NEEDED_TEMPLATES,

        # Wikilinks having these prefixes will be omitted
        # entirely from the output; others will get replaced
        # by their titles.
        wikilink_prefix_blacklist = EN_WIKILINK_PREFIX_BLACKLIST,

        # The name of the category for hidden categories. Categories
        # belonging to this category are typically used for maintenance
        # and should not show up on Citation Hunt.
        hidden_category = 'Hidden_categories',

        # Citation Hunt will ignore categories if their names match one
        # of these regular expressions.
        category_name_regexps_blacklist = [
            '^Articles',
            '^Pages ',
            ' stubs$',
            '.*[0-9]+.*',
        ],

        # The maximum number of categories to use
        max_categories = 5000,
    ),

    fr = dict(
        name = 'Français',
        database = 'frwiki_p',
        wikipedia_domain = 'fr.wikipedia.org',
        citation_needed_category = 'Article_à_référence_nécessaire',

        # Looks like there are many other interesting templates:
        # https://fr.wikipedia.org/wiki/Aide:Référence_nécessaire
        citation_needed_templates = EN_CITATION_NEEDED_TEMPLATES + [
            'Référence nécessaire',
            'ref nec',
            'Inédit',
            'refnec',
        ],

        wikilink_prefix_blacklist = EN_WIKILINK_PREFIX_BLACKLIST + [
            'Fichier:',
        ],

        hidden_category = 'Catégorie_cachée',

        category_name_regexps_blacklist = [
            '.*[0-9]+.*',
        ],

        max_categories = 1000,
    ),
)

# In py3: types.SimpleNamespace
class Config(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def get_localized_config(lang_code = None):
    if lang_code is None:
        lang_code = os.getenv('CH_LANG')
    cfg = Config(lang_code = lang_code, **lang_code_to_config[lang_code])
    return cfg

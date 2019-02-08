import functools

import pandas


@functools.lru_cache()
def get_crossref_type_df():
    """
    Return dataframe from Sci-Hub Coverage Study of Crossref Types
    https://github.com/greenelab/scihub/issues/7
    """
    url = "https://github.com/greenelab/scihub/raw/9280e4479fbe32a48d7c0f836b9292b0e4a5319c/data/crossref-types.tsv"
    crossref_type_df = pandas.read_csv(url, sep='\t')
    return crossref_type_df


def get_crossref_types():
    """
    Return a set of Crossref Types to include in analysis.
    """
    crossref_type_df = get_crossref_type_df()
    return set(crossref_type_df.query("include == 1").type_id)


# Access status categories inferred from Unpaywall data
# Colors taken from https://doi.org/10.7717/peerj.4375/fig-2
access_categories_colors = {
    'gold': '#D5BC2D',
    'hybrid/bronze': '#A66B00',
    'green': '#4AAB4E',
    'closed': '#BBBBBB',
}

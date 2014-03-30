import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from argparse import ArgumentParser


def plot_correlation_big(dataframe, filename, title='', corr_type=''):
    lang_names = dataframe.columns.tolist()
    tick_indices = np.arange(0.5, len(lang_names) + 0.5)
    plt.figure(figsize=(12, 12), dpi=1800)
    plt.pcolor(dataframe.values, cmap='RdBu', vmin=-2, vmax=2)
    colorbar = plt.colorbar()
    colorbar.set_label(corr_type)
    plt.title(title)
    plt.xticks(tick_indices, lang_names, rotation='vertical')
    plt.yticks(tick_indices, lang_names)
    plt.savefig(filename)


def plot_correlation(dataframe, filename, title='', corr_type=''):
    lang_names = dataframe.columns.tolist()
    tick_indices = np.arange(0.5, len(lang_names) + 0.5)
    plt.figure()
    plt.pcolor(dataframe.values, cmap='RdBu', vmin=-1, vmax=1)
    colorbar = plt.colorbar()
    colorbar.set_label(corr_type)
    plt.title(title)
    plt.xticks(tick_indices, lang_names, rotation='vertical')
    plt.yticks(tick_indices, lang_names)
    plt.savefig(filename)


def plot_correlation_vmin2(dataframe, filename, title='', corr_type=''):
    lang_names = dataframe.columns.tolist()
    tick_indices = np.arange(0.5, len(lang_names) + 0.5)
    plt.figure()
    plt.pcolor(dataframe.values, cmap='RdBu', vmin=-.2, vmax=.2)
    colorbar = plt.colorbar()
    colorbar.set_label(corr_type)
    plt.title(title)
    plt.xticks(tick_indices, lang_names, rotation='vertical')
    plt.yticks(tick_indices, lang_names)
    plt.savefig(filename)


def main():
    parser = ArgumentParser()
    parser.add_argument("number")
    args = parser.parse_args()
    howmany = int(args.number)
    iter = 0
    #quit()

    pushes = pd.read_csv('stacked_language_by_user.csv').pivot(
        index='actor',
        columns='repository_language',
        values='pushes')

    popular = pushes.select(lambda x: np.sum(pushes[x]) > 1000, axis=1)
    popular2 = pushes.select(
        lambda x: np.sum(pushes[x]) > 50000, axis=1).fillna(0)

    pearson_corr = popular.corr()
    plot_correlation_big(
        pearson_corr,
        'pearson_language_correlation_big.svg',
        title='2013 GitHub Language Correlations, sum(pushes[x]) > 1000',
        corr_type='Pearson\'s Correlation')

    spearman_corr = popular.corr(method='spearman')
    plot_correlation_big(
        spearman_corr,
        'spearman_language_correlation_big.svg',
        title='2013 GitHub Language Correlations, sum(pushes[x]) > 1000',
        corr_type='Spearman\'s Rank Correlation')

    pearson_corr_db2 = popular2.corr()
    plot_correlation_big(
        pearson_corr_db2,
        'pearson_language_correlation_big_denoise.svg',
        title='2013 GitHub Language Correlations',
        corr_type='Pearson\'s Correlation')

    spearman_corr_db2 = popular2.corr(method='spearman')
    plot_correlation_big(
        spearman_corr_db2,
        'spearman_language_correlation_big_denoise.svg',
        title='2013 GitHub Language Correlations',
        corr_type='Spearman\'s Rank Correlation')

    pearson_corr = popular2.corr()
    plot_correlation(
        pearson_corr,
        'pearson_language_correlation_denoise_onaxis-01.svg',
        title='2013 GitHub Language Correlations',
        corr_type='Pearson\'s Correlation')

    spearman_corr = popular2.corr(method='spearman')
    plot_correlation(
        spearman_corr,
        'spearman_language_correlation_denoise_onaxis-01.svg',
        title='2013 GitHub Language Correlations',
        corr_type='Spearman\'s Rank Correlation')

    '''kendall_corr = popular2.corr(method='kendall')
    plot_correlation(
        kendall_corr,
        'kendall_language_correlation.svg',
        title='2013 GitHub Language Correlations',
        corr_type='Kendall\'s Rank Correlation')'''

    pearson_corr2 = popular2.corr()
    plot_correlation_vmin2(
        pearson_corr2,
        'pearson_language_correlation_denoise.svg',
        title='2013 GitHub Language Correlations',
        corr_type='Pearson\'s Correlation')

    spearman_corr2 = popular2.corr(method='spearman')
    plot_correlation_vmin2(
        spearman_corr2,
        'spearman_language_correlation_denoise.svg',
        title='2013 GitHub Language Correlations',
        corr_type='Spearman\'s Rank Correlation')

    '''kendall_corr2 = popular2.corr(method='kendall')
    plot_correlation_vmin2(
        kendall_corr2,
        'kendall_language_correlation_vmin2.svg',
        title='2013 GitHub Language Correlations',
        corr_type='Kendall\'s Rank Correlation')'''


if __name__ == '__main__':
    main()

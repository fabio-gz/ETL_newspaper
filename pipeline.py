import subprocess
import datetime
import logging
logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)
news_sites_uids = ['vanguardia']
date_e = datetime.datetime.now().strftime('%Y_%m_%d')


def main():
    _extract()
    _transform()
    _load()


def _extract():
    logger.info('Starting extract process')
    for news_site_uid in news_sites_uids:
        subprocess.run(['python3', 'main.py', news_site_uid], cwd='./Extract')
        subprocess.run(['find', '.', '-name', '{}*'.format(news_site_uid),
                        '-exec', 'mv', '{}', '../Transform/{}_{}_articles.csv'.format(news_site_uid, date_e), ';'],
                       cwd='./Extract')


def _transform():
    logger.info('Starting transform process')
    for news_site_uid in news_sites_uids:
        dirty_data_filename = '{}_{}_articles.csv'.format(
            news_site_uid, date_e)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(
            ['python3', 'news_cleaning.py', dirty_data_filename], cwd='./Transform')
        subprocess.run(['rm', dirty_data_filename], cwd='./Transform')
        subprocess.run(['mv', clean_data_filename,
                        '../Load/{}.csv'.format(news_site_uid)], cwd='./Transform')


def _load():
    logger.info('Starting loading process')
    for news_site_uid in news_sites_uids:
        clean_data_filename = '{}.csv'.format(news_site_uid)
        subprocess.run(
            ['python3', 'main.py', clean_data_filename], cwd='./Load')
        subprocess.run(['rm', clean_data_filename], cwd='./Load')


if __name__ == '__main__':
    main()

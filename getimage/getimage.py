from icrawler.builtin import BingImageCrawler

crawler=BingImageCrawler(storage={"root_dir":"C:\Python_Work\Pycharm\getimage\\download"})
crawler.crawl(keyword="みかん",max_num=10)
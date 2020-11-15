# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

# steps
# 1. add connection
# 2. add cursor
# 3. create table
# 4. fill value
# 5. commit
# 6. close


import sqlite3


class ScrapperassignmentPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('news.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS article_tb""")
        self.curr.execute("""create table article_tb(
                date_published text,
                title text,
                detail text,
                news_from text,
                url text
                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("insert into article_db values (?,?,?,?,?)", (
            item['date_published'],
            item['title'],
            item['detail'],
            item['news_from'],
            item['url']
        ))
        self.conn.commit()

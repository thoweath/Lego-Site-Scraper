# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from LegoScraper.models import Lego, db_connect, create_lego_table


class LegoscraperPipeline(object):
    """Lego pipleline for storing scraped items to Postgres database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates lego table.
        """
        engine = db_connect()
        create_lego_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self,item,spider):
        """Save scraped data to the database.
        This method is called for every item pipeline component.
        """

        session = self.Session()
        lego = Lego(**item)

        try:
            session.add(lego)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

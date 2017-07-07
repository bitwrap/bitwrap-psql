"""
Test Db migrations
"""
import time
import unittest
import bitwrap_psql.db as pg
import bitwrap_machine as pnml
from bitwrap_psql import Storage

class SchemaTest(unittest.TestCase):
    """ deploy machine schemata to database """

    def setUp(self):

        self.options = {
            'pg-host': '127.0.0.1',
            'pg-port': 5432,
            'pg-username': 'postgres',
            'pg-password': 'bitwrap',
            'pg-database': 'bitwrap'
        }

        pg.recreate_db(**self.options)


    def test_migration(self):
        """ recreate the DB with machine schemata """

        def test_db(schema):

            pg.create_schema(
                pnml.Machine(schema),
                schema_name=schema,
                drop=False,
                **self.options
            )

            stor = Storage(schema, **self.options)
            self.assertTrue(stor.db.schema_exists())

        test_db('counter')
        test_db('vote')
        test_db('octoe')

if __name__ == '__main__':
    unittest.main(verbosity=2)

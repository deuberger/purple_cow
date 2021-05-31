import unittest
import os
import json
from app import create_app, db


class TestItems(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.items = [
                {"name": "item1"},
                {"name": "item2"},
                {"name": "item3"}
                ]

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_item_set(self):
        res = self.client().post('/item/', data=json.dumps(self.items),
                content_type="application/json")
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data)
        self.assertEqual(data[0]["name"], "item1")
        self.assertEqual(data[1]["name"], "item2")
        self.assertEqual(data[2]["name"], "item3")

    def test_item_get(self):
        pres = self.client().post('/item/', data=json.dumps(self.items),
                content_type="application/json")
        self.assertEqual(pres.status_code, 201)
        gres = self.client().get('/item/')
        self.assertEqual(gres.status_code, 200)
        data = json.loads(gres.data)
        self.assertEqual(data[0]["name"], "item1")
        self.assertEqual(data[1]["name"], "item2")
        self.assertEqual(data[2]["name"], "item3")

    def test_item_delete(self):
        pres = self.client().post('/item/', data=json.dumps(self.items),
                content_type="application/json")
        self.assertEqual(pres.status_code, 201)
        dres = self.client().delete('/item/')
        self.assertEqual(dres.status_code, 200)
        # Test to validate that result is empty list now
        gres = self.client().get('/item/')
        self.assertEqual(gres.status_code, 200)
        self.assertEqual(json.loads(gres.data), [])

    def test_item_id_get(self):
        pres = self.client().post('/item/', data=json.dumps(self.items),
                content_type="application/json")
        self.assertEqual(pres.status_code, 201)
        pdata = json.loads(pres.data)
        gres = self.client().get(
            '/item/{}'.format(pdata[1]['id']))
        self.assertEqual(gres.status_code, 200)
        gdata = json.loads(gres.data)
        self.assertEqual(gdata["name"], "item2")

    def test_item_id_get(self):
        pres = self.client().post('/item/', data=json.dumps(self.items),
                content_type="application/json")
        self.assertEqual(pres.status_code, 201)
        pdata = json.loads(pres.data)
        put_res = self.client().put(
            '/item/{}'.format(pdata[1]['id']),
            data = {"name": "Freddy"})
        self.assertEqual(put_res.status_code, 200)
        gres = self.client().get(
            '/item/{}'.format(pdata[1]['id']))
        self.assertEqual(gres.status_code, 200)
        gdata = json.loads(gres.data)
        self.assertEqual(gdata["name"], "Freddy")

    #def test_bucketlist_deletion(self):
    #    """Test API can delete an existing bucketlist. (DELETE request)."""
    #    rv = self.client().post(
    #        '/bucketlists/',
    #        data={'name': 'Eat, pray and love'})
    #    self.assertEqual(rv.status_code, 201)
    #    res = self.client().delete('/bucketlists/1')
    #    self.assertEqual(res.status_code, 200)
    #    # Test to see if it exists, should return a 404
    #    result = self.client().get('/bucketlists/1')
    #    self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

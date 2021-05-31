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
        res = self.client().post('/item/', data=json.dumps(self.items),
                content_type="application/json")
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/item/')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data[0]["name"], "item1")
        self.assertEqual(data[1]["name"], "item2")
        self.assertEqual(data[2]["name"], "item3")

    #def test_api_can_get_bucketlist_by_id(self):
    #    """Test API can get a single bucketlist by using it's id."""
    #    rv = self.client().post('/bucketlists/', data=self.bucketlist)
    #    self.assertEqual(rv.status_code, 201)
    #    result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
    #    result = self.client().get(
    #        '/bucketlists/{}'.format(result_in_json['id']))
    #    self.assertEqual(result.status_code, 200)
    #    self.assertIn('Go to Borabora', str(result.data))

    #def test_bucketlist_can_be_edited(self):
    #    """Test API can edit an existing bucketlist. (PUT request)"""
    #    rv = self.client().post(
    #        '/bucketlists/',
    #        data={'name': 'Eat, pray and love'})
    #    self.assertEqual(rv.status_code, 201)
    #    rv = self.client().put(
    #        '/bucketlists/1',
    #        data={
    #            "name": "Dont just eat, but also pray and love :-)"
    #        })
    #    self.assertEqual(rv.status_code, 200)
    #    results = self.client().get('/bucketlists/1')
    #    self.assertIn('Dont just eat', str(results.data))

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
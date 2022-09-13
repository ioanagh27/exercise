import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        # assert res.json['message'] == 'Hello to my flower shop!'

    def test_get_flowers(self, api):
        res = api.get('/flowers')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_flower(self, api):
        res = api.get('/flowers/2')
        assert res.status == '200 OK'
        assert res.json[0]['name'] == 'test2'

    def test_get_flower_error(self, api):
        res = api.get('/flowers/8')
        assert res.status == '404 NOT FOUND'
        assert "No flower with this id 8" in res.json['message']

    def test_post_flowers(self, api):
        mock_data = json.dumps({'name': 'sunflower'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/flowers', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 3

    def test_delete_flower(self, api):
        res = api.delete('/flowers/1')
        assert res.status == '200 OK'

    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops' in res.json['message']
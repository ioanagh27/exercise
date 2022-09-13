from werkzeug import exceptions

flowers = [
    {'id': 1, 'name': 'rose', 'colour': 'white', 'water': True},
    {'id': 2, 'name': 'orchid', 'colour': 'purple', 'water': False},
    {'id': 3, 'name': 'tulip', 'colour': 'red', 'water': True},
    {'id': 4, 'name': 'cactus', 'colour': 'green', 'water': False},
    {'id': 5, 'name': 'bluebell', 'colour': 'blue', 'water': True},
    {'id': 6, 'name': 'sunflower', 'colour': 'yellow', 'water': True}
]

def index(req):
    return [f for f in flowers], 200

def create(req):
    new_flower = req.get_json()
    new_flower['id'] = sorted([f['id'] for f in flowers])[-1] +1
    flowers.append(new_flower)
    return new_flower, 201

def show(req, uid):
    return find_by_uid(uid), 200

def update(req, uid):
    flower = find_by_uid(uid)
    data = req.get_json()
    for key, val in data.items():
        flower[key] = val
    return flower, 200

def destroy(req, uid):
    flower = find_by_uid(uid)
    flowers.remove(flower)
    return flower, 204

def find_by_uid(uid):
    try:
        return next(f for f in flowers if f['id'] == uid)
    except:
        raise exceptions.NotFound(f"No flower with this id {uid}")

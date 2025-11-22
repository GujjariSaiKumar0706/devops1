from app import app 

def test_get_students():
    tester = app.test_client()
    response = tester.get('/students')
    assert response.status_code == 200
    
def test_add_student():
    tester = app.test_client()
    response = tester.post('/new-student', json={'id': 2, 'name': 'Bob', 'age': 22})
    assert response.status_code == 201

def test_update_student():
    tester = app.test_client()
    response = tester.patch('/update-student/0', json={'age': 21})
    assert response.status_code == 200  
    
def test_delete_student():
    tester = app.test_client()
    response = tester.delete('/delete-student/0')
    assert response.status_code == 200
def test_get_post(post_api):
    response = post_api.get_post(1)
    assert response.status_code ==200
    data = response.json()
    assert data["id"]==1
def test_get_posts_by_user(post_api):
    response = post_api.get_posts_by_user(1)
    assert response.status_code ==200
    data = response.json()
    assert isinstance(data,list)
    assert len(data)>0 
    for post in data:
        assert post["userId"]==1

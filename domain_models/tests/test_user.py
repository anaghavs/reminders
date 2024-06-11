from domain_models.user import User

def test_user_model():
    name = "Anagha Shenoy"
    email = "anagha.1512@gmail.com"
    password_hash = "1234"
    user1 = User(name=name, email=email, password_hash=password_hash)
    user2 = User(name=name, email=email, password_hash=password_hash)

    assert user1.name == name
    assert user1.email == email
    assert user1.password_hash == password_hash 

    assert user1 == user2
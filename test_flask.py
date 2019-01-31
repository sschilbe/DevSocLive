import pytest
from app.models import User

def test_new_user():
    """Test creating a new user"""
    user = User(username='seth.schilbe@gmail.com',email='FlaskIsAwesome')
    assert user.username == 'seth.schilbe@gmail.com'
    assert user.password_hash != 'FlaskIsAwesome'
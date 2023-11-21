import httpx
import pytest 


@pytest.mark.asyncio
async def test_sign_new_user(default_client:httpx.AsyncClient) -> None:
    payload = {
        'email' : 'testuser1111111@test.com',
        'password':'testpassword'
        
    }
    
    headers = {
        'accept':'application/json', 
        'Content-Type':'application/json'
    }
    
    test_response = {
        'message':'User successfully registered!'
    }
    
    response = await default_client.post('/user/signup', json=payload, headers=headers)
    
    assert response.status_code == 200 
    assert response.json() == test_response 


@pytest.mark.asyncio 
async def test_sign_in_user(default_client:httpx.AsyncClient) -> None : 
    payload = {
        'email' : 'testuser1111111@test.com',
        'password':'testpassword'    
    }
    
    headers = {
        'accept':'application/json', 
        'Content-Type':'application/json'
        
    }
    
    response = await default_client.post('/user/signin', json=payload, headers=headers)
    
    assert response.status_code == 200 
    assert response.json()['token_type'] == 'Bearer' 
  

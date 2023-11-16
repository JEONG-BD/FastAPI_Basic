from fastapi import Depends, HTTPException, status 
from fastapi.security import OAuth2AuthorizationCodeBearer 
from auth.jwt_handler import verify_access_token 

oauth2_schema = OAuth2AuthorizationCodeBearer(tokenUrl="/user/signin")

async def authenticate(token:str = Depends(oauth2_schema)) ->str:
    if not token:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN, 
            detail = 'Sign in for access'
        )
    
    decoded_token = verify_access_token(token)
    return decoded_token 
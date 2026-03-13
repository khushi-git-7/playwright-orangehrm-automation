def test_api_get(playwright):
    request=playwright.request.new_context(
        extra_http_headers={
            "Accept":"application/json",
            "authorization":"Bearer session_token",
            "x-api-key":"reqres_5cb73c570e7444efb36f9d2e8c76386b"
        }
    )
    response=request.get("https://reqres.in/api/users?page=2")  
    
    assert response.status==200
    json_data=response.json()
    print(json_data)
    
    assert json_data["data"][3]["first_name"]=="Byron"
    assert json_data["data"][4]["last_name"]=="Edwards"
    
    request.dispose()
    print("test completed successfully")
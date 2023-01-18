# EXPENSE TRACKER APP


## Running the app


***Installing packages*** 

```
    pip install flask
        
```


## App
    - accessKey
    - secretKey
    - item_types
    - users
        - email
        - password
        - usernames
        - purchases
            - Date
                - list of purchases on that date
                    - item_id       
                    - item_name
                    - item_type
                    - item_price
                    - purchase_time

## API PLANNING

 01. Signing up an user

    ```
    route: /signup
    method: POST
    request_body:
        type: form-data
        data: name
              email
              password
              username
    response_body: "User signed up successfully"
    ```

02. Logging in user
```
    route: /login
    method: POST
    request_body:
        type: form-data
        data: email/username
              password
    response_body: user_idx
                   "User logged in successfully"
```

03. Add a purchase
```
    route: /add_purchase_today
    method: POST
    request_body: 
        type: form-data
        data:   user_idx
                item_name
                item_type
                item_price
                purchase_time
        response_body: "Purchase added successfully
```
    
04. Delete a purchase
```
    route: /delete_purchase
    method: DELETE
    request_body: 
        type: form-data
        data:   user_idx
                item_id
        response_body: "Purchase deleted successfully
```


05. Get all purchases for today
```
    route: /get_purchases_today
    method: GET
    request_body:
        data: user_idx
    response_body:
        list of all purchases in the following format:
            [
                {
                    "item_name": "", "item_price":"", "item_type":"", "purchase_time":""
                }
            ]
```

06. Get all purchases from start date and end date
```
    route: /get_purchases_date_specific
    method: [GET, POST]
    request_body:
        data:   user_idx
                start_date
                end_date
    response_body:
        list of all purchases in the following format:
            {
                date: [
                    {
                        "item_name": "", "item_price":"", "item_type":"", "purchase_time":""
                    }
                ]
            }
```

07. Get the average amount of purchase till now

```
    route: /get_purchases_average
    method: GET
    request_body:
        data:   user_idx
    response_body:    
            {
                average: <average_amount/>
            }
```

08. Get the most purchased item
```
    route: /get_purchases_most_frequency
    method: GET
    request_body:
        data:   user_idx
    response_body:    
            {
                item: <item/>
            }
```




## Technologies

- python
- flask
- json
- os
- pytz
- uuid
- datetime
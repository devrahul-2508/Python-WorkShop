```
App
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
                    - item_name
                    - item_type
                    - item_price
                    - purchase_time

# API PLANNING

-> Signing up an user
    route: /signup
    method: POST
    request_body:
        type: form-data
        data: name
              email
              password
              username
    response_body: "User signed up successfully"

-> Logging in user
    route: /login
    method: POST
    request_body:
        type: form-data
        data: email/username
              password
    response_body: user_id
                   message

-> Add a purchase
    route: /add_purchase
    method: POST
    request_body:
        type: form-data
        data: {
            userId,
            item_name
            item_price,
            item_type,
            purchase_time
        }
    response_body: user_id
                   message
    
<!-- -> Delete a purchase -->

-> Get all purchases for today
    route: /get_purchases_today
    method: GET
    request_body:
        data: user_id
    response_body:
        list of all purchases in the following format:
            [
                {
                    "item_name": "", 
                    "item_price":"", 
                    "item_type":"", 
                    "purchase_time":""
                }
            ]
-> Get all purchases from start date and end date
    route: /get_all_purchases
    method: GET
    request_body:
        data: {
            user_id,
            start_date,
            end_date
        }
    response_body:
        list of all purchases in the following format:
            [
                {
                    "item_name": "", 
                    "item_price":"", 
                    "item_type":"", 
                    "purchase_time":""
                }
            ]

-> Get the average amount of purchase till now
    route: /get_purchases_avg
    method: GET
    request_body:
        data: user_id
    response_body:
        list of all purchases in the following format:
            {
                avg
            }

-> Get the most purchased item
    route: /get_most_purchase
    method: GET
    request_body:
        data: user_id
    response_body:
        {
            "item_name": "", 
            "item_price":"", 
            "item_type":""
        }
            


# Planning APIs as admin user
```
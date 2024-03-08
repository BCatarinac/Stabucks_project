new_column_names = {'1. Your Gender': 'gender', '2. Your Age': 'age', 
                   '3. Are you currently....?': 'occupation', '4. What is your annual income?': 'income', 
                   '5. How often do you visit Starbucks?': 'visits', 
                   '6. How do you usually enjoy Starbucks?': 'meal_type', 
                   '7. How much time do you normally  spend during your visit?': 'time_spent', 
                   "8. The nearest Starbucks's outlet to you is...?": 'distance', 
                   '9. Do you have Starbucks membership card?': 'member', 
                   '10. What do you most frequently purchase at Starbucks?': 'purchase', 
                   '11. On average, how much would you spend at Starbucks per visit?': 'money_spent', 
                   '12. How would you rate the quality of Starbucks compared to other brands (Coffee Bean, Old Town White Coffee..) to be:': 'quality_rating', 
                   '13. How would you rate the price range at Starbucks?': 'price_rating', 
                   '14. How important are sales and promotions in your purchase decision?': 'sales/promotions_importance', 
                   '15. How would you rate the ambiance at Starbucks? (lighting, music, etc...)': 'ambiance_rating', 
                   '16. You rate the WiFi quality at Starbucks as..': 'wifi_quality', 
                   '17. How would you rate the service at Starbucks? (Promptness, friendliness, etc..)': 'service_rating', 
                   '18. How likely you will choose Starbucks for doing business meetings or hangout with friends?': 'starbucks_for_business_meetings/hangouts', 
                   '19. How do you come to hear of promotions at Starbucks? Check all that apply.': 'promotions_source', 
                   '20. Will you continue buying at Starbucks?': 'will_return'}




category_mapping = {
    "coffee": "coffee",
    "cold_drinks": "cold drinks",
    "pastries": "pastries",
    "sandwiches": "sandwiches",
    "juices": "others",
    "cake": "others",
    "jaws_chip": "others",
}




aggregated_purchase = {
    'coffee': 81, 
    'cold drinks': 36, 
    'pastries': 16, 
    'sandwiches': 8, 
    'others': 6
}




promotions_mapping = {
    "social_media": "social_media",
    "through_friends_and_word_of_mouth": "through_friends_and_word_of_mouth",
    "in_store_displays": "in_store_displays ",
    "starbucks_website/apps": "website/apps",
    "emails": "others",
    "billboards": "others",
    "deal_sites_(fave,_iprice,_etc...)": "others",
    "application_offer" : "others",
}



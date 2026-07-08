def process_user_data(user_input,is_admin):
    if not user_input:
        return "no data"
    
    role ="super user" if is_admin else "regular user"
    
    return f" processing {len(user_input)} for {is_admin} "




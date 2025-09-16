from functools import wraps

def check_admin(func):
    @wraps(func)
    def wrapper(name, password):
        if name == "admin" and password == "1234":
            return func(True)
        else:
            return func(False)
    return wrapper  # <- Missing return in your code
        

@check_admin
def show_admin_status(is_admin):
    print(f"Admin: {is_admin}")


# Example usage:
show_admin_status("admin", "1234")   # ✅ prints "Admin: True"
show_admin_status("user", "abcd")    # ✅ prints "Admin: False"

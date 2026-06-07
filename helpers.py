from faker import Faker

fake = Faker()


def generate_name():
    return fake.first_name()


def generate_login():
    return fake.email()


def generate_pass():
    return fake.password()

def generate_user_data():
    email = fake.email(15)
    password = fake.password(15)
    name = fake.first_name(10)
    return {
        "email": email,
        "password": password,
        "name": name
    }
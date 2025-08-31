def build_profile(first_name, last_name, **kwargs):
    profile = {"first_name": first_name, "last_name": last_name}

    for key, value in kwargs.items():
        profile[key] = value

    return profile

print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}
Company = {
    "ceo": "Ahmed",
    "departments": {
        "engineering": {
            "manager": "Sara",
            "team_size": 12,
            "projects": ["Backend API", "Mobile App"],
        },
        "design": {
            "manager": "Omar",
            "team_size": 5,
            "projects": ["Website Redesign"],
        },
    },
}

print(f"CEO : {Company['ceo']}")
print(f"Engineering manager : {Company['departments']['engineering']['manager']}")
print(f"Design team size : {Company['departments']['design']['team_size']}")
print(f"First engineering project : {Company['departments']['engineering']['projects'][0]}")
print(f"Total team size : {Company['departments']['engineering']['team_size'] + Company['departments']['design']['team_size']}")

Company["departments"]["design"]["team_size"] = 6

Company["departments"]["marketing"] = {
    "manager": "Lina",
    "team_size": 3,
    "projects": [],
}

print("Marketing :", Company["departments"]["marketing"])
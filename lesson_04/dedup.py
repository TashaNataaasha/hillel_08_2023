users = ["jhon", "marry", "jack", "jhon", "marry", "mark"]

users_gen = (user for users in users )
# users_seen = set()

# for user in users:
#     if user in users_seen:
#         continue
#     users_seen.add(user)
#     print(user)

def dedup(collections):
    items = set()
    for item in collections:
        if item in items:
            continue 
        items.add(item)
        yield item
        
        
users_dedup = (user for user in dedup(users))



for user in dedup(users):
    print(user)
def update_vote_count(obj, choice):
    if choice == 'upvote':
        obj.upvotes += 1
    elif choice == 'downvote':
        obj.downvotes += 1
    obj.save()
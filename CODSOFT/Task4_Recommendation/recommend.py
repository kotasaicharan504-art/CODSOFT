movies = {
    "action": ["KGF", "Pushpa", "Salaar"],
    "comedy": ["Jathi Ratnalu", "F2", "MAD"],
    "love": ["Hi Nanna", "Sita Ramam", "Geetha Govindam"]
}

print("=== Movie Recommendation System ===")
print("Choose genre: action / comedy / love")

genre = input("Enter genre: ").lower()

if genre in movies:
    print("Recommended Movies:")
    
    for movie in movies[genre]:
        print("-", movie)

else:
    print("Genre not found")
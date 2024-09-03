def greet(language):
    match language:
        case "en":
            return "Hi!"
        case "fr":
            return "Salut!"
        case "pt":
            return "Ola!"
        case "sv":
            return "Hej!"


print(greet("en"))

mystr = "Cooking like a chef, i am a 5 star michellin"
mysubstr = input()

def search_substr(subst, st):
    if subst.lower() in st.lower():
        return "Есть контакт!"
    else:
        return "Мимо!"

print(search_substr(mysubstr, mystr))

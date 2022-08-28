

def searcher():
    import time

    book = "This is a book about bcs preparation"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("Your text is on the book")
        else:
            print("Text is not the book")

search=searcher()
print("search started")
next(search)
search.send("back")
search.close()
search.send("Rony")
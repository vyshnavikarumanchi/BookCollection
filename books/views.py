
from django.shortcuts import render

books = [
    {
        "id": 1,
        "name": "Harry Potter and the Philosopher's Stone",
        "author": "J. K. Rowling",
        "price": 499,
        "category": "Fantasy",
        "chapters": 17,
        "available_copies": 50
    },
    {
        "id": 2,
        "name": "The Alchemist",
        "author": "Paulo Coelho",
        "price": 299,
        "category": "Fiction",
        "chapters": 2,
        "available_copies": 35
    },
    {
        "id": 3,
        "name": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "price": 450,
        "category": "Fantasy",
        "chapters": 19,
        "available_copies": 42
    },
    {
        "id": 4,
        "name": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "price": 350,
        "category": "Classic",
        "chapters": 9,
        "available_copies": 28
    },
    {
        "id": 5,
        "name": "Pride and Prejudice",
        "author": "Jane Austen",
        "price": 399,
        "category": "Romance",
        "chapters": 61,
        "available_copies": 40
    },
    {
        "id": 6,
        "name": "The Hunger Games",
        "author": "Suzanne Collins",
        "price": 499,
        "category": "Adventure",
        "chapters": 27,
        "available_copies": 32
    },
    {
        "id": 7,
        "name": "The Fault in Our Stars",
        "author": "John Green",
        "price": 349,
        "category": "Romance",
        "chapters": 25,
        "available_copies": 45
    },
    {
        "id": 8,
        "name": "Atomic Habits",
        "author": "James Clear",
        "price": 599,
        "category": "Self Help",
        "chapters": 20,
        "available_copies": 55
    },
    {
        "id": 9,
        "name": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "price": 299,
        "category": "Finance",
        "chapters": 10,
        "available_copies": 38
    },
    {
        "id": 10,
        "name": "Wings of Fire",
        "author": "A. P. J. Abdul Kalam",
        "price": 350,
        "category": "Biography",
        "chapters": 16,
        "available_copies": 47
    },
]

descriptions = [
    "A young wizard discovers a magical world, makes loyal friends, and faces dangerous mysteries while learning courage, friendship, and responsibility.",
    "A shepherd follows his dreams across distant lands, discovering wisdom, love, courage, and the importance of listening to his heart.",
    "A reluctant hobbit joins an adventurous journey with dwarves, encountering mysterious creatures, hidden treasures, and unexpected challenges along the way.",
    "A mysterious millionaire pursues lost love while wealth, ambition, social expectations, and tragic circumstances shape his extraordinary American dream.",
    "Elizabeth Bennet navigates love, family expectations, social class, and misunderstandings while discovering the importance of character, honesty, and personal growth.",
    "A brave girl enters a dangerous competition where survival requires courage, intelligence, sacrifice, friendship, and resistance against an oppressive government.",
    "Two teenagers facing serious illnesses develop a beautiful relationship, discovering love, hope, friendship, courage, and meaningful moments despite difficult circumstances.",
    "Learn how small daily improvements create remarkable results through practical habits, consistent actions, effective systems, personal discipline, and lasting changes.",
    "A financial education book explains wealth building, investing, financial independence, money management, and differences between assets, liabilities, and income.",
    "Discover the inspiring journey of an Indian scientist who overcame challenges, pursued education, achieved remarkable success, and became a respected president."
]

extra_books = [
    ("The Little Prince", "Antoine de Saint-Exupery", "Fiction"),
    ("1984", "George Orwell", "Dystopian"),
    ("Animal Farm", "George Orwell", "Political Fiction"),
    ("The Kite Runner", "Khaled Hosseini", "Fiction"),
    ("The Book Thief", "Markus Zusak", "Historical Fiction"),
    ("To Kill a Mockingbird", "Harper Lee", "Classic"),
    ("The Silent Patient", "Alex Michaelides", "Thriller"),
    ("The Psychology of Money", "Morgan Housel", "Finance"),
    ("Deep Work", "Cal Newport", "Self Help"),
    ("Think and Grow Rich", "Napoleon Hill", "Self Help"),
    ("The Power of Habit", "Charles Duhigg", "Self Help"),
    ("Ikigai", "Hector Garcia and Francesc Miralles", "Self Help"),
    ("The Secret", "Rhonda Byrne", "Self Help"),
    ("The Monk Who Sold His Ferrari", "Robin Sharma", "Fiction"),
    ("The Diary of a Young Girl", "Anne Frank", "Biography"),
    ("Sapiens", "Yuval Noah Harari", "History"),
    ("A Brief History of Time", "Stephen Hawking", "Science"),
    ("The Lord of the Rings", "J. R. R. Tolkien", "Fantasy"),
    ("Dune", "Frank Herbert", "Science Fiction"),
    ("The Chronicles of Narnia", "C. S. Lewis", "Fantasy"),
    ("The Da Vinci Code", "Dan Brown", "Mystery"),
    ("Angels and Demons", "Dan Brown", "Thriller"),
    ("Inferno", "Dan Brown", "Thriller"),
    ("The Lost Symbol", "Dan Brown", "Mystery"),
    ("Origin", "Dan Brown", "Thriller"),
    ("The Girl on the Train", "Paula Hawkins", "Thriller"),
    ("Gone Girl", "Gillian Flynn", "Mystery"),
    ("The Shining", "Stephen King", "Horror"),
    ("It", "Stephen King", "Horror"),
    ("Carrie", "Stephen King", "Horror"),
    ("The Stand", "Stephen King", "Horror"),
    ("The Green Mile", "Stephen King", "Fiction"),
    ("The Notebook", "Nicholas Sparks", "Romance"),
    ("A Walk to Remember", "Nicholas Sparks", "Romance"),
    ("Dear John", "Nicholas Sparks", "Romance"),
    ("The Last Song", "Nicholas Sparks", "Romance"),
    ("Me Before You", "Jojo Moyes", "Romance"),
    ("After You", "Jojo Moyes", "Romance"),
    ("Still Me", "Jojo Moyes", "Romance"),
    ("The Time Traveler's Wife", "Audrey Niffenegger", "Romance"),
    ("The Lovely Bones", "Alice Sebold", "Fiction"),
    ("Life of Pi", "Yann Martel", "Adventure"),
    ("The White Tiger", "Aravind Adiga", "Fiction"),
    ("The Palace of Illusions", "Chitra Banerjee Divakaruni", "Mythology"),
    ("The Immortals of Meluha", "Amish Tripathi", "Mythology"),
    ("The Secret of the Nagas", "Amish Tripathi", "Mythology"),
    ("The Oath of the Vayuputras", "Amish Tripathi", "Mythology"),
    ("Five Point Someone", "Chetan Bhagat", "Fiction"),
    ("2 States", "Chetan Bhagat", "Romance"),
    ("Half Girlfriend", "Chetan Bhagat", "Romance"),
    ("One Indian Girl", "Chetan Bhagat", "Fiction"),
    ("Revolution 2020", "Chetan Bhagat", "Fiction"),
    ("The 3 Mistakes of My Life", "Chetan Bhagat", "Fiction"),
    ("The Blue Umbrella", "Ruskin Bond", "Fiction"),
    ("The Room on the Roof", "Ruskin Bond", "Fiction"),
    ("A Flight of Pigeons", "Ruskin Bond", "Historical Fiction"),
    ("The Guide", "R. K. Narayan", "Fiction"),
    ("Malgudi Days", "R. K. Narayan", "Short Stories"),
    ("Swami and Friends", "R. K. Narayan", "Fiction"),
    ("The Bachelor of Arts", "R. K. Narayan", "Fiction"),
    ("The Vendor of Sweets", "R. K. Narayan", "Fiction"),
    ("The Financial Expert", "R. K. Narayan", "Fiction"),
    ("The English Teacher", "R. K. Narayan", "Fiction"),
    ("Train to Pakistan", "Khushwant Singh", "Historical Fiction"),
    ("Midnight's Children", "Salman Rushdie", "Fiction"),
    ("The God of Small Things", "Arundhati Roy", "Fiction"),
    ("A Suitable Boy", "Vikram Seth", "Fiction"),
    ("The Namesake", "Jhumpa Lahiri", "Fiction"),
    ("Interpreter of Maladies", "Jhumpa Lahiri", "Short Stories"),
    ("Unaccustomed Earth", "Jhumpa Lahiri", "Short Stories"),
    ("The Lowland", "Jhumpa Lahiri", "Fiction"),
    ("The Great Indian Novel", "Shashi Tharoor", "Satire"),
    ("India After Gandhi", "Ramachandra Guha", "History"),
    ("The Discovery of India", "Jawaharlal Nehru", "History"),
    ("My Experiments with Truth", "Mahatma Gandhi", "Autobiography"),
    ("Ignited Minds", "A. P. J. Abdul Kalam", "Motivation"),
    ("India 2020", "A. P. J. Abdul Kalam", "Development"),
    ("Turning Points", "A. P. J. Abdul Kalam", "Biography"),
    ("You Are Born to Blossom", "A. P. J. Abdul Kalam", "Motivation"),
    ("The Power of Your Subconscious Mind", "Joseph Murphy", "Self Help"),
    ("How to Win Friends and Influence People", "Dale Carnegie", "Self Help"),
    ("The 7 Habits of Highly Effective People", "Stephen Covey", "Self Help"),
    ("The 5 AM Club", "Robin Sharma", "Self Help"),
    ("Who Will Cry When You Die?", "Robin Sharma", "Self Help"),
    ("The Leader Who Had No Title", "Robin Sharma", "Self Help"),
    ("The Alchemist's Daughter", "Katharine McMahon", "Historical Fiction"),
    ("The Midnight Library", "Matt Haig", "Fiction"),
    ("The House in the Cerulean Sea", "TJ Klune", "Fantasy"),
    ("The Song of Achilles", "Madeline Miller", "Mythology"),
    ("Circe", "Madeline Miller", "Mythology"),
    ("The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", "Fiction"),
    ("Daisy Jones and The Six", "Taylor Jenkins Reid", "Fiction"),
    ("Malibu Rising", "Taylor Jenkins Reid", "Fiction"),
    ("The Invisible Life of Addie LaRue", "V. E. Schwab", "Fantasy"),
    ("The Night Circus", "Erin Morgenstern", "Fantasy"),
    ("The Starless Sea", "Erin Morgenstern", "Fantasy"),
    ("The Priory of the Orange Tree", "Samantha Shannon", "Fantasy"),
    ("The Atlas Six", "Olivie Blake", "Fantasy"),
    ("Babel", "R. F. Kuang", "Fantasy"),
    ("Yellowface", "R. F. Kuang", "Thriller"),
]

for index, (title, author, category) in enumerate(extra_books, start=11):
    books.append({
        "id": index,
        "name": title,
        "author": author,
        "price": 200 + (index % 8) * 50,
        "category": category,
        "chapters": 10 + index % 15,
        "available_copies": 10 + (index * 7) % 45
    })

default_description = (
    "Explore a fascinating story filled with memorable characters, "
    "interesting experiences, valuable lessons, unexpected discoveries, "
    "and meaningful moments throughout this book."
)

for index, book in enumerate(books):
    if index < len(descriptions):
        book["description"] = descriptions[index]
    else:
        book["description"] = default_description


def home(request):
    try:
        selected_id = int(request.GET.get("book", 1))
    except (ValueError, TypeError):
        selected_id = 1

    selected_book = next(
        (book for book in books if book["id"] == selected_id),
        books[0]
    )

    context = {
        "books": books,
        "selected_book": selected_book,
        "total_books": len(books),
        "total_available_copies": sum(
            book["available_copies"] for book in books
        ),
    }

    return render(request, "index.html", context)

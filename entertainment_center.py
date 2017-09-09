import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy that comes to life.",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                        "A marine on an alien planet.",
                        "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.title)
school_of_rock = media.Movie("School of Rock",
                        "A music movie.",
                        "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
#print(school_of_rock.storyline)
#school_of_rock.show_trailer()
Ratatouille = media.Movie("Ratatouille",
                        "A rat is the chef.",
                        "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=bKedSHDpkvI")

midnight_in_paris = media.Movie("Midnight in Paris",
                        "An animated movie.",
                        "https://en.wikipedia.org/wiki/File:Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                        "Best movie ever.",
                        "https://en.wikipedia.org/wiki/File:HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=n-7K_OjsDCQ")

movies = [toy_story, avatar, school_of_rock, Ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

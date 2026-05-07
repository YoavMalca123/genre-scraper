from types_lib.constants import UNKNOWN

GENRE_GROUPS = {
    "Games": {
        "Action",
        "Adventure",
        "Arcade",
        "Board",
        "Card",
        "Casino",
        "Casual",
        "Educational",
        "Music",
        "Puzzle",
        "Racing",
        "Role Playing",
        "Simulation",
        "Sports",
        "Strategy",
        "Trivia",
        "Word",
    },

    "Social": {
        "Social",
        "Communication",
        "Dating",
    },

    "Media": {
        "Entertainment",
        "Video Players & Editors",
        "Music & Audio",
    },

    "Education": {
        "Education",
        "Books & Reference",
        "Libraries & Demo",
    },

    "Productivity": {
        "Productivity",
        "Business",
        "Tools",
        "Personalization",
        "Photography",
    },

    "Lifestyle": {
        "Lifestyle",
        "Shopping",
        "Food & Drink",
        "Travel & Local",
        "Events",
    },

    "Utility": {
        "Finance",
        "Maps & Navigation",
        "Weather",
        "House & Home",
        "Auto & Vehicles",
    },

    "Health": {
        "Health & Fitness",
        "Medical",
        "Parenting",
    }
}


CATEGORY_DISTRACTION_VALUES = {
    "Games": 10,
    "Social": 8,
    "Media": 7,
    "Education": 6,
    "Productivity": 5,
    "Lifestyle": 4,
    "Utility": 3,
    "Health": 2,
}

def get_category(genre: str) -> str:
    for category, genres in GENRE_GROUPS.items():
        if genre in genres:
            return category
    return UNKNOWN

def get_category_distraction(genre: str) -> int:
    category = get_category(genre)
    return CATEGORY_DISTRACTION_VALUES.get(category, 0)
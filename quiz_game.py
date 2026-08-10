"""Command-line computer hardware quiz game."""


def ask_question(question, correct_answer):
    """Ask a question and return 1 for a correct answer, otherwise 0."""
    answer = input(question).strip().lower()

    if answer == correct_answer:
        print("Correct answer")
        return 1

    print("Incorrect answer!")
    return 0


def main():
    """Run the quiz game."""
    print("Welcome to my Quiz Game")

    playing = input("Do you want to play? ").strip().lower()

    if playing != "yes":
        print("Maybe next time!")
        return

    print("Okay!! Let's play the game")
    score = 0

    score += ask_question(
        "What does CPU stand for? ",
        "central processing unit",
    )
    score += ask_question(
        "What does GPU stand for? ",
        "graphics processing unit",
    )
    score += ask_question(
        "What does RAM stand for? ",
        "random access memory",
    )
    score += ask_question(
        "What does PSU stand for? ",
        "power supply unit",
    )

    print(f"Your final score: {score}")


if __name__ == "__main__":
    main()

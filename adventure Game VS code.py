#!/usr/bin/env python3
"""
Adventure Game - W03 Project

Description (creativity note):
A short branching adventure through the Mystic Forest with three distinct levels.
I showed this game to two friends who tried different paths and enjoyed discovering the endings.

Rubric requirements implemented:
- Three levels of scenarios (LEVEL 1, LEVEL 2, LEVEL 3)
- At least one scenario offers and correctly handles more than two choices
- All choices shown in ALL CAPS when asking
- Input handled case-insensitively
- Every valid choice leads to a different scenario/outcome
- Invalid input is handled (reprompt)
- Choices only valid for the current question
"""

def get_choice(prompt, valid_choices):
    """
    Prompt the user and return a validated choice (uppercased).
    valid_choices: iterable of uppercase strings (e.g., ["CAVE","MEADOW"])
    Prompts will show choices in ALL CAPS as required.
    """
    valid_set = set(valid_choices)
    # Show prompt (should include choices in ALL CAPS in the text passed)
    while True:
        user = input(prompt + "\n> ").strip().upper()
        if user in valid_set:
            return user
        print("Invalid choice. Please type one of the choices shown in ALL CAPS.")

def main():
    print("WELCOME TO THE MYSTIC FOREST!")
    print("You wake up in a foggy forest with no memory of how you got here.")
    print("Make choices shown in ALL CAPS. Choices are NOT case-sensitive.\n")

    # LEVEL 1 (two options -> leads to different LEVEL 2 branches)
    choice1 = get_choice(
        "LEVEL 1 — You see two possible ways out: a DARK CAVE or a BRIGHT MEADOW.\n"
        "Do you choose CAVE or MEADOW? (Type CAVE or MEADOW)",
        ["CAVE", "MEADOW"]
    )

    # LEVEL 2 depends on LEVEL 1
    if choice1 == "CAVE":
        # In the cave branch the second question has two clear options.
        choice2 = get_choice(
            "LEVEL 2 — Inside the CAVE you hear a DEEP GROWL and notice a MYSTERIOUS GLOW.\n"
            "Do you investigate the GROWL or the GLOW? (Type GROWL or GLOW)",
            ["GROWL", "GLOW"]
        )

        if choice2 == "GROWL":
            # LEVEL 3 for CAVE->GROWL: three choices (more than two), all handled
            choice3 = get_choice(
                "LEVEL 3 — A shadowy WOLF steps forward. You can FIGHT, RUN, or OFFER FOOD.\n"
                "What do you do? (Type FIGHT, RUN, or OFFER)",
                ["FIGHT", "RUN", "OFFER"]
            )
            if choice3 == "FIGHT":
                print("\nYou draw a branch and bravely fight. The wolf is injured but you escape.")
                print("Ending: You survive but carry a scar — wiser, and alive.")
            elif choice3 == "RUN":
                print("\nYou sprint back through the tunnel and stumble into a hidden exit.")
                print("Ending: You escape safely, but you wonder what the GLOW really was.")
            else:  # OFFER
                print("\nYou offer a bit of your snack. The wolf sniffs it, gently takes it, and becomes friendly.")
                print("Ending: The wolf leads you to a secret trove of glowing mushrooms — you gain a curious friend.")
        else:  # choice2 == "GLOW"
            # LEVEL 3 for CAVE->GLOW: three choices (more than two), all handled
            choice3 = get_choice(
                "LEVEL 3 — The GLOW is coming from a CRYSTAL on a stone pedestal. TOUCH it, TAKE it, or LEAVE it?\n"
                "What do you do? (Type TOUCH, TAKE, or LEAVE)",
                ["TOUCH", "TAKE", "LEAVE"]
            )
            if choice3 == "TOUCH":
                print("\nYou touch the crystal and visions show you the forest's memory. You remember your name.")
                print("Ending: The crystal restores a piece of your past. You leave with clarity.")
            elif choice3 == "TAKE":
                print("\nYou pocket the crystal. It hums and grows warm — then becomes heavy as regret.")
                print("Ending: The crystal bonds to you; you gain power but lose a slice of daylight.")
            else:  # LEAVE
                print("\nYou decide some things are better left undisturbed. You leave quietly.")
                print("Ending: By not taking the crystal you avoid a curse; you walk out peacefully.")
    else:
        # MEADOW branch
        choice2 = get_choice(
            "LEVEL 2 — In the MEADOW you spot a SILVER RIVER and a TALL OAK TREE with a ladder.\n"
            "Do you go to the RIVER or CLIMB the TREE? (Type RIVER or TREE)",
            ["RIVER", "TREE"]
        )

        if choice2 == "RIVER":
            # LEVEL 3 for MEADOW->RIVER: three choices
            choice3 = get_choice(
                "LEVEL 3 — The river sparkles strangely. You can SWIM across, FOLLOW the river upstream, or DRINK from it.\n"
                "What do you do? (Type SWIM, FOLLOW, or DRINK)",
                ["SWIM", "FOLLOW", "DRINK"]
            )
            if choice3 == "SWIM":
                print("\nYou swim and the cool water cleanses you. On the far bank, a hidden path appears.")
                print("Ending: Rejuvenated, you follow the path to a village of friendly travelers.")
            elif choice3 == "FOLLOW":
                print("\nYou follow the river upstream and find a waterfall with a hidden cave behind it.")
                print("Ending: The cave contains a mural that tells of a heroic ancestor — you feel connected.")
            else:  # DRINK
                print("\nYou drink the water. It tastes like summertime and courage flows through you.")
                print("Ending: Suddenly confident, you set off to map the forest and tell others of your journey.")
        else:  # TREE
            # LEVEL 3 for MEADOW->TREE: three choices
            choice3 = get_choice(
                "LEVEL 3 — Up the TREE you find a platform with a BIRD'S NEST, a KEY hanging on a branch, and a HOLE.\n"
                "Do you LOOK (inside the nest), TAKE the KEY, or CLIMB HIGHER? (Type LOOK, TAKE, or CLIMB)",
                ["LOOK", "TAKE", "CLIMB"]
            )
            if choice3 == "LOOK":
                print("\nYou peek into the nest and find a tiny map tucked under some twigs.")
                print("Ending: The map points to a grotto where you find shelter and friendly faces.")
            elif choice3 == "TAKE":
                print("\nYou take the key. It fits a rusty lock on a trunk at the base of the tree.")
                print("Ending: Inside the trunk you find letters from someone who once lived here — a new family history.")
            else:  # CLIMB
                print("\nYou climb higher to see the whole forest. From above, you spot smoke from a distant cabin.")
                print("Ending: You climb down and head to the cabin, where a kind stranger offers help and food.")

    # Extra small interactive wrap-up to emphasize different outcomes
    print("\n--- GAME OVER ---")
    print("Thanks for playing! Try different paths next time to discover all endings.")

if __name__ == "__main__":
    main()

from generator import generate_test_cases, save_to_json


def main():
    print("=== Agentic Game QA ===")

    mode = input("Enter game mode (battle royale / pvp / team deathmatch): ").strip().lower()
    feature = input("Enter feature to test: ").strip()

    test_cases = generate_test_cases(mode, feature)

    if not test_cases:
        print("\nMode not recognized.")
        print("Please enter: battle royale, pvp, or team deathmatch.")
        return

    print(f"\nGenerated test cases for {mode} - {feature}:\n")

    for test_case in test_cases:
        print(f"{test_case['id']} - {test_case['title']}")
        print(f"   Type: {test_case['type']}")
        print(f"   Priority: {test_case['priority']}")
        print(f"   Severity: {test_case['severity']}")
        print(f"   Precondition: {test_case['precondition']}")
        print("   Steps:")
        for step_index, step in enumerate(test_case["steps"], start=1):
            print(f"      {step_index}. {step}")
        print(f"   Expected Result: {test_case['expected_result']}")
        print()

    file_name = save_to_json(mode, feature, test_cases)
    print(f"Saved test cases to: {file_name}")


if __name__ == "__main__":
    main()
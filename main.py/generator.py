import json
import os


def build_test_case(title, test_type, priority, severity, precondition, steps, expected_result):
    return {
        "title": title,
        "type": test_type,
        "priority": priority,
        "severity": severity,
        "precondition": precondition,
        "steps": steps,
        "expected_result": expected_result
    }


def add_ids(test_cases):
    for index, test_case in enumerate(test_cases, start=1):
        test_case["id"] = f"TC-{index:03}"
    return test_cases


def generate_battle_royale_cases(feature):
    return [
        build_test_case(
            title=f"Verify {feature} works in normal battle royale flow",
            test_type="positive",
            priority="high",
            severity="critical",
            precondition="Player is logged in, matchmaking is available, and the match has started successfully.",
            steps=[
                f"Launch a battle royale match with {feature} enabled.",
                "Join the match and proceed through normal gameplay flow.",
                f"Trigger or use {feature} during normal gameplay.",
                "Observe gameplay behavior and UI response."
            ],
            expected_result=f"{feature} should work correctly during normal battle royale gameplay."
        ),
        build_test_case(
            title=f"Verify {feature} handles invalid or unexpected player actions",
            test_type="negative",
            priority="high",
            severity="major",
            precondition="Player is in an active battle royale session.",
            steps=[
                f"Start a match and reach a state where {feature} can be triggered.",
                "Perform invalid, unexpected, or rapid player actions.",
                f"Try to use or interrupt {feature} in an abnormal way.",
                "Observe system stability and feedback."
            ],
            expected_result=f"{feature} should fail safely without crashes, soft locks, or broken gameplay."
        ),
        build_test_case(
            title=f"Verify {feature} remains stable during final-circle pressure",
            test_type="edge case",
            priority="medium",
            severity="major",
            precondition="Player has reached a late-game or high-pressure endgame state.",
            steps=[
                "Play until the final circle or simulate endgame conditions.",
                f"Use or trigger {feature} during intense combat and zone pressure.",
                "Monitor responsiveness, animation, UI, and gameplay stability."
            ],
            expected_result=f"{feature} should remain stable and responsive during high-pressure endgame conditions."
        )
    ]


def generate_pvp_cases(feature):
    return [
        build_test_case(
            title=f"Verify {feature} works during standard PvP combat",
            test_type="positive",
            priority="high",
            severity="critical",
            precondition="Two players are matched successfully and the PvP match is active.",
            steps=[
                "Start a PvP match.",
                f"Use or trigger {feature} during normal combat.",
                "Observe gameplay response for both players.",
                "Verify UI and match state update correctly."
            ],
            expected_result=f"{feature} should work correctly in standard PvP combat."
        ),
        build_test_case(
            title=f"Verify {feature} handles disconnects or lag correctly",
            test_type="negative",
            priority="high",
            severity="critical",
            precondition="A PvP match is active and network conditions can be varied.",
            steps=[
                "Start a PvP match.",
                f"Trigger {feature} during combat.",
                "Simulate lag, packet delay, or a temporary disconnect.",
                "Observe recovery behavior after the connection changes."
            ],
            expected_result=f"{feature} should recover gracefully from lag or disconnect conditions."
        ),
        build_test_case(
            title=f"Verify {feature} remains fair for both players",
            test_type="edge case",
            priority="medium",
            severity="major",
            precondition="A balanced PvP match is active between two valid players.",
            steps=[
                f"Use {feature} repeatedly from both player perspectives.",
                "Compare results, timing, and feedback on both sides.",
                "Check whether one player gets an unfair advantage."
            ],
            expected_result=f"{feature} should behave fairly and consistently for all players."
        )
    ]


def generate_tdm_cases(feature):
    return [
        build_test_case(
            title=f"Verify {feature} works during normal team deathmatch flow",
            test_type="positive",
            priority="high",
            severity="critical",
            precondition="A team deathmatch session has started with valid teams assigned.",
            steps=[
                "Start a team deathmatch match.",
                f"Trigger or use {feature} during normal gameplay.",
                "Observe team state, UI, and gameplay flow."
            ],
            expected_result=f"{feature} should work correctly during normal team deathmatch gameplay."
        ),
        build_test_case(
            title=f"Verify {feature} handles respawn or score issues correctly",
            test_type="negative",
            priority="high",
            severity="major",
            precondition="A TDM match is active with score tracking and respawn enabled.",
            steps=[
                f"Use {feature} before a death, kill, or respawn event.",
                "Trigger repeated kills, deaths, or score updates.",
                "Observe respawn logic and score behavior."
            ],
            expected_result=f"{feature} should not break respawn logic or scoring behavior."
        ),
        build_test_case(
            title=f"Verify {feature} remains stable under repeated kills and respawns",
            test_type="edge case",
            priority="medium",
            severity="major",
            precondition="Players can repeatedly enter combat and respawn in the same TDM session.",
            steps=[
                "Play repeated combat loops with frequent kills and respawns.",
                f"Trigger {feature} across multiple cycles.",
                "Observe whether the feature remains stable over time."
            ],
            expected_result=f"{feature} should remain stable across repeated combat and respawn cycles."
        )
    ]


def generate_test_cases(mode, feature):
    if mode == "battle royale":
        test_cases = generate_battle_royale_cases(feature)
    elif mode == "pvp":
        test_cases = generate_pvp_cases(feature)
    elif mode == "team deathmatch":
        test_cases = generate_tdm_cases(feature)
    else:
        return []

    return add_ids(test_cases)


def save_to_json(mode, feature, test_cases):
    os.makedirs("outputs", exist_ok=True)

    safe_mode = mode.replace(" ", "_")
    safe_feature = feature.replace(" ", "_").lower()
    file_name = f"outputs/{safe_mode}_{safe_feature}_test_cases.json"

    data = {
        "mode": mode,
        "feature": feature,
        "test_cases": test_cases
    }

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

    return file_name
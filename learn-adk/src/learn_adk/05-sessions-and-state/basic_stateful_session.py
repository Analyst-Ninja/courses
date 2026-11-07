import asyncio
import uuid

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent import question_answering_agent  # type: ignore

# Create a new session service
session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Eren Yaegar",
    "user_preferences": """
        I like to play Pickleball, Disc Golf, and Tennis.
        My favorite food is Mexican.
        My favorite TV show is Game of Thrones.
        Loves it when people like and subscribe to his YouTube channel.
    """,
}

# Create a new session
APP_NAME = "Eren Bot"
USER_ID = "eren_yaegar"
SESSION_ID = str(uuid.uuid4())


async def main():
    stateful_session = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state,
    )

    print("NEW SESSION CREATED!!")
    print(f"SESSION ID: {SESSION_ID}")

    # runner
    runner = Runner(
        agent=question_answering_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
    )

    new_message = types.Content(
        role="user",
        parts=[types.Part(text="What is the Eren Yaegar's favorite TV show?")],
    )

    async for event in runner.run_async(
        user_id=USER_ID, session_id=SESSION_ID, new_message=new_message
    ):
        if event.is_final_response() and event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

    print("====== Session Event Exploration ======")
    session = await session_service_stateful.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    # Log Final Session State
    print("=== Final Session State ===")
    for key, value in session.state.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    asyncio.run(main())

# Project Context Resume Agent

**Project Context Resume Agent** is a lightweight AI agent that helps developers quickly resume work on a code project after time away. Instead of manually inspecting git history and recent file changes, the agent reconstructs the *mental context* of the last working session and provides a concise summary.

## What the Agent Does

Given a project directory, the agent:

- Analyzes recent git activity (commits and diffs)
- Detects recently modified files
- Builds a structured prompt from these signals
- Uses a language model to infer:
  - What was being worked on
  - Why it matters
  - The next concrete step
  - A 2-minute re-entry task
- Saves the generated context for future reference

The result is a concise summary that allows you to resume work immediately.

## Example Output
```shell
=== Project Context ===

1. What the developer was working on:
The recent work involved adding new construct objects ("nuevos constructos") and implementing a "highway" feature, although it still has bugs. Additionally, there were updates to the audio mixer system and game mode switching with music filtering.

2. Why (goal / feature / bug):
The goal was to expand the game's content by introducing new constructs and implement new features like the highway system to enhance gameplay. Audio improvements aimed for a better sound experience in different game modes. The bugs in the highway implementation indicate that this feature is not fully stable yet.

3. What the next concrete step should be:
Focus on identifying and fixing the bugs in the highway implementation to make the feature stable and playable. This may involve debugging the highway code and testing its integration with other systems such as movement, animations, and audio transitions.

4. A 2-minute re-entry task:
Load the project and open the highway-related scripts and prefabs that were recently changed (look for "Highway" in construct prefabs and scripts). Review the code sections where the new highway feature is implemented, and run the game to test the highway behavior. Observe any errors or unexpected behavior and note down where issues occur for targeted debugging next.

```
## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/denisseantunez/ProjectContextResumeAgent.git
cd ProjectContextResumeAgent
pip install openai python-dotenv
```
## LLM Configuration
This project uses the OpenAI API to generate project context summaries, but it can be easily adapted with the LLM wrapper.

**API Key Setup**  
Create a .env file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```
## How to Run
Run the agent by providing a path to the project you want to analyze:
```bash
python agent.py <project_path>
```
The agent will print the generated context to the terminal and store it in context_store.json.

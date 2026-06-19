# Documentation style guide

These are the writing rules for this project. They keep the documentation
consistent, clear, and — importantly — cheap to translate, since the same
content is often published in several languages.

## Voice and structure

- Write in the **second person** ("you") and the **active voice**: "Load the
  robot", not "the robot should be loaded".
- Use the **imperative** for instructions: "Run the script", "Open the file".
- Keep each guide in its Diátaxis category. A tutorial teaches; a how-to solves
  one task; reference describes; explanation gives background. Do not mix them.

## Sentences and terminology

- Prefer **short sentences**, one instruction each. Short, simple sentences are
  easier to read and far cheaper and more accurate to translate.
- Use **one term for one thing**, every time. The part at the end of the arm is
  always the "end effector" — not "hand", "tip", or "gripper" interchangeably.
  Consistent terminology is the single biggest lever on translation quality.
- Avoid idioms, humour, and culture-specific references. They rarely survive
  translation.
- Spell out an acronym on first use in each page.

## Formatting

- Use sentence case for headings: "Set multiple joint angles".
- Put commands and code in fenced code blocks, never inline screenshots of text.
- State units explicitly. Angles are in radians; distances are in metres.

## Standards we keep in mind

This project is a learning example, but it is written with the same standards a
product team would apply:

- **IEC/IEEE 82079-1** — the international standard for the structure and content
  of instructions for use. It drives the task-oriented, minimal-step approach
  here.
- **EU Machinery Regulation / Directive** — governs the safety information that
  must accompany machinery, including robots. Production documentation must meet
  it; this example points to where such content would live.
- **Translation-friendly authoring** — the sentence and terminology rules above
  exist so content can move into a translation workflow with minimal rework.

## Before you open a pull request

- Read your change out loud. If you run out of breath, the sentence is too long.
- Check that every new term appears in the same form everywhere.
- Confirm the page sits in the right Diátaxis category.

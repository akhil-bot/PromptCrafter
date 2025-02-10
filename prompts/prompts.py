class Prompts:
    def __init__(self):
        self.prompt_writer_prompt = """
Given a task description or existing prompt, produce a detailed system prompt to guide a language model in completing the task effectively.

# Guidelines

- Understand the Task: Grasp the main objective, goals, requirements, constraints, and expected output.
- Minimal Changes: If an existing prompt is provided, improve it only if it's simple. For complex prompts, enhance clarity and add missing elements without altering the original structure.
- Reasoning Before Conclusions**: Encourage reasoning steps before any conclusions are reached. ATTENTION! If the user provides examples where the reasoning happens afterward, REVERSE the order! NEVER START EXAMPLES WITH CONCLUSIONS!
    - Reasoning Order: Call out reasoning portions of the prompt and conclusion parts (specific fields by name). For each, determine the ORDER in which this is done, and whether it needs to be reversed.
    - Conclusion, classifications, or results should ALWAYS appear last.
- Examples: Include high-quality examples if helpful, using placeholders [in brackets] for complex elements.
   - What kinds of examples may need to be included, how many, and whether they are complex enough to benefit from placeholders.
- Clarity and Conciseness: Use clear, specific language. Avoid unnecessary instructions or bland statements.
- Formatting: Use markdown features for readability. DO NOT USE ``` CODE BLOCKS UNLESS SPECIFICALLY REQUESTED. Use ```json for JSON output. DO NOT USE H1, H2 of markdowns.
- Preserve User Content: If the input task or prompt includes extensive guidelines or examples, preserve them entirely, or as closely as possible. If they are vague, consider breaking down into sub-steps. Keep any details, guidelines, examples, variables, or placeholders provided by the user.
- Constants: DO include constants in the prompt, as they are not susceptible to prompt injection. Such as guides, rubrics, and examples.
- Output Format: Explicitly the most appropriate output format, in detail. This should include length and syntax (e.g. short sentence, paragraph, JSON, etc.)
    - For tasks outputting well-defined or structured data (classification, JSON, etc.) bias toward outputting a JSON.
    - JSON should never be wrapped in code blocks (```) unless explicitly requested.

The final prompt you output should adhere to the following structure below. Do not include any additional commentary, only output the completed system prompt. SPECIFICALLY, do not include any additional messages at the start or end of the prompt. (e.g. no "---"). DO NOT REPEAT THE TASK DESCRIPTION AS IS.

[Concise instruction describing the task - this should be the first line in the prompt, no section header and don't repeat the task description as is]

[Additional details as needed.]

[Optional sections with headings or bullet points for detailed steps.]

# Steps [optional]

[optional: a detailed breakdown of the steps necessary to accomplish the task]

# Output Format

[Specifically call out how the output should be formatted, be it response length, structure e.g. JSON, markdown, etc]

# Examples [optional]

[Optional: 1-3 well-defined examples with placeholders if necessary. Clearly mark where examples start and end, and what the input and output are. User placeholders as necessary.]
[If the examples are shorter than what a realistic example is expected to be, make a reference with () explaining how real examples should be longer / shorter / different. AND USE PLACEHOLDERS! ]

# Notes [optional]

#Input Placeholders If Necessary

[optional: edge cases, details, and an area to call or repeat out specific important considerations]
""".strip()
        
        
        self.prompt_reviewer_prompt = """
**Objective**: Enhance the clarity and effectiveness of a given prompt to ensure it aligns with the task's objectives.

**Internal Guidelines** (Not to be included in output):

1. **Understand the Task**: 
   - Analyze the main objective and goals of the prompt
   - Identify the requirements and constraints

2. **Evaluate Clarity**: 
   - Assess whether the prompt is clear and specific
   - Identify any vague or ambiguous language

3. **Identify Missing Elements**: 
   - Determine if any critical information or instructions are missing
   - Add necessary context or requirements

4. **Enhance Structure**: 
   - Organize the prompt logically
   - Use clear formatting (bullet points, sections) if needed

5. **Encourage Reasoning**: 
   - Ensure the prompt promotes step-by-step thinking
   - Include reasoning requirements if necessary

6. **Include Examples**: 
   - Add relevant examples if they help clarify
   - Use placeholders for variable elements

7. **Specify Output Format**: 
   - Define expected output structure
   - Include any format requirements

**Output Instructions**:
- Return ONLY the enhanced prompt
- Do not include any meta-text like "Revised Prompt:" or "Enhanced Version:"
- Do not include any of the internal guidelines or notes
- Maintain a clean, professional format
- Keep the original intent of the task

**Example Internal Reference** (Not to be included in output):

Task: "Write a story about a hero"

Output should be like:
Write a 500-word story about a heroic character who faces a significant challenge. Include:
- A clear description of the hero's background and motivation
- The central conflict or challenge they must overcome
- Their actions and decisions during the crisis
- The resolution and its impact
- Focus on showing their heroic qualities through actions rather than just stating them

The story should have a clear beginning, middle, and end, with emphasis on character development and meaningful consequences of the hero's actions.

**Notes**:
- Keep outputs focused and direct
- Omit any meta-commentary or revision markers
- Ensure the prompt stands alone as a complete instruction set

**Inputs**:
task: {task}
promptGenerated: {promptGenerated}
""".strip()

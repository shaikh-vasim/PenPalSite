from langchain_core.prompts.prompt import PromptTemplate


custom_prompt_template = """
Design a Modern Sans-Serif Handwriting Website

You have been provided with a layout of a handwriting website design, including the text elements and their coordinates for the four outer vertices. Your task is to create an HTML website that reflects these elements and decide which CSS properties can be used to match their relative positions. Here are the specific instructions:

1. HTML Structure:
   - Use appropriate layout tags to match the font size and relative placement based on the given coordinates.
   - If the elements appear as a menu list, use `<ul>` and `<li>` tags.
   - Smartly utilize function tags like `<button>` and `<input>` if their names suggest such functionality.
   - Remember not to use absolute coordinates in your HTML source code.

2. Design Considerations:
   - Prioritize the design based on the provided coordinates.
   - Use your imagination to enhance the layout and apply common web design principles.
   - Utilize CSS effectively to style the elements, including font selection, color scheme, margins, padding, etc.
   - Consider using CSS Flexbox or Grid layout for structuring and positioning elements.
   - Add header and footer menus only if necessary. Pay special attention to the design and styling of these menus to ensure they look visually appealing and well-designed.

3. CSS and JavaScript:
   - Include CSS and JavaScript within the HTML page itself.

 Remember, don't use absolute coordinates in your HTML source code. 
 Generate only source code file, no description: {layout}.\n

- Return the code in the following format:
     [
         ['your_html_code_here_with_css_and_js_embedded']
     ]

Remember, creativity and thoughtful design are key! 🎨🌟
"""


def set_costom_prompt():
    """
    Prompt template for QA retrieval for eacg vector stores
    """

    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['layout'])

    return prompt
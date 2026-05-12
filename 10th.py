from pydantic import BaseModel
from typing import Optional
import wikipediaapi
import re
from IPython.display import display
import ipywidgets as widgets
def fetch_ipc_content():
    user_agent = "IPCChatbot/1.0 (student project)"
    wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language='en')
    page = wiki.page("Indian Penal Code")
    if not page.exists():
        raise ValueError("❌ IPC page not found")
    return page.text
ipc_content = fetch_ipc_content()
class IPCResponse(BaseModel):
    section: Optional[str]
    explanation: Optional[str]
def get_ipc_response(question: str) -> IPCResponse:
    question = question.lower()
    section_match = re.search(r"section\s*(\d+)", question)
    section = section_match.group(1) if section_match else None
    if "theft" in question:
        return IPCResponse(
            section="378",
            explanation="Section 378 defines theft as dishonestly taking movable property out of someone's possession without consent."
        )
    elif "murder" in question:
        return IPCResponse(
            section="300",
            explanation="Section 300 defines murder as causing death with intention or knowledge."
        )
    elif "punishment for murder" in question:
        return IPCResponse(
            section="302",
            explanation="Section 302 provides punishment for murder, which may include death or life imprisonment."
        )
    elif "cheating" in question:
        return IPCResponse(
            section="415",
            explanation="Section 415 defines cheating as deceiving a person to gain unfair advantage."
        )
    else:
        if section:
            pattern = f"section {section}"
            idx = ipc_content.lower().find(pattern)
            if idx != -1:
                snippet = ipc_content[idx:idx+300]
                return IPCResponse(section=section, explanation=snippet)
        return IPCResponse(
            section=None,
            explanation="Sorry, I could not find a precise answer. Please try asking about specific IPC sections like theft, murder, cheating."
        )
def display_response(response: IPCResponse):
    print("\n🤖 IPC CHATBOT RESPONSE:\n")
    print(f"Section: {response.section or 'N/A'}")
    print(f"Explanation: {response.explanation}")
def on_button_click(b):
    question = text_box.value
    try:
        response = get_ipc_response(question)
        display_response(response)
    except Exception as e:
        print("Error:", e)
text_box = widgets.Text(
    placeholder="Ask about IPC (e.g., What is theft?)",
    description="You:"
)
button = widgets.Button(
    description="Ask",
    button_style="success",
    icon="legal"
)
button.on_click(on_button_click)
display(text_box, button)




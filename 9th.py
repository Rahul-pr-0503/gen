from pydantic import BaseModel
from typing import List, Optional
import wikipediaapi
import re
from IPython.display import display
import ipywidgets as widgets
class InstitutionDetails(BaseModel):
    founder: Optional[str]
    founded: Optional[str]
    branches: Optional[List[str]]
    number_of_employees: Optional[int]
    summary: Optional[str]
def fetch_institution_details(institution_name: str) -> InstitutionDetails:
    user_agent = "MyApp/1.0 (contact: student@example.com)"
    wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language='en')
    page = wiki.page(institution_name)
    if not page.exists():
        raise ValueError("❌ Institution not found on Wikipedia")
    text = page.text
    summary = page.summary[:500]
    year_match = re.search(r"\b(18|19|20)\d{2}\b", text)
    founded = year_match.group() if year_match else None
    founder_match = re.search(r"founded by ([A-Z][a-zA-Z\s]+)", text, re.IGNORECASE)
    founder = founder_match.group(1) if founder_match else None
    branches = None
    if "campus" in text.lower():
        branches = ["Main Campus"]
    emp_match = re.search(r"(\d{3,6}) employees", text)
    number_of_employees = int(emp_match.group(1)) if emp_match else None
    return InstitutionDetails(
        founder=founder,
        founded=founded,
        branches=branches,
        number_of_employees=number_of_employees,
        summary=summary
    )
def display_institution_details(details: InstitutionDetails):
    print("\n✅ FINAL OUTPUT:\n")
    print(f"Founder: {details.founder or 'N/A'}")
    print(f"Founded: {details.founded or 'N/A'}")
    print(f"Branches: {', '.join(details.branches) if details.branches else 'N/A'}")
    print(f"Number of Employees: {details.number_of_employees or 'N/A'}")
    print(f"Summary:\n{details.summary or 'N/A'}")
def on_button_click(b):
    institution_name = text_box.value
    try:
        details = fetch_institution_details(institution_name)
        display_institution_details(details)
    except Exception as e:
        print(e)
text_box = widgets.Text(
    value='',
    placeholder='Enter institution name',
    description='Institution:',
    style={'description_width': 'initial'}
)
button = widgets.Button(
    description='Fetch Details',
    button_style='success',
    icon='search'
)
button.on_click(on_button_click)
display(text_box, button)
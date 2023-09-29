from dotenv import load_dotenv
load_dotenv()

from utilities.AI_Lookups import Llama2LLM, LangChainLLM
from utilities.create_excel_report import write_into_excel
from utilities.prompts import get_function_calling_prompt

data_source_descriptions = [{
    "HR Information / Policy" : "Contains details about Admin Form Pages, Benefits pool, Buddy program, Business Travel Policy, Leave Policy and Calendar 2023 for India and USA based solitons, Feedback channels, Flexi-pay Benefit Plan, Grievance Redressal Policy, Guideline for [Fast Track Promotion,Virtual Connects,work-life balance], Open-Source Initiative, Person in Charge,Prevention of Sexual Harrassment, Procedure to apply reimbursement claims, Role Document for [Delivery Track, Marketing, PMO, Product Design, Quality Assurance, Sales & Account Management, Strategic Offering, Technical Solutions], Separation Policy, Soliton's [CBE Guest Houses-Policy Documenty, Handbook, Recognition Framework], Flexi-pay Benefit plan (FBP) declaration, Policy for [Team Outing & Annual Trip , Training & Development , Rewards & Recognition]",
    "IT Information" : "Contains details about the Office365 Do's and donts, IT awarness, phising content and how to report them, Approved and unapproved software list details, IT Dos and donts, Soliton IT infrastrcuture usage policy, Domain Password Reset, How to use Soliton VPN, LabView Installation Procedure, New XID Creation, Remote Desktop connection procedure, Soliton VPN Connection, VNC Connection Procedure"},
    {"Soliton Way" : "Contains details about Soliton, the Soliton Way, Soliton Values, Soliton Culture, Soliton History , Soliton Vision, Soliton Mission, Soliton Goals, Soliton Strategy, Soliton Branding"},
    {"AI Policy" :"Contains details about the Generative AI Usgae Policy"},
    {"Test Methodology" : "Contains details about the different LDO Measurements including LDO Dropout Voltage, LDO Line Regulation, LDO Line Transient, LDO Load Regulation, LDO Load Transient, LDO PSRR, LDO20xx family Characteristics. It also contains details about different measurement methodologies, procedures and test setups to make LDO measurements like Line Regulations, Load Regulations, Drop Out Voltage measurements. It also contains information on various characterization and production test methods and test setups used by High Speed Converter Groups. Call this datasource for questions related to measurement methodology of ldo and different testing methods, procedures and test setups used by High Speed Converters."},
    {"Project Management Information" : "Contains details about Soliton Quality Management System, Change Management Procedure, Customer Communication Guideline, Post Project Review Process, Procedure for Controlling Non-Conforming Products, Procedure for Corrective Action, Procedure for Document Control, Procedure to follow for Customer Delight Analysis, Risk Assessment Guideline, Sales Process, Soliton Quality Objectives, Soliton Quality Policy, Soliton Scope for QMS, STEPS Project Design Guideline, STEPS Project Design Process Guideline, STEPS Project Testing Guideline and this also has the various Forms and Templates links related to PMO."},
    {"Spartans" : "Contains information about Spartans Group Challenge 2023 where people in Soliton are involved in making 1 lakh kilometers challenge. It also contains details of each people in Soliton like Employee Id, the mission they belong, the project they are currently working on, whether they have signed up for the challenge or not, Annual Target set in kilometers, Acheieved target in kilometers, the milestone progress and number of kilometeres run by each people in each month."},
    {"Falcon" : "Contains details about the Engineer's (Employee) Information like Employee Id, Employee Name, Technology they are working or familiar with, Skill sets, Mission they are assigned to, thier email address, thier project role or designation. It also contains about the details of engineer's availability based on thier name or technology or project role. The falcon can answer to the 'Who' questions by providing the engineer's details. Also contains the details about the customers and projects."}
]

questions = ["How to apply for sick leave?","How to book soliton guest house?",
             "Whom should I contect for my doubts regarding salary deposits?", "What is Soliton Recognition framework",
             "What is the cash prize for Start Soliton Award?", "How many sick leave that I can take for a year?",
                "Which book inspired the creation of Soliton?",
                "What is the annual compounded growth rate of Soliton?",
                "What is Soliton’s Quality Policy?",
                "What is Soliton’s Sales Process? ",
                "How to kick off a project? ",
                "What is a risk tracker? ",
                "What are the testing guidelines for a project? ",
                "Can you give me the template for Project Reterospection ?",
                "Can you share me the link for Team Delight form? ",
                "What is the procedure to measure Line Regulation in LDO?",
                "How do I make drop out voltage measurement?",
                "Give me the Station Configuration for LDO PSSR?",
                "How to log the data with TestStand logger?",
                "How to calculate the settling time in LDO Load transient?",
                "Show the test setup diagram for Dither testing and explain it",
                "Show the test setup for CMRR and explain it",
                "Explain aperture time delay and show its test setup diagram",
                "How to report a phising incident?",
                "I am not sure what softwares I can install on my office computer, what should I do?",
                "How to connect to Soliton VPN?",
                "What is the employee id of Navin?",
                "What is the email of Bharathi?",
                "What is the designation of Nanthagopal?",
                "In which technology is Keerthana working on?",
                "List down the employees working in the python technology?",
                "List down the project engineers working in LabView?",
                "Can you list me the engineers who knows python available for next 6 months?",
                "Can you list me the senior project engineers available between sept -2023 to dec 2023?",
                "Can you list me the senior project engineers of python tech stream who are all available for next month?",
                "Is Sanjay available between Sept-2023 to Nov-2023?",
                "Is Sanjay will be available after Sept-2023?",
                "Give me details about the projects which are handled by Miruthula?",
                "Give me details about the project Argon?",
                "Give me details about the projects using LabView?",
                "Give me details about the projects under hisi?",
                "Give me details about the projects under scv mission?",
                "Which mission has run more kilometers in Spartans Challenge?",
                "How many people signed up for Spartans Challenge?",
                "How many kilometres were run by PES mission?",
                "List the total kilometers run by each mission in Sparatans Challenge."

             ]
nodes_collections = []
llama2_responses = []
langchain_responses = []

prompt = get_function_calling_prompt()

excel_report_path = 'C:\\v2\\Model Exploration\\Reports\\FunctionCallReport.xlsx'

for question in questions:
    print(question)
    

    llama2_response = Llama2LLM(question, data_source_descriptions, prompt)
    llama2_responses.append(llama2_response)

    print(llama2_response)

    langchain_response = LangChainLLM(question, data_source_descriptions, prompt)
    langchain_responses.append(langchain_response)
    
    print(langchain_response)

write_into_excel(nodes_collections,llama2_responses, langchain_responses, questions, excel_report_path)
print("Report Generated...")
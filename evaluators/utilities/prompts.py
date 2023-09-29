
def get_summarization_prompt():
    return """You are an expert in providing the summarized answer for the given user_question with the provided source nodes.
Please find the user_question below:
{user_question}

Use these source below to summarize your answer for the user_question provided :
{source}

Answer:
"""

def get_function_calling_prompt():
    return """You are an expert in picking up the particular domain based on its description provided where the user_question belongs to.
Please find the user_question below:
{user_question}

The source contains list of domain names and its description.
Use these source below to pick up a domain based on its description with respect to the user_question provided :
{source}

Your answer should only contain the Domain Name from the source provided. DO NOT create a domain of your own.
Answer Format: Domain Name : "<DOMAIN NAME HERE>"

Answer:
"""

def get_spartans_query_generator_prompt():
    return """
System:
You act as an expert in writing SQL queries based on the user_question.

Rules for generating Queries:
-Write SQL queries based on the user_question.
-The column name must be always enclosed in double quotes in the query.
-Extract the same column names as decsribed in the headers.
-The SQL query should be in a standard format such that it supports PANDASQL library in Python.
-Always use 'StartsWith' sql query for Full Name.
-Always Use 'LIKE' sql query with '%' for Mission and Full Name.
-Extract the column for achieved target as "Achieved\nTarget"
-Extract the column for annual target as "Annual\nTarget"


Rules for generating queries based on Mission:
Possible mission names and short forms:
-SCV - Semi-Conductor Validation, D2T - Design To Test, UPS - Unbeatable Professional Services, PES - Product Engineering Services, MDV - Medical Devices Validation and CORP - Corporate.
-If there any any other mission names mentioned in the user_question extarct  as "OTHER".
-All the mission names should be extracted in their respective short forms and should be in capital letters.

You have a dataframe in Python with the name "spartans_data". The dataframe contains information about engineers who have been taking part in the Spartans Group Challenge 2023 which invloves all employees in Soliton to reach one lakh kilometers. 

The data frame has the following headers:
Emp ID - Employee ID of the Engineer
Full Name - Name of the Engineer
Mission - Mission to which the engineer belongs to
Project Name - The project in which the engineer is currently working
Sign up for Challenge? - Whether the engineer have signed in for the Spartans Group Challenge 2023 or not
Annual\nTarget (km) - Annual target set by each engineer in kilometeres (kms set as a target by the engineer)
Achieved\nTarget (km) - Achieved target by each engineer in kilometeres (total kms run so far by the engineer)
Milestone Progress % - Progress in challenge in percentage
Jan'23 - Kilometers run by the engineer in January 2023
Feb'23 - Kilometers run by the engineer in February 2023
Mar'23 - Kilometers run by the engineer in March 2023
Apr'23 - Kilometers run by the engineer in April 2023
May'23 - Kilometers run by the engineer in May 2023
Jun'23 - Kilometers run by the engineer in June 2023
Jul'23 - Kilometers run by the engineer in July 2023
Aug'23 - Kilometers run by the engineer in August 2023
Sep'23 - Kilometers run by the engineer in September 2023
Oct'23 - Kilometers run by the engineer in October 2023
Nov'23 - Kilometers run by the engineer in November 2023
Dec'23 - Kilometers run by the engineer in December 2023

user_question (enclosed in a XML tag below) :
<user_question>user: {user_question}</user_question>
"""

def get_measurement_program_generation_prompt():
    return """
    System:
    You act as a expert in generating a python function code for a measurement procedure.

    Obey: You must,
    1. Generate a python code based on the user input.
    2. Your code should be based on the measurement procedure shared with you.
    3. Always provide a clean and neatly formatted python code.
    4. Create the measurement code within a python function provided to you below, so this function can be called by the user in their main program.
    5. The generated code will run in a virtual environments with the below libraries installed. Make sure you comply with the below libraries and its recommendations. Supported Python libraries:
        a. Pandas 1.5.3 is supported
            Use Pandas for any calculation, logging data, etc.
            When storing columns in a dataframe, make sure the columns are of same size. If not, fill the empty values with 'None' or 'NaN'.
        b. time is supported
            Use this library for any delays or timing operations.
    6. The generated code should not throw any errors when executed. Make sure you avoid below errors.
        a. Avoid ZeroDivisionError: float division by zero.
        b. Avoid IndexError: list index out of range.
        c. Avoid TypeError like 'float' object cannot be interpreted as an integer and 'str' object is not callable.
        d. Avoid using decimal value in range() function. range() function only accepts integer values.

    User Intent in tripe quotes:
    ```{intent}```

    Use the recommended measurement procedure shared below in triple quotes to satisfy the User Intent.
    ```{measurement_procedure}```

    Use the below recommendation to log the results from the measurement function. Make sure to import the required libraries.
    ```{log}```

    Driver Definition in tripe quotes:
    ```
    {driver_details}
    ```
    
    Obey:
    1. Do Not define any of the Instrument Session classes in the generated code as it already defined in the driver definition and the intialized session object is stored in the dictionary 'channelsLookup' with the pin name as the key.
    2. When calling the methods on the Instrument Object you should only use the methods from the driver definition.

    The name of the measurement function for the given measurement procedure is (given in triple quotes below):
    ```def {measurement_name}(channelsLookup):```

    The measurement function takes a dictionary 'channelsLookup' as input. The dictionary 'channelsLookup' contains the initialized instrument session object for each pin name in the pin map.

    Below are the list of Instrument session Object stored in the dictionary 'channelsLookup' with the pin name as the key.
    ```
    The initialized PowerSupply object for Vin is stored in the dictionary 'channelsLookup' with the key 'Vin'.
    The initialized PowerSupply class object for 'I_load' is stored in the dictionary 'channelsLookup' with the key 'I_load'.
    The initialized DMM class object for 'Vout' is stored in the dictionary 'channelsLookup' with the key 'Vout'.
    The initialized DMM class object for 'Vin_DMM' is stored in the dictionary 'channelsLookup' with the key 'Vin_DMM'.
    The initialized DUT class object for 'DUT' is stored in the dictionary 'channelsLookup' with the key 'DUT'. This will be used to write and read registers.
    ```

    In order to retrieve the object of the class, you can use the following code.
    ```channelsLookup[<pin name>]```

    Obey:
    1. Do NOT initialize or unintialize the Instrument or session for the object retrieved from 'channelsLookup' in your code as the object is already initialized.
    2. If you do the initialization, the instrument will throw error as it is already initialized.

    Obey:
    1. All the measurement code MUST be within the {measurement_name} function definition.
    2. ONLY generate the python code assuming that the generated code will be saved in a .py file, and the {measurement_name} measurement function will be imported and called in a main program by the user.
    3. DO NOT make {measurement_name} measurement function call in the generated program.

    Python Measurement Code:
    ```
    """

def get_general_code_generation_prompt():
    return """You are an expert in generating Python code for the user_question provided.
Please find the user_question below:
{user_question}

Obey:
1. Your code should be error free.
2. Handle All posible exceptions in your code.
3. Create functions wherever possible and use them wherever needed.
4. Follow the coding standards and Naming convention standards.
5. Return only the code. DO NOT explain the code. 

Code:
"""
import json

class Prompt:
    
    # First input variable - the conversation history (this can also be added as preceding `user` and `assistant` messages in the API call)
    HISTORY = ""

    # Second input variable - the user's question
    QUESTION = "Share your recommendation about the medical conditions of the patient"
    
    ######################################## PROMPT ELEMENTS ########################################

    ##### Prompt element 1: `user` role
    # Make sure that your Messages API call always starts with a `user` role in the messages array.
    # The get_completion() function as defined above will automatically do this for you.
    
    ##### Prompt element 2: Task context
    # Give Claude context about the role it should take on or what goals and overarching tasks you want it to undertake with the prompt.
    # It's best to put context early in the body of the prompt.
    TASK_CONTEXT = "You are a medical reviewer. You review patient notes and provide recommendation to the doctor about the medical conditions of the patient. Your recommendation includes patient’s current and chronic medical conditions. Your recommendation helps the doctor to decide on the treatment plan."
    
    ##### Prompt element 3: Tone context
    # If important to the interaction, tell Claude what tone it should use.
    # This element may not be necessary depending on the task.
    TONE_CONTEXT = "You should maintain a friendly customer service tone."
    
    ##### Prompt element 4: Detailed task description and rules
    # Expand on the specific tasks you want Claude to do, as well as any rules that Claude might have to follow.
    # This is also where you can give Claude an "out" if it doesn't have an answer or doesn't know.
    # It's ideal to show this description and rules to a friend to make sure it is laid out logically and that any ambiguous words are clearly defined.
    
    TASK_DESCRIPTION = """Here are some important rules for the interaction:
    
    - Refer to the <patient_notes>. Carefully read through the history, medications, encounters. For each encounter, carefully review the lab results, note. Check line-by-line to look for any evidence of medical conditions. 
    
    - Lab results contain comma separated list of lab readings, which can be lengthy. Please read through each and every value carefully. Maintain a list of common lab value thresholds that indicate potential conditions, and cross-check any out-of-range values against this list. 
    
    - When reviewing notes, actively look for any mention of symptoms, diagnoses, medications prescribed, or procedures done that could indicate a condition. Only list a medical condition when you see clear evidence in the lab results or notes to support a diagnosis. 
    
    - Refer to the findings from comprehend medical inside <comprehend_medical></comprehend_medical> XML tag. Use this as a helper tool to identify the medical conditions.
    
    - Please do not make any assumptions without verifying supporting evidence for the specific date.
    
    - For each date, list all the medical conditions, corresponding ICD 10 codes, relevant explanation as evidence.
    
    - Only use the information provided to generate the recommendation. If there are no medical condition to recommend to the doctor tell no medical condition to report.
    
    - Provide the final recommendation inside <recommendation></recommendation> XML tags in JSON format, with each condition formatted as:
    {
      "Active_Condition":[
      {"Review": {  
      "DX_Code": "ICD10 Code",
      "Description": "Condition description",
      "Memo": {
                  "date":"date",
                  "note":"Explanation from notes"
              }
      }},
      {"Review": {
      "DX_Code": "ICD10 Code",
      "Description": "Condition description",
      "Memo": {
                  "date":"date",
                  "note":"Explanation from notes"
              }
      }}],
      "Inactive_Condition": [
        {"Review": {
          "DX_Code": "ICD10 Code",
          "Description": "Condition description",
          "Memo": {
            "date": "date",
            "note": "Explanation from notes"
          }
      }}]
    }
    """
    
    EXAMPLES = """Here is an example inside <example></example> XML tag on how to perform the task: 
    <example>
    user: <patient_notes>
    {
      "name": "XYZ",
      "age": "60 years",
      "sex": "Male",
      "encounters": [ 
        {
          "Date": "2022-01-04", 
          "Procedure codes": "99214",
          "note": ["Blood pressure has been stable. Pt is overdue for physical and labs. Pt will come to the lab next month and will schedule an appointment for a physical.", "stable"]
        },
        {
          "Date": "2022-02-04", 
          "note": ["Dual-chamber pacemaker was placed for sinus node dysfunction."]
        },
        {
          "Date": "2023-07-22",
          "note": ["Had unprovoked PE.  Still on anticoagulation.  Oncology note dated 07/05/2023: long term anticoagulation recommended.  It can be primary hypercoagulability."]
        }, 
        {
          "Date": "2023-07-31", 
          "note": ["Patient visited XXX DPM. Came in for foot care, upon neurology foot examination revealed reduced monofilament test and spontaneous. Suggested evaluation for Type 2 diabetes mellitus with diabetic polyneuropathy.", "Patient visited doctor for cough, chest soreness, runny nose, headache, slight fever, and sore throat. Doctor suggested to take Ibuprofen and cough suppressant"]
        }
      ]
    }
    </patient_notes>
    
    assistant: <response>
    <thinking>
    Date: 2022-01-04
    No evidence of medical conditions
    
    Date: 2022-02-04
    Condition: Sinus node dysfunction 
    ICD10: I49.5
    Evidence: Dual-chamber pacemaker was placed for sinus node dysfunction.
    
    Date: 2023-07-22  
    Condition: Pulmonary embolism
    ICD10: I26.99
    Evidence: Had unprovoked PE. Still on anticoagulation. Oncology note dated 07/05/2023: long term anticoagulation recommended. It can be primary hypercoagulability.
    
    Date: 2023-07-31
    Condition 1: Type 2 diabetes mellitus with diabetic polyneuropathy
    ICD10: E11.42
    Evidence: Patient visited XXX DPM. Came in for foot care, upon neurology foot examination revealed reduced monofilament test and spontaneous. Suggested evaluation for Type 2 diabetes mellitus with diabetic polyneuropathy.
    
    Condition 2: Upper respiratory infection 
    ICD10: J06.9
    Evidence: Patient visited doctor for cough, chest soreness, runny nose, headache, slight fever, and sore throat. Doctor suggested to take Ibuprofen and cough suppressant.
    
    Date: 2023-09-01
    Condition 1: Vitamin D deficiency
    ICD10: E55.9
    Evidence: vitamin D 25-oh, total: 43 NG/mL
    
    Condition 2: Upper respiratory infection (inactive)
    ICD10: J06.9
    Evidence: Doctor visit. Patient no longer complained of cough. Patient is not taking Ibuprofen and cough suppressant anymore.
    
    Inactive Conditions:
    - Upper respiratory infection (J06.9)
    
    Active Conditions:  
    - Sinus node dysfunction (I49.5)
    - Pulmonary embolism (I26.99)
    - Type 2 diabetes mellitus with diabetic polyneuropathy (E11.42)
    - Prostate cancer (C61)
    - Vitamin D deficiency (E55.9)
    </thinking>
    
    <recommendation>
    {
      "Active_Condition": [ 
      {"Review":{
        "DX_Code": "I49.5",  
        "Description": "Sinus node dysfunction",
        "Memo": {
          "date": "2022-02-04",
          "note": "Dual-chamber pacemaker was placed for sinus node dysfunction."
        }
      }},  
      {"Review": {  
        "DX_Code": "I26.99",
        "Description": "Pulmonary embolism", 
        "Memo": {
          "date": "2023-07-22",  
          "note": "Had unprovoked PE. Still on anticoagulation. Oncology note dated 07/05/2023: long term anticoagulation recommended. It can be primary hypercoagulability."
        }
      }},
      {"Review": {
        "DX_Code": "E11.42",  
        "Description": "Type 2 diabetes mellitus with diabetic polyneuropathy",
        "Memo": {
          "date": "2023-07-31",
          "note": "Patient visited XXX DPM. Came in for foot care, upon neurology foot examination revealed reduced monofilament test and spontaneous. Suggested evaluation for Type 2 diabetes mellitus with diabetic polyneuropathy."
        }
      }},
      {"Review": {
        "DX_Code": "E55.9",
        "Description": "Vitamin D deficiency",  
        "Memo": {
            "date": "2023-09-01",
            "note": "vitamin D 25-oh, total: 43 NG/mL"
          }
        }}],
      "Inactive_Condition": [
        {"Review": {
          "DX_Code": "J06.9",
          "Description": "Upper respiratory infection",
          "Memo": {
            "date": "2023-09-01",
            "note": "Doctor visit. Patient no longer complained of cough. Patient is not taking Ibuprofen and cough suppressant anymore."
          }
        }}]
      }
    </recommendation>
    </response>
    </example>"""

    ##### Prompt element 6: Input data to process
    # If there is data that Claude needs to process within the prompt, include it here within relevant XML tags.
    # Feel free to include multiple pieces of data, but be sure to enclose each in its own set of XML tags.
    # This element may not be necessary depending on task. Ordering is also flexible.
    
    INPUT_DATA = f"""Here are the patient notes: 
    <patient_notes>
    $patient_notes$
    </patient_notes>
    
    Here are the comprehend medical findings:
    $cm_output_str$ 

    
    Here is the user's question:
    <question>
    {QUESTION}
    </question>"""
    
    ##### Prompt element 7: Immediate task description or request #####
    # "Remind" Claude or tell Claude exactly what it's expected to immediately do to fulfill the prompt's task.
    # This is also where you would put in additional variables like the user's question.
    # It generally doesn't hurt to reiterate to Claude its immediate task. It's best to do this toward the end of a long prompt.
    # This will yield better results than putting this at the beginning.
    # It is also generally good practice to put the user's query close to the bottom of the prompt.
    IMMEDIATE_TASK = "How do you respond to the user's question?"
    
    ##### Prompt element 8: Precognition (thinking step by step)
    # For tasks with multiple steps, it's good to tell Claude to think step by step before giving an answer
    # Sometimes, you might have to even say "Before you give your answer..." just to make sure Claude does this first.
    # Not necessary with all prompts, though if included, it's best to do this toward the end of a long prompt and right after the final immediate task request or description.
    PRECOGNITION = "Think step by step about your answer first before you respond. When you reply, first find all the medical conditions, corresponding ICD10 codes, explanation and write them down inside <thinking></thinking> XML tags.  This is a space for you to write down relevant content. Once you are done extracting relevant information, double check your work. Look back over the lab results and notes again with fresh eyes to make sure nothing was missed. Now answer the question. Put your recommendation inside <recommendation></recommendation> XML tag."

    
    ##### Prompt element 9: Output formatting
    # If there is a specific way you want Claude's response formatted, clearly tell Claude what that format is.
    # This element may not be necessary depending on the task.
    # If you include it, putting it toward the end of the prompt is better than at the beginning.
    OUTPUT_FORMATTING = "Put your response in <response></response> tags."
    
    ##### Prompt element 10: Prefilling Claude's response (if any)
    # A space to start off Claude's answer with some prefilled words to steer Claude's behavior or response.
    # If you want to prefill Claude's response, you must put this in the `assistant` role in the API call.
    # This element may not be necessary depending on the task.
    PREFILL = "[assistant] <response>"


    ####### COMBINE ELEMENTS #######

    LLM_PROMPT = ""
    
    if TASK_CONTEXT:
        LLM_PROMPT += f"""{TASK_CONTEXT}"""
    
    if TONE_CONTEXT:
        LLM_PROMPT += f"""\n\n{TONE_CONTEXT}"""
    
    if TASK_DESCRIPTION:
        LLM_PROMPT += f"""\n\n{TASK_DESCRIPTION}"""
    
    if EXAMPLES:
        LLM_PROMPT += f"""\n\n{EXAMPLES}"""
    
    if INPUT_DATA:
        LLM_PROMPT += f"""\n\n{INPUT_DATA}"""
    
    if IMMEDIATE_TASK:
        LLM_PROMPT += f"""\n\n{IMMEDIATE_TASK}"""
    
    if PRECOGNITION:
        LLM_PROMPT += f"""\n\n{PRECOGNITION}"""
    
    if OUTPUT_FORMATTING:
        LLM_PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""



    ######################################## BUILD THE FINAL PROMP ####################T####################
    #We'll keep some of the components as before, we'll change few
    #No changes for HISTORY, QUESTION, TASK_CONTEXT, TONE_CONTEXT, EXAMPLES, IMMEDIATE_TASK, PRECOGNITION, OUTPUT_FORMATTING, PREFILL
    
    ##### Prompt element 4: Detailed task description and rules
    # Expand on the specific tasks you want Claude to do, as well as any rules that Claude might have to follow.
    # This is also where you can give Claude an "out" if it doesn't have an answer or doesn't know.
    # It's ideal to show this description and rules to a friend to make sure it is laid out logically and that any ambiguous words are clearly defined.
    TASK_DESCRIPTION = """The patient notes are provided inside <patient_notes></patient_notes> XML tag. It contains date, medication, history, procedure codes, lab results and note.

    Your initial recommendations based on the patient notes analysis are provided inside <initial_recommendation></initial_recommendation> XML tag. 

    Guidelines about the medical conditions and corresponding ICD 10 codes are provided inside <guidelines></guidelines> XML tag. 

    When you reply, you follow these steps:

    - Refer to the <patient_notes>. Carefully read through the history, medications, encounters. For each encounter, carefully review the lab results, note. Check line-by-line to look for any evidence of medical conditions. 

    - Lab results contain comma separated list of lab readings, which can be lengthy. Please read through each and every value carefully. Maintain a list of common lab value thresholds that indicate potential conditions, and cross-check any out-of-range values against this list. 

    - When reviewing notes, actively look for any mention of symptoms, diagnoses, medications prescribed, or procedures done that could indicate a condition. Only list a medical condition when you see clear evidence in the lab results or notes to support a diagnosis. 

    - Refer to the guidelines from the knowledge base inside <guidelines></guidelines> XML tag. Use it as a helper tool to identify the medical conditions and ICD 10 codes.

    - Refer to your initial recommendations inside <initial_recommendation></initial_recommendation> XML tag. Please adjust any recommendations as appropriate.

    - Please do not make any assumptions without verifying supporting evidence for the specific date.

    - For each date, list all the medical conditions, corresponding ICD 10 codes, relevant explanation as evidence.

    - Only use the information provided to generate the recommendation. If there are no medical condition to recommend to the doctor tell no medical condition to report.

    - Provide the final recommendation inside <recommendation></recommendation> XML tags in JSON format, with each condition formatted as:
    {
      "Active_Condition":[
      {"Review": {  
      "DX_Code": "ICD10 Code",
      "Description": "Condition description",
      "Memo": {
                  "date":"date",
                  "note":"Explanation from notes"
              }
      }},
      {"Review": {
      "DX_Code": "ICD10 Code",
      "Description": "Condition description",
      "Memo": {
                  "date":"date",
                  "note":"Explanation from notes"
              }
      }}],
      "Inactive_Condition": [
        {"Review": {
          "DX_Code": "ICD10 Code",
          "Description": "Condition description",
          "Memo": {
            "date": "date",
            "note": "Explanation from notes"
          }
      }}]
    }
    """
    
    ##### Prompt element 6: Input data to process
    # If there is data that Claude needs to process within the prompt, include it here within relevant XML tags.
    # Feel free to include multiple pieces of data, but be sure to enclose each in its own set of XML tags.
    # This element may not be necessary depending on task. Ordering is also flexible.
    INPUT_DATA = f"""Here are the patient notes: 
    <patient_notes>
    $patient_notes$
    </patient_notes>

    Here are the initial recommendations: 
    $initial_recommendation$

    Here are the guidelines: 
    $guidelines$

    Here is the user's question:
    <question>
    {QUESTION}
    </question>"""
    
    ####### COMBINE ELEMENTS #######
    FINAL_PROMPT = ""
    
    if TASK_CONTEXT:
        FINAL_PROMPT += f"""{TASK_CONTEXT}"""

    if TONE_CONTEXT:
        FINAL_PROMPT += f"""\n\n{TONE_CONTEXT}"""

    if TASK_DESCRIPTION:
        FINAL_PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

    if EXAMPLES:
        FINAL_PROMPT += f"""\n\n{EXAMPLES}"""

    if INPUT_DATA:
        FINAL_PROMPT += f"""\n\n{INPUT_DATA}"""

    if IMMEDIATE_TASK:
        FINAL_PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

    if PRECOGNITION:
        FINAL_PROMPT += f"""\n\n{PRECOGNITION}"""

    if OUTPUT_FORMATTING:
        FINAL_PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

# Few shot prompting
# Examples are provided
# Improve the output quality as well

import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")

client = OpenAI(
    api_key=GEMINI_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/"
)


# ------------- IMPORTANT ----------------------
# ------------- add in system prompt --------------------------
#- Each message must be **one single JSON object only**.
# else we get parsing errors, if the response contains something other than JSON
# add this too since even after adding above prompt got error ....So add this
# - content should be only string strictly, since its used to get reponse 

SYSTEM_PROMPT = """

    You're an helpful AI assistant, You work on chain of thoughts procedure.
    You work on START, PLAN and OUTPUT steps.
    When you get a question you plan and then give result when you think enough planning is done.

    RULES-
    - Strictly give in JSON
    - Each message must be **one single JSON object only**.
    - content should be only string strictly, since its used to get reponse
    - Only run one step at a time
    - Sequence of steps START(user gives input), PLAN (you think the ans or result), OUTPUT

    OUTPUT FORMAT-
    - {"step": "START" | "PLAN" | "OUPUT", "content": "string" }

    Example-
    START: Find SI for Principal Rs.10000 for time period 2 years, 10 percent interest
    PLAN: {
        "step": "PLAN", "content": "Looks like you're working on a math question based on Simple interest"
    }
    PLAN: {
        "step": "PLAN", "content": "We can begin with finding interest using I = (P*R*T)/100, P = Principal amt., R=Rate of interest, T=time period and then Adding the interest to the principal amt."
    }
    PLAN: {
        "step": "PLAN", "content": "Now let's put values in the above formula (10000 * 10 * 2)/100 = Rs.2000 , On solving we get Rs.2000"
    }
    PLAN: {
        "step": "PLAN", "content": "For total amount, We add this Rs.2000 to the principal Rs.10000 + 2000 = Rs.12000"
    }
    OUTPUT: {
        "step": "OUTPUT", "content": "Total amt: Rs. 12000, Interest: Rs.2000"
    }
    
    Above is just an example to show step, you can modify answers(content) properly yourself

"""

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]
user_query = input("\nType in something >>>\t")
message_history.append(
    {
        "role": "user",
        "content": user_query,
    }
)

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history,
    )

    raw = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw})
    parsed = json.loads(raw)
    toPrint = parsed.get("content")
    print(f"\n{toPrint}")

    # if parsed.get("step") == "START":
    #     continue
    # if parsed.get("step") == "PLAN":
    #     continue
    if parsed.get("step") == "OUTPUT":
        break






#  Manual

# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     response_format={"type": "json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {
#             "role": "user",
#             # "content": "Write an essay on Seasons",
#             # "content": "write a function to find tsa of cube in typescript",
#             "content": "Find SI on Rs.100000 for 10% interest and Time 2 years",
#         },

#         # Manually added

#         # {
#         #     "role": "assistant",
#         #     "content": json.dumps(
#         #         {
#         #             "step": "START",
#         #             "content": "Find SI on Rs.100000 for 10% interest and Time 2 years",
#         #         }
#         #     ),
#         # },
#         # {
#         #     "role": "assistant",
#         #     "content": json.dumps(
#         #         {
#         #             "step": "PLAN",
#         #             "content": "Looks like you're asking to calculate Simple Interest. I will use the formula SI = (P * R * T) / 100.",
#         #         }
#         #     ),
#         # },
#     ],
# )

# print(f"\n\n\n {response.choices[0].message.content} \n\n")

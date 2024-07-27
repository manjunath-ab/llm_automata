from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.metrics import FaithfulnessMetric
from deepeval.metrics import ContextualPrecisionMetric
from deepeval.metrics import ContextualRecallMetric
from deepeval.metrics import ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd

dotenv_path = Path('/home/abhi/.env')
load_dotenv(dotenv_path=dotenv_path)


df=pd.read_excel("updated_snowflake_queries_evaluation.xlsx")


AnswerRelevancy = AnswerRelevancyMetric(
    threshold=0.7,
    model="gpt-4o-mini",
    include_reason=True
)

Faithfulness= FaithfulnessMetric(
    threshold=0.7,
    model="gpt-4o-mini",
    include_reason=True
)

ContextualPrecision= ContextualPrecisionMetric(

    threshold=0.7,
    model="gpt-4o-mini",
    include_reason=True
)
ContextualRecall= ContextualRecallMetric(

    threshold=0.7,
    model="gpt-4o-mini",
    include_reason=True
)
ContextualRelevancy= ContextualRelevancyMetric(

    threshold=0.7,
    model="gpt-4o-mini",
    include_reason=True
)

metrics=[AnswerRelevancy, ContextualPrecision, ContextualRelevancy, ContextualRecall, Faithfulness]

test_cases=[]
for index, row in df.iterrows():

  test_case = LLMTestCase(
    input=row["Query"],
    actual_output=row["Actual Output"],
    expected_output=row["Expected Output"],
    retrieval_context=[row["Retrieval Context"]])
  test_cases.append(test_case)



# or evaluate test cases in bulk
evaluate(test_cases, metrics)

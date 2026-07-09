from pipeline.llm import ReasoningLLM, SQL_LLM

reasoning = ReasoningLLM()
print("Reasoning:", reasoning.generate("Say hello in one sentence."))

sql_llm = SQL_LLM()
print("SQL:", sql_llm.generate("Write a SQL query to get all customers from the customer table."))
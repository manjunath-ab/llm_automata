Will be Using GROQ and LLAMA3 model to create a personal SQL Agent that will ultimately generate views and stored procedures . Will be using snowflake as a base SQL data warehouse


At a high level, the agent will:

1.Fetch the available tables from the database
2.Decide which tables are relevant to the question
3.Fetch the DDL for the relevant tables
4.Generate a query based on the question and information from the DDL
5.Double-check the query for common mistakes using an LLM
6.Execute the query and return the results
7.Correct mistakes surfaced by the database engine until the query is successful
8.Formulate a response based on the results

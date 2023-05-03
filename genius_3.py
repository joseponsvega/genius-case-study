from langchain.agents import AgentType
from langchain.agents import create_csv_agent
from langchain.agents import initialize_agent
from langchain.agents import load_tools
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.tools import tool


@tool
def search_csv(query: str) -> str:
    """Answers questions about a csv file. The format is the name of the csv file, then a comma, then the question. For example: 'data.csv,what is the csv about?'."""

    results = query.split(",")

    agent = create_csv_agent(OpenAI(temperature=0), results[0].replace("'", ""), verbose=True)

    response = agent.run(results[1])

    return response

@tool
def open_text_file(filename: str) -> str:
    """Opens the text file and returns the contents. Don't forget to use the structure of Action, Action Input, etc."""

    with open(filename.replace("\n", "").replace("'", "")) as infile:
        return infile.read()


llm = OpenAI(temperature=0, model_name="gpt-4")

tools = load_tools(["llm-math"], llm=llm) + [search_csv, open_text_file]

memory = ConversationBufferMemory(memory_key="chat_history")

from tempfile import TemporaryDirectory

# We'll make a temporary directory to avoid clutter
working_directory = TemporaryDirectory()

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, memory=memory)

question = "What is the subject with the lowest average grade? Find its syllabus."

agent.run(f"You have the following files at your disposal: Grades.csv, Professors.csv, Syllabus.txt and Weekly Schedule.txt. First, summarize each file and what information it contains. Then using those files and knowing the information within each one, answer the following question: {question} Remember to use the structure of Action, Action Input, etc.")
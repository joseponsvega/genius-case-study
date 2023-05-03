from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.agents import create_csv_agent
from typing import Optional, Type

from langchain.memory import ConversationBufferMemory
from langchain.tools import tool

@tool
def search_csv(query: str) -> str:
    """Answers questions about a csv file. The format is the name of the csv file, then a comma, then the question. For example: 'data.csv,what is the csv about?'"""

    results = query.split(",")

    agent = create_csv_agent(OpenAI(temperature=0), results[0], verbose=True)

    response = agent.run(results[1])

    return response

@tool
def open_text_file(filename: str) -> str:
    """Opens the text file and returns the contents."""

    with open(filename) as infile:
        return infile.read()


llm = OpenAI(temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm=llm) + [search_csv, open_text_file]

memory = ConversationBufferMemory(memory_key="chat_history")

from langchain.tools.file_management import (
    ReadFileTool,
    CopyFileTool,
    DeleteFileTool,
    MoveFileTool,
    WriteFileTool,
    ListDirectoryTool,
)
from langchain.agents.agent_toolkits import FileManagementToolkit
from tempfile import TemporaryDirectory

# We'll make a temporary directory to avoid clutter
working_directory = TemporaryDirectory()

toolkit = FileManagementToolkit(root_dir=str(working_directory.name)) # If you don't provide a root_dir, operations will default to the current working directory


# tools += toolkit.get_tools()


agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, memory=memory)

agent.run("You have the following files at your disposal: Grades.csv, Professors.csv, Syllabus.txt and Weekly Schedule.txt. Read the csv files then translate them to plain text descriptions. Then use that and the text files to figure out which professors teach mathematics.")

# agent = create_csv_agent(OpenAI(temperature=0), 'Grades.csv', verbose=True)
#
# agent.run("What is the average grade in Economics?")

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

# news_text = """WASHINGTON (AP) — Joe Biden faced a test Thursday that he had avoided so far this year — a solo news conference with questions from the White House press corps.

# The news conference was meant to reassure a disheartened group of Democratic lawmakers, allies and persuadable voters in this year’s election that Biden still has the strength and stamina to be president. Biden has tried to defend his feeble and tongue-tied performance in the June 27 debate against Republican Donald Trump as an outlier rather than evidence that at 81 he lacks the vigor and commanding presence that the public expects from the commander in chief.

# He made at least two notable flubs, referring at an event beforehand to Ukrainian President Volodymyr Zelenskyy as “President Putin” and then calling Kamala Harris “Vice President Trump” when asked about her by a reporter. But he also gave detailed responses about his work to preserve NATO and his plans for a second term. And he insisted he’s not leaving the race even as a growing number of Democratic lawmakers ask him to step aside.
# """

# news_title = """Key takeaways from Biden’s news conference: Insistence on staying in the race and flubbed names"""

def check_news_relevance(news_text):
    openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = openai.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "You are an assistant to check if the news is related to the US stock market."},
            {"role": "user", "content": f"Here is the news: {news_text}. Reply in one word whether it is Relevant or Not Relevant to the USA stock market news."}
        ]
    )
    return response.choices[0].message.content

def news_summarizer(news_content, news_title):
    openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = openai.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "You are an assistant to summarize the news information in one line."},
            {"role": "user", "content": f"Here is the news title {news_title} and here is the news content {news_content} Provide me with a one line summary of the news."}
        ]
    )
    return response.choices[0].message.content

# print(check_news_relevance(news_text))
# print(news_summarizer(news_content = news_text, news_title = news_title))
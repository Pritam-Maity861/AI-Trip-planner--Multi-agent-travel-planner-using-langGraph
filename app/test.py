# from app.tools.tavily import tavily_search
from app.tools.flight import search_flights

# res = tavily_search("luxury hotels in Paris")
# print(res)

res = search_flights("Plan a 7 days Japan trip from India")
print(res)
#### Butler bot

1. I want this bot to automate tasks for me when I write to it.
2. then I want to store that context in a local postgres so we can call it and it will have context
3. I want to get a message every morning with my daily tasks along with a humorous butlery vibe it needs to give off
4. I want it to write to the postgres as well, any AI will work just use the cheapest (free if possible)
5. It needs to run on a raspberry pi so it needs to be efficient



### What needs to be done
1. Build out data model for single table that will store messages, emails, text, etc for the bot to understand context.
    - pretty easy for the most part

2. Build out AI prompts as well as agent tooling so it can read and write to the postgres
    - To build the daily schedule prompt lets pull in the data from table based on a query
        - simple prompt
    - also make a prompt to read a message from a telegram service and classify it and write to postgres
        - simple prompt

3. setup telegram serive so the app can read and write to the telegram
4. set up crons to read weather, etc other news sources.
Introduction
------------
Recent [research]("https://webspace.utexas.edu/pe2929/Eastwick/Ireland2011_PSci.pdf") has shown that language usage is a strong predictor for relationship stability. Modern dating sites rely on user-submitted information to find compatible partners; MatchBot aims to bring science to bear on the art of matchmaking.

Concept
-------
The language style of users can be analyzed and compared once writing samples have been collected and stored. But how to elicit user input in an engaging and intuitive way? Enter chatbot technology. The user interacts with a chatbot (christened MatchBot), and their inputs are saved for analysis. Once enough input has been collected, compatible users can be matched!

Implementation
--------------
The website was created with HTML, CSS, and JavaScript. It is mounted on a Rails framework and a PostGreSQL database hosted with [Heroku]("http://heroku.com"). The chatbot is [PyAIML]("http://pyaiml.sourceforge.net/"), a Python implementation for AIML that runs as a daemon on the Heroku server. 
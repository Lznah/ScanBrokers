###########
ScanBrokers
###########

This is a semestral work for NI-PYT at faculty of IT at Czech Technical University in Prague. An analytical tool that utilizes information gathered by a crawler, made in MI-DDW class.

Description:
============

It is well-known fact that there is a big competition between real estate agencies at the Czech Republic estate scene. An estate agent usually helps a client to sell a property in an enchange for a percentage portion of money out of the selling price, called provision. The estate agency usually provides their brand, tools, marketing and law services to the agent, also for a portion out of the agent's provision. This leads to a phenomen, when a part of all agents has a rich history of agencies, that they have been working with. This fact collerates with agents abilities to cheat on a real estate agency. However, leaders of the biggest agencies know each other and with this tool, they could easily track these bad behaving estate agents.
Also, this tool can be used the other way. A franchisor could track franchises of other real estate agencies (franchisors), that are doing well in the bussiness. Eventually, this franchisor can use this data to know, which franchises he should motivate to work with him.

Functional requirements:
========================

* Gathered data are stored in JSON. Create a program, that will find this newly gathered data and save them to database.
* Analytical tool will use MongoDB/Redis/ElasticSearch - *I am not sure which one I should choose. I will be very thankful if you helped me with this, because you definitely have more experience in this field. The crawler saves data in JSON format every day.*
* Use Flask to build the website (*Also, if you have better option that could fit this task, please let me know :) *)
* User can filter a real estate agent by agent's name and he can show agent's history.
* User can see historical data of estate agencies and their franchisors
* Documentation would be focused more on how to use this tool then to its technical side. (*Please, let me know if it is a problem*)
* Only basic auth is used to enter this tool.

Nonfunction requirements:
=========================

* This program does not inform administrator or anyone, if there is an error, no new data or something bad happened during the transfer to database with each new gathered data. I plan to add this later, but not in this semestral work.
* The analytical tool is not able to give tips for good franchises and it is meant to be added in future versions.
* A crawler is not a part of this semestral work at all.
* The tool is not able to do advanced filtering, only by agents name.

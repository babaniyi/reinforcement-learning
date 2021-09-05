# reinforcement-learning

## Multi-armed bandit problem
Imagine you are in Las Vegas, in your favorite casino. You are in a room containing five slot machines. For each of them the game is the same: you bet a certain amount of money, say 1 dollar, you pull the arm, and then the machine will either take your money, or give you twice your money back. Remember the rewards we talked about in the previous chapter? Let's say that if the machine takes your money, your reward is -1, and if the machine returns you twice your money, your reward is +1.

The first step of your strategy must be to figure out, in the minimum number of plays, which of these five slot machines has the highest chance of giving you a 1 reward. In other words, you have to quickly figure out the slot machine with the highest success rate. Then, as soon as you figure it out, you simply need to keep playing on that most successful slot machine.

Finding the most successful slot machine is not hard; one simple strategy could be to play 100 times on each of these five slot machines and then, at the end, look at which of them gave you more money. Statistically, this gives you a good chance of finding that most generous slot machine.
All the challenge is in "quickly". The hardest part is to find the best slot machine in a minimum number of trials. This is where your first AI model comes into play.

My solution uses **Thompson Sampling model** and is saved as ts-casino-bandit.py

## AI for Sales and Marketing
### Problem to solve
Imagine an e-commerce business that has millions of customers. These customers are people buying products on the website from time to time, getting those products delivered to their homes. The business is doing well, but the board of executives has decided to follow an action plan to maximize revenue.
This plan consists of offering the customers the option to subscribe to a premium plan, which will give them benefits like reduced prices, special deals, and so on. This premium plan is offered at a yearly price of $200, and the goal of this e-commerce business is, of course, to get the maximum number of customers to subscribe to this premium plan. Let's do some quick math to give us some motivation for building an AI to maximize the revenue of this business.

The marketing team has 9 strategies.  These strategies were carefully and smartly elaborated by the marketing team, and each of them has the same goal: convert the maximum number of clients to the premium plan. However, these nine strategies are all different. The marketing team wants to figure out which strategy has the highest conversion rate as soon as possible, and by spending the minimum amount. They know that finding and deploying the best strategy can significantly increase the business's revenue. 

My solution uses **Thompson Sampling model** and is saved as ts-marketing-bandit.py

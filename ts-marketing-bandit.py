totalCust = 1000

# Suppose we have given the following conversion rates. Note that we don't need conversion rates for Thompson Sampling but for building a simulation 
# environment to be sure Thomspon Sampling will select the best ad strategy most of the times
conv_rate = [0.15, 0.34, 0.2, 0.15, 0.18, 0.12]
ads = len(conv_rate)

environment = np.zeros([totalCust, ads])

# Building the simulation environment
for person in range(totalCust):
  for ad in range(ads):
    if np.random.rand() <= conv_rate[ad]:
      environment[person, ad] = 1


# Run the Thompson Sampling selection algorithm

rewardPos = np.zeros(ads)
rewardNeg = np.zeros(ads)

for person in range(totalCust):
  selected_ad = 0
  randomState = 0

  for ad in range(ads):
    rbeta = np.random.beta(rewardPos[ad]+1, rewardNeg[ad]+1)
    if rbeta > randomState:
      randomState = rbeta
      selected_ad = ad

  if environment[person][selected_ad] == 1:
    rewardPos[selected_ad] += 1
  else:
    rewardNeg[selected_ad] += 1

# See results
totalSelected = rewardPos + rewardNeg

for i in range(ads):
  print(f" Ad {str(i)} was selected {str(totalSelected[i])} times")

print('=' * 50)
print(f"Conclusion: \tThe best Ad is Ad #{str(np.argmax(totalSelected)+1)}")

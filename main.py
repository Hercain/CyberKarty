import random

# Cybersecurity definitions
definitions = ['The process of protecting networks, systems, and programs from digital attacks',
               'A type of malicious software designed to gain access to or damage a computer system',
               'A set of strategies for managing and protecting digital data',
               'A type of computer program designed to detect and defend against malicious software']

# Cybersecurity terms
terms = ['Cybersecurity', 'Malware', 'Data Security', 'Antivirus']

# Mapping definitions to terms
definitions_terms = dict(zip(definitions, terms))

# Message to prompt the user to start the game
print('Welcome to the Cybersecurity Definition Matching Game!')

# Shuffle the definitions
random.shuffle(definitions)

# Initialize the score
score = 0

# Iterate through the definitions
for definition in definitions:
    # Prompt the user to enter the term
    print('What is the term for the following definition?')
    print(definition)
    # Get the user's answer
    answer = input()
    # Check if the answer is correct
    if answer == definitions_terms[definition]:
        print('Correct!')
        score += 1
    else:
        print('Incorrect! The correct answer is', definitions_terms[definition])

# Print the final score
print('You scored', score, 'points!')


import random
import time

#create a list of cybersecurity definitions
cybersecurity_definitions = ["Malware: malicious software designed to damage or disable computers and computer systems", 
"Phishing: an attempt to gain sensitive information by masquerading as a trustworthy entity", 
"Social Engineering: using psychological manipulation to obtain confidential information or change user behavior", 
"DoS Attack: a coordinated effort to make a network or system unavailable to its intended users", 
"Spoofing: pretending to be someone else to gain access to secure information", 
"DDoS Attack: a distributed denial-of-service attack which floods a target with traffic from many sources"]

#create a list of matching terms for the definitions
cybersecurity_terms = ["malware", "phishing", "social engineering", "DoS attack", "spoofing", "DDoS attack"]

#create a list to store mistakes made by the user
mistakes = []

#introduce the game
print("Welcome to the Cybersecurity Definition Matching Game!")
print("In this game, you will be given a definition and must match it to its corresponding term. Let's get started!")

#create a counter for the round
round = 0

#create a timer to keep track of time
start_time = time.time()

#create a loop for the game to continue until all definitions have been matched to terms
while round < len(cybersecurity_definitions):
  #increment the round counter
  round += 1
  
  #print the current round
  print("\nRound {}".format(round))
  
  #randomly select a definition
  current_definition = random.choice(cybersecurity_definitions)
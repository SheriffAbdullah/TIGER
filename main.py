from GeneticAlgo import *

theoryLabels = ["M","OP","OS","CP","AI","D","OSL","OPL","DL","EA","LIB","F","SEM","MEN","TUT"]
classRooms = ["A","A","A","A","A","A"]

# model variables  
#   |   |   |
#   v   v   v
DAYS = 5
PERIODS = 7
BREAK = [4]


POPULATION_SIZE = 8

basicCreditRequirements = {0 : {"noOfClasses" : 4,"classRoom" : 0},
              1 : {"noOfClasses" : 3,"classRoom" : 0},
              2 : {"noOfClasses" : 3,"classRoom" : 0},
              3 : {"noOfClasses" : 2,"classRoom" : 0},
              4 : {"noOfClasses" : 3,"classRoom" : 0},
              5 : {"noOfClasses" : 3,"classRoom" : 0},
              6 : {"noOfClasses" : 3,"classRoom" : 0}}


profPreferences = {
    0 : [[ 0, 9, 0, 0, -1, -1, -9],
         [ 0, 9, 0, 0, -1, -1, -9],
         [ 0, 9, 0, 0, -1, -1, -9],
         [ 0, 9, 0, 0, -1, -1, -9],
         [ 0, 9, 0, 0, -1, -1, -9]],
    
    1 : [[ 9, 0, 0, 0, -1, -1, -9],
         [ 9, 0, 0, 0, -1, -1, -9],
         [ -9, -9, -9, -9, -9, -9, -9],
         [ 9, 0, 0, 0, -1, -1, -9],
         [ 9, 0, 0, 0, -1, -1, -9]],
    
    2 : [[ 9, 9, 0, 0, -5, -7, -9],
         [ 9, 9, 0, 0, -5, -7, -9],
         [ 9, 9, 0, 0, -5, -7, -9],
         [ 9, 9, 0, 0, -5, -7, -9],
         [ 9, 9, 0, 0, -5, -7, -9]],
    
    3 : [[ 0, 0, 0, -9, -1, -1, -9],
         [ 0, 0, 0, -9, -1, -1, -9],
         [ 0, 0, 0, -9, -1, -1, -9],
         [ 0, 0, 0, -9, -1, -1, -9],
         [ 0, 0, 0, -9, -1, -1, -9]],
    
    4 : [[ 0, 1, 0, 9, -1, -1, -9],
         [ 0, 1, 0, 9, -1, -1, -9],
         [ 0, 1, 0, 9, -1, -1, -9],
         [ 0, 1, 0, 9, -1, -1, -9],
         [ 0, 1, 0, 9, -1, -1, -9]],
    
    5 : [[ 9, 0, 0, 0, -1, -1, -9],
         [ 0, 0, 0, 0, -1, -1, -9],
         [ 0, 0, 0, 0, -1, -1, -9],
         [ 0, 0, 0, 0, -1, -1, -9],
         [ 9, 0, 0, 0, -1, -1, -9]],
    
    6 : [[ 0, 9, -9, -9, 0, 0, -9],
         [ 9, 9, -9, -9, 0, 0, -9],
         [ 9, 9, -9, -9, 0, 0, -9],
         [ 9, 9, -9, -9, 0, 0, -9],
         [ 0, 9, -9, -9, 0, 0, -9]],    
    }
'''
profPreferences = {
    0 : [[ 9, 0, 0, 0, 0, 0, 0],
         [ 9, 0, 0, 0, 0, 0, 0],
         [ 9, 0, 0, 0, 0, 0, 0],
         [ 9, 0, 0, 0, 0, 0, 0],
         [ 9, 0, 0, 0, 0, 0, 0]],
    
    1 : [[ 0, 9, 0, 0, 0, 0, 0],
         [ 0, 9, 0, 0, 0, 0, 0],
         [ 0, 9, 0, 0, 0, 0, 0],
         [ 0, 9, 0, 0, 0, 0, 0],
         [ 0, 9, 0, 0, 0, 0, 0]],
    
    2 : [[ 0, 0, 9, 0, 0, 0, 0],
         [ 0, 0, 9, 0, 0, 0, 0],
         [ 0, 0, 9, 0, 0, 0, 0],
         [ 0, 0, 9, 0, 0, 0, 0],
         [ 0, 0, 9, 0, 0, 0, 0]],
    
    3 : [[ 0, 0, 0, 9, 0, 0, 0],
         [ 0, 0, 0, 9, 0, 0, 0],
         [ 0, 0, 0, 9, 0, 0, 0],
         [ 0, 0, 0, 9, 0, 0, 0],
         [ 0, 0, 0, 9, 0, 0, 0]],
    
    4 : [[ 0, 0, 0, 0, 9, 0, 0],
         [ 0, 0, 0, 0, 9, 0, 0],
         [ 0, 0, 0, 0, 9, 0, 0],
         [ 0, 0, 0, 0, 9, 0, 0],
         [ 0, 0, 0, 0, 9, 0, 0]],
    
    5 : [[ 0, 0, 0, 0, 0, 9, 0],
         [ 0, 0, 0, 0, 0, 9, 0],
         [ 0, 0, 0, 0, 0, 9, 0],
         [ 0, 0, 0, 0, 0, 9, 0],
         [ 0, 0, 0, 0, 0, 9, 0]],
 
    6 : [[ 0, 0, 0, 0, 0, 0, 9],
         [ 0, 0, 0, 0, 0, 0, 9],
         [ 0, 0, 0, 0, 0, 0, 9],
         [ 0, 0, 0, 0, 0, 0, 9],
         [ 0, 0, 0, 0, 0, 0, 9]]
    }
'''

# Start the timer
start_time = timer()

# model instantiation
model = GeneticAlgorithm(DAYS, PERIODS, BREAK, basicCreditRequirements, profPreferences, allowRepetitions = False)

model.generateFirstPopulation_unique(POPULATION_SIZE)

for i in model.POPULATION:
    print(i)
    print()
    print()

print("Average fitness of Generation 1:", model.calcFitness())
print(model.fitnessValues)


for i in range(50):
    model.reproduce_SPC_rows_randomswap(noOfParents = 5)
    
    '''
    for j in model.POPULATION:
        print(j)
        print()
        print()
    '''
    
    print(f"Average fitness of Generation {i}: {model.calcFitness()}")
    print(model.fitnessValues)
    print("==================================================")

# End the timer
end_time = timer()

for i in model.POPULATION:
    print(i)
    print()
    
print("Timetable Generation ended.")

# Print out timer and results
total_time = print_time(start=start_time, end=end_time)
    





'''
print("=================================================================")
POPULATIONunique = model.generateFirstPopulation_unique(POPULATION_SIZE)
for i in POPULATIONunique:
    print(i)
    print()
    print()
    
model.calcFitness()
print(model.fitnessValues)
'''
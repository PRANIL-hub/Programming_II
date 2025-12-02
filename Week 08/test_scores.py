"""
set NUM_SCORES = 4
def main():
 scores=[]
 for i in range (1, NUM_SCORES+1)
  get score
  while score<0 or score>100:
   display test score should be between 0 and 100
  add score to the scores list
  jcu_grade = determines_jcu_grade(score) #function to determine jcu grade
  display jcu grades
 average_score= sum(scores)/len(scores)
 display average score

main()
"""
NUM_SCORES = 4
def main():
    scores = []
    for i in range(1, NUM_SCORES+1):
      score = float(input("Score : "))
      while score < 0 or score > 100:
          print("Test score should be between 0 & 100")
          score = float(input("Score : "))
      scores.append(score) #adds each score to the list

    for score in scores:
      jcu_grade = determines_jcu_grade(score)
      print(f"score {score}, which is {jcu_grade}")

    average_score = sum(scores) / len(scores)
    print(f"The average score was {average_score}")

def determines_jcu_grade(score):
    if score<50:
        return "F"
    elif score<65:
        return "P"
    elif score<75:
        return "C"
    elif score<85:
        return "D"
    else:
        return "HD"

main()
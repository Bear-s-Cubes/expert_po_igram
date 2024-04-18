import json
from ExpertSystem import Fact
from ExpertSystem import ExpertSystem

def get_QA(): 
    with open("AnswerQuestion.json", encoding="utf8") as aq_file:
        aq = json.load(aq_file)
    return aq

def main():
    expert = ExpertSystem()
    expert.reset()

    aq = get_QA()
    q = aq["Questions"]
    a = aq["Answers"]
    for key in q:
        print('\n' + q[key])
        x = str(input(f"{'\n'.join(a[key])}\n"))
        ans = key + "-" + x
        expert.declare(Fact(answ=ans))
        expert.run()

    game = expert.get_game()

    print(f'Поиграй в {game[0]}, бро!')

    return 0

if __name__ == '__main__':
    main()
    
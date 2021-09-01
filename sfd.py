question_list=["당신의 꿈은 무엇인가요?","그 꿈을 갖게 된 이유는 무엇인가요?","마지막으로, 그 꿈을 이루기 위해 어떤 일을 할 것인가요?"]
answer_list=[]

def ask(ask):
    a = input(ask+"\n")
    answer_list.append(a)
    print("\n")

for q in question_list :
    ask(q)

print(f"""당신의 꿈은 {answer_list[0]}이고
이유는 {answer_list[1]},
꿈을 이루기 위해 할 일은 {answer_list[2]}이군요.

꿈이 이뤄지길 바랍니다""")


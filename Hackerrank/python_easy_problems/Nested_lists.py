if __name__ == '__main__':
    L=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        L.append([name,score])
    # print(L) 
    
    scores = [sub_list[1] for sub_list in L]   
    # print("scores", scores)
    
    scores.sort()
    # print("sorted", scores)
    
    min_score = scores[0]
    scores = [x for x in scores if x != min_score]
    
    second_lowest_grade = scores[0]
    # print(second_lowest_grade) 
    
    target_students = [sub_list[0] for sub_list in L if sub_list[1] == second_lowest_grade]
    target_students.sort()
    # print(target_students)  
    for student in target_students:
        print(student)
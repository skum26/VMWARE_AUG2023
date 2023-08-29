# "This is problem 5 by S.Sivakumar"

# Program for greedy
# father --> 2+2+2 = 6 , 3rd 3+3+3+ 1 = 10, 2nd daughter 5+5+5+1 =16 1st daughter 8+8+8 +1 = 25

print("*"*20)
intial_total =0
for total in range(1,1000) :
    if total != 1 :
        total_after_first_daughter_son =  total-1
        if total_after_first_daughter_son % 3 == 0:
            first_daughter_share = total_after_first_daughter_son /3
            #print("first_daughter_share", total , first_daughter_share)

            total_after_second_daughter_son = first_daughter_share * 2 - 1
            if total_after_second_daughter_son % 3 == 0:
                second_daughter_share = total_after_second_daughter_son / 3
                #print("Second daughter took ", total, second_daughter_share)

                total_after_third_daughter_son = second_daughter_share * 2 - 1
                if total_after_third_daughter_son % 3 == 0:
                    third_daughter_share = total_after_third_daughter_son / 3
                    #print("Third daughter took ", total, third_daughter_share)

                    father_share_to_distrubute = third_daughter_share *2
                    if father_share_to_distrubute % 3 == 0:
                        each_daughter_share = father_share_to_distrubute / 3
                        print("Total in the basket               :", total)
                        print("First  daughter took", int(first_daughter_share),  ",+1 for son :", int(first_daughter_share+1))
                        print("Second daughter took", int(second_daughter_share), ",+1 for son :", int(second_daughter_share+1))
                        print("Third  daughter took", int(third_daughter_share),  ",+1 for son :", int(third_daughter_share+1))
                        print("Each daughter  share from father   :", int(each_daughter_share))
                        print("*" * 20)

else :
    print("PGM Completed")
    print("*" * 20)



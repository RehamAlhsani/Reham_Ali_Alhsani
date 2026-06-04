high_score_board = []

def record_game(player , *scores , bonus=0 , multiplier = 1.0) :
    """
    *scores : any number of round scores
    bonus : extra points added to the score
    multiplier : applied to the final score
    """

    if len(scores) == 0 :
        return player , 0 , 0 , "no rounds played"

    for score in scores :
        if score < 0 :
            return player , 0 , 0 , "negative score not allowed"

    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)
    rounds = len(scores)

    high_score_board.append((player , total))

    sorted_board = sorted (
        high_score_board ,
        key = lambda item : item[1] ,
        reverse = True
    )

    rank = 0
    for i , entry in enumerate(sorted_board , start = 1) :
        if entry == (player , total) :
            rank = i
            break

    if rank == 1 :
        status = "high score!"
    else :
        status = f"rank {rank}"

    return player , rounds , total , status

record_game("Reham", 20, 15, 10)
record_game("sara", 30, 25, bonus=5)
record_game("Ibtesam", 40, 20, multiplier=1.2)

print("Leaderboard :")
for player, score in high_score_board :
    print(player , score)
    